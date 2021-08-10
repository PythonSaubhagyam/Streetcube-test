import os
import random
import string
import stripe
import boto3
import datetime
from flask_mail import Mail, Message
from datetime import datetime, date
from datetime import timedelta
from datetime import time
from urllib.request import Request, urlopen
from flask import (Blueprint, request, render_template,
                   flash, session, redirect, url_for, abort, jsonify)
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from os.path import splitext
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from itsdangerous import URLSafeTimedSerializer
from streetcube import app, db, login_manager
from streetcube.home.forms import LoginForm,UserForm,UserLastNameForm,EmailForm, PasswordForm, MobileForm, MobileVerifyForm, TraderDetailsForm,TraderDetailsUploadForm, BookSlotForm, ShowBookDateForm,ContactForm,OtpForm,RegisterForm
from streetcube.models import UserInfo,UserRoles, TraderDetails, SlotBookingDetails, ShowBookDate,MemberOrder,Contact,SlotsInfo,Slots



app.config["S3_KEY"] =  'AKIAYXDYKG4AY34BHKFF'
app.config["S3_SECRET"] = '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'
app.config['AWS_REGION']='eu-west-2'

# app.config['MAIL_SERVER'] = 'smtp.hostinger.in'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'streetcube@appzack.com'
# app.config['MAIL_PASSWORD'] = 'mJ~^uuw1?X'
# app.config['MAIL_DEFAULT_SENDER'] = 'streetcube@appzack.com'
# mail = Mail(app)

# app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_JUiX8n2A3zlLoZ8HiMdF1VgF00iEQvMAgY'
# app.config['STRIPE_SECRET_KEY'] = 'sk_test_wi4psHh3LoBTiAkfwZKJiJo600sYCxeON3'

# stripe.api_key = app.config['STRIPE_SECRET_KEY']
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


@login_manager.user_loader
def load_user(id):
    return UserInfo.query.get(int(id))


def randomkey(stringLength=10):
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(stringLength))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



def send_email(subject,message,receipent_email_arr):
    
    SENDER = "StreetCube<info@streetcube.org>"
    TOADDRESSES = receipent_email_arr
    SUBJECT = subject
    BODY_HTML = message
    CHARSET = "UTF-8"
    client = boto3.client('pinpoint-email', aws_access_key_id=app.config["S3_KEY"],aws_secret_access_key=app.config["S3_SECRET"],region_name= app.config['AWS_REGION'])

    # Send the email....
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




# home = Blueprint('home', __name__, url_prefix='/home')
main = Blueprint('main', __name__)
# udash = Blueprint('udash', __name__, url_prefix='/udash')



 

 
'''
@main.route("/apply/<string:cano_url>",methods=['POST','GET'])
def apply(cano_url):
    apply_for = cano_url
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        email = request.form.get('email')
        uname = request.form.get('uname')
        lname = request.form.get('lname')
        hashed_password = generate_password_hash(request.form.get('lname'))
        password = hashed_password
        mobile = request.form.get('mobile')
        new_user = UserInfo(cano_url=apply_for,last_name=lname,uname=uname, email=email, password=password, mobile=mobile, user_role=3, is_show_mobile=1,
                                    is_mobile_verified=0, no_of_logins=0,address=0
                                    )
        
        if new_user:
            db.session.add(new_user)
            db.session.commit()
            session['mobile'] = mobile
            # return str(session['mobile'] )
            password_characters = string.digits
            otp = ''.join(random.choice(password_characters) for i in range(4))
            session['otp'] = otp
            # sms = "Your%20StreetCube%20mobile%20verification%204-digit%20pin:%20" + str(otp)
            sms = "Your StreetCube mobile verification 4-digit pin: " + str(otp)
            # gen_otp(sms, "%2b44" + mobile)
            send_sms("+44"+mobile,sms)

            # return str(send_status)
            return redirect(url_for('main.verify_otp_msg'))
            # return str("Saved database")
        else:
            return str("Something went wrong")
        
    return render_template('streetcube/partners.jinja2', title="Sign Up", form=form)

'''

@main.route("/home")
def home():
    # return 'tesing'+str(id)
    return render_template('reg.jinja2')


