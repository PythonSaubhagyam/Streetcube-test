import os
import random
import string
import stripe
import boto3
from array import *
from datetime import date
from datetime import datetime, timedelta
from itsdangerous import URLSafeTimedSerializer
from flask import (Blueprint, request, render_template,
				   flash, session, redirect, url_for, abort, jsonify)
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_mail import Mail, Message
from functools import wraps
from os.path import splitext
from sqlalchemy.sql.functions import func
from urllib.request import Request, urlopen
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from streetcube import app, db, login_manager
from streetcube.admin.forms import UserForm, BookSlotForm, LoginForm, EmailForm, PasswordForm
from streetcube.models import UserInfo, TraderDetails, SlotBookingDetails, ShowBookDate, MemberOrder, Contact, UserAccess, \
	UserRoles,SlotsInfo,Slots

# app.config['MAIL_SERVER'] = 'smtp.hostinger.in'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'streetcube@appzack.com'
# app.config['MAIL_PASSWORD'] = 'mJ~^uuw1?X'
# app.config['MAIL_DEFAULT_SENDER'] = 'streetcube@appzack.com'
# mail = Mail(app)



app.config["S3_KEY"] =  'AKIAYXDYKG4AY34BHKFF'
app.config["S3_SECRET"] = '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'
app.config['AWS_REGION']='eu-west-2'

admin = Blueprint('admin', __name__, url_prefix='/admin')
# admin = Blueprint('admin', __name__)


def send_email(subject,message,receipent_email_arr):
    
    SENDER = "StreetCube<info@streetcube.org>"
    TOADDRESSES = receipent_email_arr
    SUBJECT = subject
    BODY_HTML = message
    CHARSET = "UTF-8"
    client = boto3.client('pinpoint-email', aws_access_key_id=app.config["S3_KEY"],aws_secret_access_key=app.config["S3_SECRET"],region_name= app.config['AWS_REGION'])

    # Send the email.
    try:
        
        response = client.send_email(
            FromEmailAddress=SENDER,
            Destination={
                'ToAddresses': TOADDRESSES,
            },
            Content={
                'Simple': {
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML
                        },
                    }
                }
            },
        )
    
    except Exception as e:
        return 'fail'
    else:
        return 'sent'
   


def send_sms(mobile,message):
   
    client = boto3.client("sns",aws_access_key_id=app.config["S3_KEY"],aws_secret_access_key=app.config["S3_SECRET"],region_name= app.config['AWS_REGION'])
    try:
        client.publish(
            PhoneNumber = mobile,
            Message = message
        )
        return 'sent'
    except Exception as e:
        return str(e)




@login_manager.user_loader
def load_user(id):
	return UserInfo.query.get(int(id))

def randomkey(stringLength=10):
	password_characters = string.ascii_letters + string.digits
	return ''.join(random.choice(password_characters) for i in range(stringLength))


stripe_keys = {
  'secret_key': 'sk_test_51HUXyLHFUNWUCikXNXjuvwWzWSr8mEofHg6AnoLJAPtDDa3ttvmRxBEvUpQlbf8jKpU6zo552P3k8AKs3nG5rtrp00P0Ts1Lkw',
  'publishable_key': 'pk_test_51HUXyLHFUNWUCikXvrFR7ePlRKwFDdEFwHT2r2YIOhG1gybw0Sb8BNQ8Fh0lfZpNS70hD8qwD0lnlPVAzLgunTmX009PyJNL3Z'
}

stripe.api_key = stripe_keys['secret_key']

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Insurence_Doc = basedir + '/static/insurence_doc/'
Covid19_Asses_Doc = basedir + '/static/covid19_asses_doc/'
Food_Hygiene_Doc = basedir + '/static/food_hygiene_doc/'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov', 'jfif', 'docx'])





def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (
				getattr(form, field).label.text,
				error
			), 'info')

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def admin_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if current_user.user_role == 1:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('admin.dashboard'))
	return wrap


'''
def send_async_email(msg):
	with app.app_context():
		mail.send(msg)
'''		

'''
def send_email(subject, recipients, html_body):
	msg = Message(subject, recipients=recipients)
	msg.html = html_body
	thr = Thread(target=send_async_email, args=[msg])
	thr.start()
'''