'''
@main.route('/otp-msg', methods=['GET', 'POST'])
def verify_otp_msg():
    try:
        if request.method == 'POST':
            otp = request.form.get('otp')
            
            if session.get('otp') == otp :
                upt_mobile = UserInfo.query.filter_by(mobile=session.get('mobile')).first()
                upt_mobile.is_mobile_verified = True
                db.session.commit()
                db.session.close()
               
                flash("Registration was successful", "success")
                return redirect(url_for('main.verified_msg'))

            else:
                flash("Please fill mobile no first")

        return render_template('otp-verification.jinja2', title="otp verification")

    except Exception as e:
        return str(e)
   
'''
@main.route("/process/mobile/verified")
def process_mobile_verified():
    try:
        form = OtpForm()
        if session.get('otp'):
            upt_mobile = UserInfo.query.filter_by(id=current_user.id).first()
            upt_mobile.is_mobile_verified = 1
            db.session.commit()
            db.close()
            session['last_id'] = new_user.id
            flash("Registration was successful", "success")
            return redirect(url_for('main.trader_details'))
        return render_template('otp-verification.jinja2', title="otp verification", form=form)
    except Exception as e:
        return str(e)
        


@main.route("/dashboard",methods=['GET','POST'])
def dashboard():
    if request.method == "GET":
        if current_user.is_authenticated:
            profile = UserInfo.query.filter_by(id=current_user.id).first()
            uer_role = UserRoles.query.filter_by(id= profile.user_role).first()
            pr = profile.id
            # return jsonify(uer_role.role_title)
            trader_profile = TraderDetails.query.filter_by(member_id=pr).first()
            #return jsonify(trader_profile.address)


            return render_template("dashboard.jinja2",user=profile,tr=trader_profile,role =uer_role)
        else:   
            return redirect(url_for('main.login'))
    else:
        uname = request.form.get('uname')
        role = request.form.get('role')
        email = request.form.get('email')
        mobile = request.form.get('mobile')
        address = request.form.get('address')
        c_name = request.form.get('c_name')
        b_name = request.form.get('b_name')
        des = request.form.get('descrip_of_service')
        story = request.form.get('story')


        u_profile = UserInfo.query.filter_by(id = current_user.id).update(dict(uname= uname,email=email,mobile=mobile,address=address))
        db.session.commit()
     
        trader_details_info = TraderDetails.query.filter_by(member_id=current_user.id).first()
        if 'pub_lib_insu' in request.files:
            pub_lib_insu = request.files['pub_lib_insu']
            pub_lib_insu_docs = secure_filename(pub_lib_insu.filename)
            filetype, extension = splitext(pub_lib_insu_docs)
            new_pub_lib_file = str(randomkey(25)).lower() + extension
            pub_lib_insu.save(os.path.join(Insurence_Doc , new_pub_lib_file))


            if trader_details_info:
                trader_details_info.pub_lib_insu = new_pub_lib_file
                db.session.commit()
                return jsonify({'status': 200, 'message': 'File uploaded successfully'})

            return jsonify({'status': 200, 'message': 'File uploaded'})


        elif 'c_19risk_asses' in request.files:
            c_19risk_asses = request.files['c_19risk_asses']
            c_19risk_asses_doc = secure_filename(c_19risk_asses.filename)
            filetype, extension = splitext(c_19risk_asses_doc)
            new_c_19risk_asses_file = str(randomkey(25)).lower() + extension
            c_19risk_asses.save(os.path.join(Covid19_Asses_Doc, new_c_19risk_asses_file))

            if trader_details_info:
                trader_details_info.c_19risk_asses = new_c_19risk_asses_file
                db.session.commit()
                return jsonify({'status': 200, 'message': 'File uploaded successfully'})

            return jsonify({'status': 200, 'message': 'File uploaded'})  
              

        elif 'food_certi' in request.files:
            food_certi = request.files['food_certi']
            food_certi_docs = secure_filename(food_certi.filename)
            filetype, extension = splitext(food_certi_docs)
            new_food_certi_file = str(randomkey(25)).lower() + extension
            food_certi.save(os.path.join(Food_Hygiene_Doc , new_food_certi_file))

            if trader_details_info:
                trader_details_info.food_certi = new_food_certi_file
                db.session.commit()
                return jsonify({'status': 200, 'message': 'File uploaded successfully'})

            return jsonify({'status': 200, 'message': 'File uploaded'})            
        
      
        t_profile = TraderDetails.query.filter_by(member_id = current_user.id).update(dict(email=email,mobile=mobile,address=address,c_name= c_name,b_name=b_name,descrip_of_service = des,story=story))
        db.session.commit()

        return redirect(url_for('main.dashboard'))  


@main.route('/delete/<id>', methods = ['GET', 'POST'])
@login_required
def delete(id):
    order_data = MemberOrder.query.get(id)
    db.session.delete(order_data)
    db.session.commit()
    flash("Order Deleted Successfully")
 
    return redirect(url_for('main.booked_details','success'))


#this is our update route where we are going to update our order
@main.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        order_data = MemberOrder.query.get(request.form.get('id'))
 
        order_data.name = request.form['name']
        order_data.email = request.form['email']
        order_data.phone = request.form['phone']
 
        db.session.commit()
        flash("Order Updated Successfully","success")
 
    return redirect(url_for('main.booked_details'))

# this is our change password route we are going to credential
@main.route('/change/pass', methods=['GET', 'POST'])
def change_pass():
    if request.method=='POST':
        user = UserInfo.query.filter_by(email=current_user.email).first()
        oldp = request.form.get('oldpass')  

        newp = request.form.get('newpass')
        confp = request.form.get('confpass')

        if check_password_hash(user.password, oldp):
            if user:
                if newp==confp:
                    hashed_password = generate_password_hash(request.form.get('newpass'))
                    password = hashed_password
                    ud = UserInfo.query.filter_by(email=current_user.email).update(dict(password=password))
                    db.session.commit()
                    flash("Your Password has been successfully Updated","success")
                    return redirect(url_for('main.change_pass'))
                else:
                    flash("New And Confirm Password Does Not  Matched !",'danger')
            else:
                flash("Something Went Wrong ! Try Again Later")

        else:
            flash("You Old Password Does Not Matched!",'danger')            
    return render_template("change-pass.jinja2")


# this is our show total booked record by the customer
@main.route('/booked/details', methods=['GET', 'POST'])
def booked_details():
    order_arr = []
    orders = MemberOrder.query.filter_by(member_id=current_user.id).all()
    for ordr in orders:
        slot_query = SlotBookingDetails.query.filter_by(member_id = ordr.member_id).all()
        for slt in slot_query:
            # return jsonify(slt.choose_slot)
            order_arr.append({'slot':slt.choose_slot,'id':ordr.id,'amount':ordr.amount,'txn_id':ordr.txn_id,'payment_status':ordr.payment_status,'date':ordr.create_at})
            # return jsonify(order_arr)
    return render_template("order-details.jinja2",order = order_arr)


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            user = UserInfo.query.filter_by(email=form.email.data, user_role=3).first()

            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)
                    setattr(user, 'no_of_logins', UserInfo.no_of_logins + 1)
                    # user.register_date(now)
                    db.session.commit()
                    db.session.flush()

                    if user.user_role == 3:
                        return redirect(url_for('main.booking_slot'))
                    else:
                        return redirect(url_for('main.home'))

                flash("Invalid Credentials Try Again Later", 'danger')
            else:
                flash("Email and Password is wrong", "danger")

        return render_template("login.jinja2", form=form)
    else:
        if not current_user.is_authenticated:
            form = LoginForm()
            return render_template("login.jinja2", form=form)
        else:
            return redirect(url_for('main.home'))



@main.route('/join_now', methods=['GET', 'POST'])
def join_now():
    form = EmailForm(request.form)
    if form.validate_on_submit():
        email = request.form.get('email')
        if email:
            session['email'] = email
        return redirect(url_for('main.user_info'))
    return render_template('join-now.jinja2', title="Join", form=form)



@main.route('/user/info',methods=['GET','POST']) 
def user_info():
    try:
        if session.get('email'):
            form = UserForm()
            if form.validate_on_submit():
                uname = request.form.get('uname')
                session['uname'] = uname
                return redirect(url_for('main.user_lname'))

            return render_template('user.jinja2', title="Auth-fname", form=form)
                
    except Exception as e:
        return str(e)