def send_password_reset_email(user_email):
	password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

	password_reset_url = url_for('admin.reset_with_token',token=password_reset_serializer.dumps(user_email, salt='password-reset-salt'),_external=True)

	html = render_template(
		'admin/email_password_reset.html',
		password_reset_url=password_reset_url)

	send_email('Password Reset Requested',html, [user_email])




def show_hide_user_menu(user_id):
	u_acc = UserAccess.query.filter_by(member_id=user_id).first()
	acc_menu = u_acc.authenticate.split(",")
	return acc_menu

@admin.route("/")
# @admin_required
def dashboard():

	if current_user.is_authenticated:

	   total_ueser = db.session.execute('select count(id) as c from user_info').scalar()
	   amt = db.session.execute('select sum(amount) as c from member_order').scalar()
	   total_order = db.session.execute('select count(id) as c from slot_booking_details').scalar()
	   contact = db.session.execute('select count(id) as c from contact').scalar()

	   # acc =show_hide_user_menu(current_user.id)
	  
	   if current_user.user_role == 1:
		   return render_template("admin/index.jinja2",total_ueser= total_ueser,amt=amt,contact=contact,total_order=total_order)
	   else:
		   return render_template("admin/user-access.jinja2")
	else:
		return redirect(url_for('admin.admin_login'))
	 
	


@admin.route("/login", methods=['POST','GET'])
def admin_login():
	form = LoginForm(request.form)
	if request.method == 'POST':

		if form.validate():

			user = UserInfo.query.filter_by(email=form.email.data).first()
			if user:
				if check_password_hash(user.password, form.password.data):
					login_user(user)
					setattr(user, 'no_of_logins', UserInfo.no_of_logins + 1)

					db.session.commit()
					db.session.flush()
					return redirect(url_for('admin.dashboard'))
				flash("Invalid Credentials Try Again Later", 'danger')
			else:
				flash("Email and Password is wrong", "danger")

	return render_template("admin/auth-signin.jinja2",form=form)


@admin.route('/price/<int:slot>')
def slotbyprice(slot):
    slot = SlotsInfo.query.filter_by(slot=slot).first()
    return jsonify({'slotprice' : str(slot.price)})


@admin.route("slot/entry", methods=['POST','GET'])
def slot_info():
	slots_d = Slots.query.all()

	if request.method == "POST":
		if request.form.get("save"):
			slot = request.form.get('slots')
			sl_price = request.form.get('sprice')
			s_details = SlotsInfo(slot = slot, price = sl_price)
			if s_details:
				db.session.add(s_details)
				db.session.commit()
				flash("Slot Inserted Successfully", "success")
			else:	
				flash("Opps! Something Went Wrong", "warning")
				
		elif request.form.get("update"):
			slot = request.form.get('slots')
			sl_price = request.form.get('sprice')
			add_access = SlotsInfo.query.filter_by(slot = slot).update(dict(price=sl_price))
			if add_access:
				db.session.commit()
				flash("Slot Updated Successfully", "success")
			else:
				flash("Opps! Something Went Wrong", "warning")
			
	
	return render_template("admin/slots-intry.jinja2" , price = slots_d)




@admin.route("/user/restrict/<int:id>", methods=["GET","POST"])
def user_block(id):
	try:
		form = UserForm()
		if request.method=='GET':
			user = UserInfo.query.filter_by(id=id).first()
			uacc = UserAccess.query.filter_by(member_id=id).first()
			
			forms = UserForm(obj=user)
			if current_user.user_role == 1:
				return render_template("admin/user-restriction.jinja2",form=forms,id=id, acc = uacc)
			else:
				return render_template("admin/user-access.jinja2")

			
		if request.method=='POST':
			uname = request.form.get('uname')
			email = request.form.get('email')
			mobile = request.form.get('mobile')
			password = request.form.get('password')
			hashed_password = generate_password_hash(password)
			password = hashed_password
			uid=request.form.get('uid')
			update_user = UserInfo.query.filter_by(id=uid).update(dict(uname=uname,email=email,mobile=mobile,password=password))
			db.session.commit()
			

			# add privacy data into database
			a_list = request.form.getlist('auth')
			auth_list = ",".join(a_list)
			# get_user = uid
			add_access = UserAccess.query.filter_by(member_id = uid).update(dict(authenticate=auth_list))
			if add_access:
				db.session.commit()
				flash('User updated successfully','success')
			else:
				add = UserAccess(member_id=uid,authenticate=auth_list)
				db.session.add(add)
				db.session.commit()
				flash('User add successfully','success')
			
			
			
			if current_user.user_role == 1:
				return render_template("admin/user-restriction.jinja2",form=form)
			else:
				return render_template("admin/user-access.jinja2")	

	except Exception as e:
		return str(e)		

	



'''
@admin.route("/signup")
def admin_signup():
   return render_template("admin/auth-signup.jinja2")
'''
@admin.route("/user/access", methods=["GET", "POST"])
def access():
	try:
		form = UserForm()
		if request.method == 'POST':
			username = form.uname.data
			email = form.email.data
			mobile = form.mobile.data
			hashed_password = generate_password_hash(form.password.data)
			password = hashed_password
			add_user = UserInfo(user_role=2,uname=username,last_name=0, email=email, mobile=mobile, password=password,address=0, is_show_mobile=0, is_mobile_verified=0,no_of_logins=0)
			db.session.add(add_user)
			db.session.commit()

			# add privacy data into database
			a_list = request.form.getlist('auth')
			auth_list = ",".join(a_list)
			get_user = add_user.id
			add_access = UserAccess(member_id = get_user, authenticate=auth_list)
			db.session.add(add_access)
			db.session.commit()

			flash("Registration was successfully with privileges")
			


			return redirect(url_for('admin.dashboard'))

		return render_template("admin/privileges.jinja2",form=form)
	except Exception as e:
		return str(e)


@admin.route("/reset", methods=["GET", "POST"])
def reset():
	form = EmailForm()
	if form.validate_on_submit():
		try:
			user = UserInfo.query.filter_by(email=form.email.data).first_or_404()
		except:
			flash('Invalid email address!', 'error')
			return render_template('admin/auth-reset-password.jinja2', form=form)

		if user.is_email_verified:
			send_password_reset_email(user.email)
			flash('Please check your email for a password reset link.', 'success')
			send_sms("+91"+str(user.mobile),"Please check your email for a password reset link")
		else:
			flash('Your email address must be confirmed before attempting a password reset.', 'error')
		return redirect(url_for('admin.admin_login'))
	return render_template("admin/auth-reset-password.jinja2", form=form)