@main.route('/user/lname',methods=['GET','POST']) 
def user_lname():
    try:
        if session.get('email') and session.get('uname'):
            form = UserLastNameForm()
            if form.validate_on_submit():
                last_name = request.form.get('lname')
                session['lname'] = last_name
                return redirect(url_for('main.auth'))

            return render_template('lname.jinja2', title="Auth-lname", form=form)
                
    except Exception as e:
        return str(e)


@main.route('/auth', methods=['GET', 'POST'])
def auth():
    try:
        if session.get('email') and session.get('uname') and session.get('lname'):
            form = PasswordForm()
            if form.validate_on_submit():
                hashed_password = generate_password_hash(form.password.data)
                password = hashed_password
                session['password'] = password
                return redirect(url_for('main.invite_form'))

        return render_template('auth.jinja2', title="Auth", form=form)

    except Exception as e:
        return str(e)

'''
def gen_otp(sms, number):
    req = Request(
        "http://www.textapp.net/webservice/httpservice.aspx?method=sendsms&returncsvstring=false&externallogin=U20229808&password=6ryuhsum&clientbillingreference=n&clientmessagereference=n&originator=%2b442035152233&destinations=%2b" + str(
            number) +
        "&body=" + sms + "&validity=72&charactersetid=2&replymethodid=4&replydata=&statusnotificationurl=")
    resp = urlopen(req).read()
    return resp

'''
'''
@main.route("/resend/otp")
def resend_otp():
    password_characters = string.digits
    otp = ''.join(random.choice(password_characters) for i in range(4))
    session['otp'] = otp
    # sms = "Your%20StreetCube%20mobile%20verification%204-digit%20pin:%20" + str(otp)
    sms = "Your StreetCube mobile verification 4-digit pin: " + str(otp)
    mobile = session.get('mobile')
    # gen_otp(sms, "%2b44" + mobile)
    send_sms("+44"+mobile,sms)
    return redirect(url_for('main.verify_otp_msg'))
'''

@main.route('/invite-form', methods=['GET', 'POST'])
def invite_form():
    try:
        if session.get('uname') and session.get('lname') and session.get('email') and session.get('password'):
            form = MobileForm()
            if form.validate_on_submit():
                # is_show_mobile = request.form.get('is_show_mobile')
                mobile = request.form.get('mobile')
                # session['is_show_mobile'] = is_show_mobile
                session['mobile'] = mobile
                # return str(session['mobile'] )
                password_characters = string.digits
                otp = ''.join(random.choice(password_characters) for i in range(4))
                session['otp'] = otp
                # sms = "Your%20StreetCube%20mobile%20verification%204-digit%20pin:%20" + str(otp)
                sms = "Your StreetCube mobile verification 4-digit pin: " + str(otp)
                # gen_otp(sms, "%2b44" + mobile)
                send_sms("+44"+mobile,sms)

                # return str(send_status)
                return redirect(url_for('main.verify_otp_msg'))

        return render_template('invite-form.jinja2', title="Invite", form=form)

    except Exception as e:
        return str(e)


"""
@main.route('/mobile-verification', methods=['GET', 'POST'])
def mobile_verification():
    try:
        if session.get('email') and session.get('password') and session.get('mobile'):
            form = MobileVerifyForm()
            if form.validate_on_submit():
                is_mobile_verified = bool(request.form.get('is_mobile_verified'))
                session['is_mobile_verified'] = is_mobile_verified
                # flash("Registration was successful","success")
                return redirect(url_for('main.verify_otp_msg'))
            # else:
            #     flash("Please fill mobile no first")
            return render_template('mobile-verification.jinja2', title="mobile verification", form=form)

    except Exception as e:
        return str(e)
"""







'''
@main.route('/otp-msg', methods=['GET', 'POST'])
def verify_otp_msg():
    try:

        form = OtpForm()
        if session.get('uname') and session.get('email') and session.get('password') and session.get('mobile'):

            if form.validate_on_submit():
                uname = session['uname']
                lname = session['lname']
                email = session['email']
                password = session['password']
                mobile = session['mobile']
                # is_show_mobile = bool(session['is_show_mobile'])
                # is_mobile_verified = session['is_mobile_verified']

                new_user = UserInfo(last_name=lname,uname=uname, email=email, password=password, mobile=mobile, user_role=3, is_show_mobile=1,
                                    is_mobile_verified=1, no_of_logins=0,address=0
                                    ,cano_url=0)
                db.session.add(new_user)
                db.session.commit()

                session['last_id'] = new_user.id
                flash("Registration was successful", "success")
                return redirect(url_for('main.trader_details'))
            # else:
            #     flash("Please fill mobile no first")
        return render_template('otp-verification.jinja2', title="otp verification", form=form)

    except Exception as e:
        return str(e)

'''




@main.route('/verified-msg', methods=['GET', 'POST'])
def verified_msg():
    return render_template('verified-msg.jinja2')


@main.route('/trader-details', methods=['GET', 'POST'])
def trader_details():
    if session.get('email') and session.get('password'):
        # flash("You are logged in")
        try:
            form = TraderDetailsForm()
            # UserInfo.query.filter_by(id= session.get('last_id')).first()
            if form.validate_on_submit():

                address = form.address.data

                mobile = form.mobile.data
                email = form.email.data
                c_name = form.c_name.data
                b_name = form.b_name.data
                descrip_of_service = form.descrip_of_service.data
                story = form.story.data

                add_trader_details = TraderDetails(member_id=session.get('last_id'), address=address, mobile=mobile,
                                                   email=email, c_name=c_name,
                                                   b_name=b_name, descrip_of_service=descrip_of_service, story=story,pub_lib_insu=0,c_19risk_asses=0,food_certi=0)
                db.session.add(add_trader_details)
                db.session.commit()
                id = add_trader_details.id

                flash("Details was successfully added", "success")
                return redirect(url_for('main.upload_documents', id=id))
            else:
                # flash("Something went wrong")
                return render_template('trader-details.jinja2', title="Trader Details", form=form)
        except Exception as e:
            return str(e)
    else:
        flash("You are not logged in")
        return render_template('verified-msg.jinja2')


@main.route('/upload-documents/<int:id>', methods=['POST', 'GET'])
def upload_documents(id):
    return render_template('upload-documents.jinja2', id=id)


@main.route('/upload/documents/<int:id>', methods=['POST', 'GET'])
def upload_doc(id):
    if request.method == 'POST':
        id = id
        trader_details_info = TraderDetails.query.filter_by(id=id).first()
        if 'pub_lib_insu' in request.files:
            pub_lib_insu = request.files['pub_lib_insu']
            pub_lib_insu_docs = secure_filename(pub_lib_insu.filename)
            filetype, extension = splitext(pub_lib_insu_docs)
            new_pub_lib_file = str(randomkey(25)).lower() + extension
            pub_lib_insu.save(os.path.join(Insurence_Doc , new_pub_lib_file))


            if trader_details_info:
                trader_details_info.pub_lib_insu = new_pub_lib_file
                db.session.commit()
                return jsonify({'status': 200, 'message': 'File uploaded successfully'})

            return jsonify({'status': 200, 'message': 'File uploaded'})

        if 'c_19risk_asses' in request.files:
            c_19risk_asses = request.files['c_19risk_asses']
            c_19risk_asses_doc = secure_filename(c_19risk_asses.filename)
            filetype, extension = splitext(c_19risk_asses_doc)
            new_c_19risk_asses_file = str(randomkey(25)).lower() + extension
            c_19risk_asses.save(os.path.join(Covid19_Asses_Doc, new_c_19risk_asses_file))

            if trader_details_info:
                trader_details_info.c_19risk_asses = new_c_19risk_asses_file
                db.session.commit()
                return jsonify({'status': 200, 'message': 'File uploaded successfully'})

            return jsonify({'status': 200, 'message': 'File uploaded'})    

        if 'food_certi' in request.files:
            food_certi = request.files['food_certi']
            food_certi_docs = secure_filename(food_certi.filename)
            filetype, extension = splitext(food_certi_docs)
            new_food_certi_file = str(randomkey(25)).lower() + extension
            food_certi.save(os.path.join(Food_Hygiene_Doc , new_food_certi_file))

            if trader_details_info:
                trader_details_info.food_certi = new_food_certi_file
                db.session.commit()
                return jsonify({'status': 200, 'message': 'File uploaded successfully'})

            return jsonify({'status': 200, 'message': 'File uploaded'})        

        
        else:
            return jsonify({'error': 1, 'message': 'Sorry file is not uploaded.'})
    else:
        return jsonify({'error': 1, 'message': 'Sorry method is not allowed.'})