@admin.route('/reset/<token>', methods=["GET", "POST"])
def reset_with_token(token):
	try:
		password_reset_serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
		email = password_reset_serializer.loads(token, salt='password-reset-salt', max_age=3600)
	except:
		flash('The password reset link is invalid or has expired.', 'error')
		return redirect(url_for('admin.admin_login'))

	form = PasswordForm()

	if form.validate_on_submit():
		try:
			user = UserInfo.query.filter_by(email=email).first_or_404()
		except:
			flash('Invalid email address!', 'error')
			return redirect(url_for('admin.admin_login'))

		
		user.password = generate_password_hash(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Your password has been updated!', 'success')
		return redirect(url_for('admin.admin_login'))

	return render_template('admin/reset_password_with_token.jinja2', form=form, token=token)




@admin.route("/show/user")
def show_user_list():
	user_list = UserInfo.query.all()
	acc =show_hide_user_menu(current_user.id)
	if '3' in acc:
		return render_template("admin/user-list-table.jinja2",user_list=user_list)
	else:
		return render_template("admin/user-access.jinja2")


@admin.route("/show/trader/list")
def show_trader_list():
   trader_list = TraderDetails.query.all()
   return render_template("admin/trader-list-table.jinja2",trader_list=trader_list)


@admin.route("/show/slot/book/list")
def show_slot_book_list():
	slot_d_list = SlotBookingDetails.query.all()
	slotarr=[]
	pay_arr = []
	paid=''
	for slot in slot_d_list:
		mid = slot.member_id
		
		order = MemberOrder.query.filter_by(member_id=slot.member_id,slot_book_id=slot.id).first()

		if order:
			pay = order.payment_status
			if pay:
				paid = "Paid"
		else:
			paid = "Fail"
		m_name = UserInfo.query.filter_by(id=mid).first()
	
			
		slotarr.append({'book_by':current_user.uname,'uname': m_name.uname,'choose_slot':slot.choose_slot,'select_date':slot.select_date,'booking_cost':slot.booking_cost,'register_date':slot.register_date,'is_expired':slot.is_expired,'paid':paid})
	# return jsonify(paid)		
	return render_template("admin/show-slot-book-list-table.jinja2",slot_d_list=slotarr)
   

@admin.route("/show/order/list")
def show_order_list():
	book_list_arr = []
	slot_query = MemberOrder.query.all()
	for slt in slot_query:
		book_query = SlotBookingDetails.query.filter_by(member_id=slt.member_id).first()    
		
		user_det = UserInfo.query.filter_by(id=slt.member_id).first()
			
		book_list_arr.append({'user_name': user_det.uname, 'choose_slot': book_query.choose_slot,'select_date':book_query.select_date,'booking_cost':slt.amount,'txn_id': slt.txn_id, 'payment_status':slt.payment_status, 'payment_response':slt.payment_response,'create_at':slt.create_at}) 
	# return jsonify(book_list_arr)
	acc =show_hide_user_menu(current_user.id)
	if current_user.user_role == 1:
		return render_template("admin/show-order-details.jinja2",order_data = book_list_arr)
	else:
		return render_template("admin/user-access.jinja2")	


@admin.route("/check_email",methods =['POST'])
def check_email():
	# get email from you form data
	email = request.form.get("email")
	# check if someone already register with the email
	user = UserInfo.query.filter_by(email=email).first()
	if not user:
		return str(1)
	else:
		return str(0)


@admin.route("/create/user",methods=['POST','GET'])
def create_user():
	roleList = db.session.execute("SELECT * FROM user_roles order by role_title")
	try:
		if request.method=='POST':
			uname = request.form.get('uname')
			email = request.form.get('email')
			hashed_password = generate_password_hash(request.form.get('password'))
			password = hashed_password
			u_role = request.form.get('u_role')
			address = request.form.get('address')
			mobile =  request.form.get('mobile')

			c_name = request.form.get('c_name')
			b_name = request.form.get('b_name')
			descrip_of_service = request.form.get('descrip_of_service')
			story = request.form.get('story')

			member = UserInfo(uname=uname,last_name=0,email=email,password=password ,user_role= u_role, address=address,mobile=mobile,is_show_mobile=0,is_mobile_verified=1,no_of_logins=0)

			db.session.add(member)
			db.session.commit()

			pub_lib_insu = request.form.get('pub_lib_insu')
			c_19risk_asses = request.form.get('c_19risk_asses')
			food_certi = request.form.get('food_certi')


			t_details = TraderDetails(  member_id=member.id, address=address, mobile=mobile, email=email, c_name=c_name, b_name= b_name, descrip_of_service =descrip_of_service, story =story,pub_lib_insu=pub_lib_insu,c_19risk_asses=c_19risk_asses,food_certi=food_certi )


			db.session.add(t_details)
			db.session.commit()

			if member and t_details:
				flash("Success! Account created Successfully")
			else:
				flash("Error! Account not created")
			return redirect(url_for('admin.dashboard'))
		else:
			acc =show_hide_user_menu(current_user.id)
			if '2' in acc:
				return render_template("admin/create-user.jinja2",roleList=roleList)
			else:
				return render_template("admin/user-access.jinja2")

	except Exception as e:
		return str(e)


@admin.route('/thanku')
def thanku():
	return render_template('admin/thanku.jinja2')

@admin.route('/fail')
def fail():
	return render_template('admin/fail.jinja2')


@admin.route('/slot/report')
def slot_report():
	try:
		today_day = date.today() 
		
		fri = []
		sat = []
		sun = []
		#days=[]

		today_days=datetime.today().strftime('%A')
		
		if today_days=='Monday':
			dtfri = date.today() + timedelta(4)
			dtsat = date.today() + timedelta(5)
			dtsun = date.today() + timedelta(6)
		elif today_days=='Tuesday':
			dtfri = date.today() + timedelta(3)
			dtsat = date.today() + timedelta(4)
			dtsun = date.today() + timedelta(5)
		elif today_days=='Wednesday':
			dtfri = date.today() + timedelta(2)
			dtsat = date.today() + timedelta(3)
			dtsun = date.today() + timedelta(4)
		elif today_days=='Thursday':
			dtfri = date.today() + timedelta(1)
			dtsat = date.today() + timedelta(2)
			dtsun = date.today() + timedelta(3)

		# if dayfri=='Friday':
		queryfri = ShowBookDate.query.filter_by(book_date=dtfri).all()
		for fr in queryfri:
			slot_query = SlotBookingDetails.query.filter_by(id=fr.book_id).all()
			for slt in slot_query:
				user_det = UserInfo.query.filter_by(id=slt.member_id).all()
				for usr in user_det:
					fri.append({'user_name': usr.uname, 'contact': usr.mobile, 'slot': slt.choose_slot,
								'cost': str(slt.booking_cost), 'date': fr.book_date, 'day': 'Friday'})
		# if daysat=='Saturday':
		querysat = ShowBookDate.query.filter_by(book_date=dtsat).all()
		for st in querysat:
			slot_query = SlotBookingDetails.query.filter_by(id=st.book_id).all()
			for slt in slot_query:
				user_det = UserInfo.query.filter_by(id=slt.member_id).all()
				for usr in user_det:
					fri.append({'user_name': usr.uname, 'contact': usr.mobile, 'slot': slt.choose_slot,
								'cost': str(slt.booking_cost), 'date': st.book_date, 'day': 'Saturday'})
		# if daysun=='Sunday':
		querysun = ShowBookDate.query.filter_by(book_date=dtsun).all()
		for sn in querysun:
			slot_query = SlotBookingDetails.query.filter_by(id=sn.book_id).all()
			for slt in slot_query:
				user_det = UserInfo.query.filter_by(id=slt.member_id).all()
				for usr in user_det:
					fri.append({'user_name': usr.uname, 'contact': usr.mobile, 'slot': slt.choose_slot,
								'cost': str(slt.booking_cost), 'date': sn.book_date, 'day': 'Sunday'})

		# all.append({'fri':fri})
		#return jsonify(today)
		if current_user.user_role == 1:
			return render_template('admin/slot-report.jinja2', fri=fri)
		else:
			return render_template("admin/user-access.jinja2")	

	except Exception as e:
		return str(e)



@admin.route('/upload/documents', methods=['POST','GET'])
def upload_doc():
	if request.method == 'POST':
		if 'pub_lib_insu' in request.files:
			pub_lib_insu = request.files['pub_lib_insu']
			pub_lib_insu_docs = secure_filename(pub_lib_insu.filename)
			filetype, extension = splitext(pub_lib_insu_docs)
			new_pub_lib_file = str(randomkey(25)).lower() + extension
			pub_lib_insu.save(os.path.join(Insurence_Doc, new_pub_lib_file))
			return jsonify({'status': 200, 'message': 'File uploaded successfully','pub_file_path':new_pub_lib_file})


		if 'c_19risk_asses' in request.files:
			c_19risk_asses = request.files['c_19risk_asses']
			c_19risk_asses_doc = secure_filename(c_19risk_asses.filename)
			filetype, extension = splitext(c_19risk_asses_doc)
			new_c_19risk_asses_file = str(randomkey(25)).lower() + extension
			c_19risk_asses.save(os.path.join(Covid19_Asses_Doc, new_c_19risk_asses_file))
			return jsonify({'status': 200, 'message': 'File uploaded successfully','c_file_path':new_c_19risk_asses_file})

		if 'food_certi' in request.files:
			food_certi = request.files['food_certi']
			food_certi_docs = secure_filename(food_certi.filename)
			filetype, extension = splitext(food_certi_docs)
			new_food_certi_file = str(randomkey(25)).lower() + extension
			food_certi.save(os.path.join(Food_Hygiene_Doc + new_food_certi_file))
			return jsonify({'status': 200, 'message': 'File uploaded successfully','f_file_path':new_food_certi_file})

		else:
			return jsonify({'error': 1, 'message': 'Sorry file is not uploaded.'})
	else:
		return jsonify({'error': 1, 'message': 'Sorry method is not allowed.'})


@admin.route('/logout')
def logout():
	logout_user()
	flash("You are successfully logout...",'success')
	return redirect(url_for('admin.admin_login'))



@admin.route('/date/block/<int:id>')
def dblock(id):
	s_date = ShowBookDate.query.filter_by(slot = id).all()
	x_date = []
	for rs in s_date:
		x_date.append(rs.book_date.strftime("%Y-%m-%d"))
	return jsonify({'block_date':x_date})
	
		
@admin.route("/slot/price/<int:id>")
def sprice(id):
	slot_list = SlotsInfo.query.filter_by(slot=id).first()
	s_price = slot_list.price
	return str(s_price)




@admin.route("/slot/book/<int:id>", methods=['POST', 'GET'])
def slot_book(id):
	random_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=25))
	try:
		s_price =''
		choose_slot = ''
		form = BookSlotForm()
		if form.validate_on_submit():
			select_date = form.select_date.data
			choose_slot = form.choose_slot.data

			# slot_list = SlotsInfo.query.filter_by(slot=choose_slot).first()
			# s_price = slot_list.price

			date_arr = select_date.split(',')
			len_data = len(date_arr)
			total_price = int(len_data) * int(2)
			s_arr = []
			c_date = []
			
			slots_data = SlotBookingDetails.query.filter_by(choose_slot=choose_slot).all()
			for sdata in slots_data:
				c_date.append(sdata.select_date)
			
			for ch_date in date_arr:
				if ch_date in str(c_date):
					s_arr.append(ch_date)
					
			nt_arr=[]		
			if s_arr:	
				#return jsonify(s_arr)
				for check_date in date_arr:
					if check_date not in s_arr:
						nt_arr.append(check_date)

				flash( "Slot booked on"+" "+str(s_arr)+" "+"Day"+" "+"Slot available on "+" "+str(nt_arr)+" "+"Date")
				return redirect(url_for('admin.slot_book', id=id))

			else:	

				add_slot_details = SlotBookingDetails(book_by=current_user.id,member_id=id, choose_slot=choose_slot,select_date=select_date,booking_cost=total_price, hash_code=random_code)
				# blank_slot = sho
				# if a
				db.session.add(add_slot_details)
				db.session.commit()

				# date_list=[]
				s_date = ''
				for list in date_arr:
					l = ShowBookDate(book_id=add_slot_details.id, book_date=list)
					db.session.add(l)
					db.session.commit()

					# return jsonify(date_list)
					session['total_price'] = total_price
					db.session.close()
					user = UserInfo.query.filter_by(id=id).first()
					eml = [user.email]
					mob = "+44"+str(user.mobile)

					# return str(total_price)

					# pay_url = f"http://localhost:5000/customer/pay/{id}/{user.uname}/{random_code}/{choose_slot}/{select_date}/{total_price}"
					pay_url = f"http://market.streetcube.org/customer/pay/{id}/{user.uname}/{random_code}/{choose_slot}/{total_price}"
					# pay_url = "<a href='localhost:5000/customer/pay/{id}'>ckick here </a>"
					# msg = Message('Payment link for slot booking,StreetCube', recipients=[eml])
					msg_subject = 'Payment link for slot booking,StreetCube'
					# msg.body = ('This link generated by streetcube for slot booking if you want to proceed Please click on the link given bellow<br>'+pay_url)
					msg_body = render_template('sendmail.html', ids=id, name=user.uname, hcode=random_code,
											   slot=choose_slot, sdate=select_date, price=str(total_price) )

					# mail.send(msg)

					send_email(msg_subject,msg_body,eml)
					# send_sms(mob,"Check Payment Link Your Registered Email "+" Your Slot  "+choose_slot+" Amount "+str(total_price)+" Click bellow link "+pay_url )
					send_sms(mob,"Your market pitch reservation for "+" "+select_date+" is now booked, pending payment. "+" Click "+pay_url+" to complete the payment process.")
					flash(f'A test message was sent to {eml}.')

					return redirect(url_for('admin.slot_book', id=id))
		
		if current_user.user_role == 1:	
			return render_template('admin/slot-book.jinja2',form=form,key=stripe_keys['publishable_key'])
		else:
		    return render_template("admin/user-access.jinja2")		
	except Exception as e:
		return str(e)



'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.jinja2')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.jinja2')
'''