@main.route("/booking-slot", methods=["GET", "POST"])
@login_required
def booking_slot():
    # sl_info = SlotsInfo.query.filter_by(slot=slot).first()
    slot_details = Slots.query.all()
    return render_template('booking-slot.jinja2',slots = slot_details, isBooking=True)


@main.route("/booking/<int:id>", methods=["GET", "POST"])
@login_required
def booking(id):
    ide = id
    slot_list = SlotsInfo.query.filter_by(slot=id).first()
    s_price = slot_list.price
    try:
        form = BookSlotForm()
        if form.validate_on_submit():
            select_date = form.select_date.data
            date_arr = select_date.split(',')


            len_data = len(date_arr)
            total_price = int(len_data)*int(s_price) 
            s_arr = [] 
            c_date = []
            slots_data = SlotBookingDetails.query.filter_by(choose_slot=id).all()
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
                return redirect(url_for('main.booking', id = id))
                
            else: 
                add_slot_details = SlotBookingDetails(member_id=current_user.id,book_by=current_user.id,choose_slot=id, select_date=select_date,
                                                      booking_cost=total_price,hash_code=0)
                db.session.add(add_slot_details)
                db.session.commit()
                book_slot_id = add_slot_details.id
                # date_list=[]
                for list in date_arr:
                    l = ShowBookDate(book_id=book_slot_id,slot=id, book_date=list)
                    db.session.add(l)
                    db.session.commit()

                # return jsonify(date_list)
                session['total_price'] = total_price
                db.session.close()
                # today = date.today()
                return redirect(url_for('main.payment',ide = book_slot_id))
        else:
            s_date = ShowBookDate.query.filter_by(slot = id).all()
            # return str(date.today())
            x_date = []

            today = date.today()
            now = datetime.now()
            current_time = now.strftime("%H")
            # current_time = datetime.datetime.utcnow()
            # return str(current_time)
            t_arr = []

                  

            # block date for saturday    
            if today.weekday() == 5:
                sat_date = today + timedelta(1)
                x_date.append(today.strftime("%Y-%m-%d"))
                x_date.append(sat_date.strftime("%Y-%m-%d")) 

            # block date for thuresday
            if today.weekday() == 3:
                if current_time > str(12):
                    th_date = today + timedelta(3)
                    x_date.append(today.strftime("%Y-%m-%d"))
                    x_date.append(th_date.strftime("%Y-%m-%d"))
            
            # block date for friday         
            if today.weekday() == 4:
                fr_date = today + timedelta(2)
                x_date.append(today.strftime("%Y-%m-%d"))
                x_date.append(fr_date.strftime("%Y-%m-%d"))        

            # block date for saturday    
            if today.weekday() == 5:
                sat_date = today + timedelta(1)
                x_date.append(today.strftime("%Y-%m-%d"))
                x_date.append(sat_date.strftime("%Y-%m-%d")) 

            # block date for sunday
            if today.weekday() == 6:
                sun_date = today
                x_date.append(sun_date.strftime("%Y-%m-%d"))    

            

            # return jsonify(x_date)    
            for rs in s_date:
                x_date.append(rs.book_date.strftime("%Y-%m-%d"))
            return render_template('booking.jinja2',list_date=x_date, s_price=s_price,form=form,ide = id,key=stripe_keys['publishable_key'])
    except Exception as e:
        return str(e)


@main.route('/payment/<int:ide>', methods=['POST', 'GET'])
@login_required
def payment(ide):
    if request.method == 'POST':

        amount = int(session['total_price'])*100
        # return str(amount*100)
        # transactionID = chargeJson['balance_transaction'];
        customer = stripe.Customer.create(email=request.form['email'], source=request.form['token'])
        charge = stripe.Charge.create(
            customer=customer.id,
            description='My Street Cube Pay',
            amount=amount,
            currency='GBP',

        )

        orders = MemberOrder(member_id= current_user.id,slot_book_id=ide, amount=(amount/100),payment_status ='Paid',payment_response="success")
        db.session.add(orders)
        db.session.commit()

        user = UserInfo.query.filter_by(id=current_user.id).first()
        eml = [user.email]
        mob = "+91"+str(user.mobile)


        msg_subject = 'Payment went successful your slot is booked'
        # msg.body = 'This link generated by StreetCube for slot booking if you want to proceed Please click on the link given bellow<br>'
        book_slot = SlotBookingDetails.query.filter_by(id=ide).first()
        # return str(book_slot.choose_slot)
        msg_body = render_template('activate.html',name = orders.member_name,slot = book_slot.choose_slot,sdate=book_slot.select_date,amt = (amount/100))
        # mail.send(msg)


        send_email(msg_subject,msg_body,eml)
        send_sms(mob,"Check Payment Link Your Registered Email")
        flash(f'A test message was sent to {eml}.')
        return redirect(url_for('main.thanku'))


    return render_template('payment.jinja2')


@main.route('/thanku')
def thanku():
    return render_template('thanku.jinja2')


@main.route('/fail')
def fail():
    return render_template('fail.jinja2')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    try:
        form = ContactForm()
        if form.validate_on_submit():
            full_name = form.full_name.data
            email = form.email.data
            subject = form.subject.data
            message = form.msg.data
            add_contact = Contact(full_name=full_name, email=email, subject=subject, msg=message)
            db.session.add(add_contact)
            db.session.commit()

            flash("Contact details was successful send", "success")
            # return redirect(url_for('main.home'))

        return render_template('contact-us.jinja2', form=form)
    except Exception as e:
        return str(e)


@main.route('/about')
def about():
    return render_template('about-us.jinja2')


@main.route('/customer/pay/<string:ids>/<string:name>/<string:hcode>/<string:slot>/<string:price>', methods=['GET', 'POST'])
def c_pay(ids,name,hcode,slot,price):
    s_block = SlotBookingDetails.query.filter_by(hash_code= hcode).first()

    if s_block:
        if request.method == 'POST':
            amount = int(s_block.booking_cost)*100
            # transactionID = chargeJson['balance_transaction'];
            customer = stripe.Customer.create(email=request.form['email'], source=request.form['token'])

            charge = stripe.Charge.create(
                customer=customer.id,
                description='My Street Cube Pay',
                amount=amount,
                currency='GBP',

            )
            stripe.Charge.retrieve(
              "ch_1HuB0A2eZvKYlo2CoYdtz2IX",
            )
            orders = MemberOrder(member_id=s_block.member_id,slot_book_id=s_block.id, amount=(amount/100), payment_status='Paid',payment_response="success")
            db.session.add(orders)
            db.session.commit()
            usr = UserInfo.query.filter_by(id= ids).first()
            adm = UserInfo.query.filter_by(user_role=1).first()
            a_m = "+91"+str(adm.mobile)

            u_m = "+91"+str(usr.mobile)
            if s_block:
                s_block.hash_code=""
                db.session.commit()
                u_msg = "Your slot booked successfully "
                send_sms(u_m,u_msg)
                a_msg = "Paid successfully for slot "+" "+slot+" "+"by customer mobile number is  "+u_m+""

                # a_msg = "Name "+" "+has booked slot  and user had successfully paid amount Please check your admin dashbord for more information
                send_sms(a_m,a_msg)


                '''
                user = UserInfo.query.filter_by(id=current_user.id).first()
                eml = user.email
                msg = Message('Payment went successful your slot is booked', recipients=[eml])
                # msg.body = 'This link generated by StreetCube for slot booking if you want to proceed Please click on the link given bellow<br>'
                book_slot = SlotBookingDetails.query.filter_by(id=s_block.id).first()
                # return str(book_slot.choose_slot)
                msg.html = render_template('activate.html',name = orders.member_name,slot = book_slot.choose_slot,sdate=book_slot.select_date,amt = amount)
                mail.send(msg)
                flash(f'A test message was sent to {eml}.')
                '''
                return redirect(url_for('main.thanku'))
            else:
                return redirect(url_for('main.fail'))

    return render_template('customer-pay.jinja2',s_block=s_block)


@main.route('/logout')
def logout():
    logout_user()
    flash("You are successfully logout...", 'success')
    return redirect(url_for('main.login'))

'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.jinja2')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.jinja2')

'''
