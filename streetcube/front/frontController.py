import os
import random
import string
import stripe
import boto3
import datetime
import decimal
from PIL import Image
from flask_mail import Mail, Message
from datetime import datetime, date
from datetime import timedelta
from datetime import time
from urllib.request import Request, urlopen
from flask import (Blueprint, request, render_template,
                   flash, session, redirect, url_for, abort, jsonify,json)
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from os.path import splitext
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from itsdangerous import URLSafeTimedSerializer
from streetcube import app, db, login_manager
from streetcube.models import UserInfo,UserRoles,Food_style_details,Gazebo_process_3rd,Gazebo_process_4th,Gazebo_process_5th,Gazebo_process_6th,Gazebo_process_7th,Gazebo_process_8th,Gazebo_process_9th,Gazebo_process_10th,Gazebo_process_11th,Gazebo_process_12th,TraderDetails, SlotBookingDetails, ShowBookDate,MemberOrder,Contact,SlotsInfo,Slots,SampleCheckData,ProductList
from functools import wraps, update_wrapper



app.config["S3_KEY"] =  'AKIAYXDYKG4AY34BHKFF'
app.config["S3_SECRET"] = 'LC/HaituV4HLhUnyv+QBky7DbgTaRnBecJqU1Q4U'
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
PROOF_OF_NCASS_TRAINING_OR_EQUIVALENT_DOC = basedir + '/static/images/proof_of_ncass_training_or_equivalent_doc/'
CV_DOC = basedir + '/static/images/cv_doc/'
LEVEL_2_HYGIENE_TRAINING_DOC = basedir + '/static/images/level_2_hygiene_training_doc/'
COVID_19_SAFETY_TRAINING_DOC = basedir + '/static/images/covid_19_safety_training_doc/'
HEALTH_SAFETY_TRAINING_DOC = basedir + '/static/images/health_safety_training_doc/'
FIRST_AID_TRAINING_DOC = basedir + '/static/images/first_aid_training_doc/'
FIRE_EXTINGUISHER_ESSENTIALS_TRAINING_DOC = basedir + '/static/images/fire_extinguisher_essentials_training_doc/'
SUSTAINABILITY_TRAINING_DOC = basedir + '/static/images/sustainability_training_doc/'
HACCP_TRAINING_DOC = basedir + '/static/images/haccp_training_doc/'
LPG_GAS_SAFETY_DOC = basedir + '/static/images/lpg_gas_safety_doc/'
COPY_OF_PASSPORT_DOC = basedir + '/static/images/copy_of_passport_doc/'
PROOF_OF_INSU_DOC = basedir + '/static/images/proof_of_insurance_doc/'
SIGNATURE = basedir + '/static/images/signature_doc/'


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov', 'jfif', 'docx'])




def street_apply_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session.get('last_id'):
            return f(*args, **kwargs)
        else:
            return redirect(url_for('front.landing'))

    return wrap

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
front = Blueprint('front', __name__)
# udash = Blueprint('udash', __name__, url_prefix='/udash')



@front.route('/')
@front.route("/landing")
def landing():
    session.clear()
    # if session.get('counter'):
        # session.pop('counter')
    return render_template('streetcube/land.jinja2')


@front.route("/apply/<string:cano_url>",methods=['POST','GET'])
def apply(cano_url):
    apply_for = cano_url
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            session['email'] = email
            session['apply_for'] = apply_for
        return redirect(url_for('front.check_fl_field')) 
    return render_template('streetcube/partners.jinja2', title="Sign Up")


@front.route("/check/fname/lname",methods=['POST','GET'])
def check_fl_field():

    try:
        if session.get('email') and session.get('apply_for'):
            if request.method == 'POST':
                uname = request.form.get('uname')
                lname = request.form.get('lname')
                session['uname'] = uname
                session['lname'] = lname
                
                return redirect(url_for('front.check_mobile'))  
            return render_template('streetcube/formfnln.jinja2')
    except Exception as e:
        return str(e)  


@front.route('/check/mobile',methods=['GET','POST']) 
def check_mobile():
    try:
        if session.get('email') and session.get('uname') and session.get('lname') and session.get('apply_for'):
            if request.method == 'POST':
                mobile = request.form.get('mobile')
                session['mobile'] = mobile

                password_characters = string.digits
                otp = ''.join(random.choice(password_characters) for i in range(4))
                session['otp'] = otp
                # sms = "Your%20StreetCube%20mobile%20verification%204-digit%20pin:%20" + str(otp)
                sms = "Your StreetCube mobile verification 4-digit pin: " + str(otp)
                # gen_otp(sms, "%2b44" + mobile)
                send_sms("+91"+mobile,sms)

                return redirect(url_for('front.verify_otp_msg'))

            return render_template('streetcube/formphone.jinja2')
                
    except Exception as e:
        return str(e)




@front.route('/front/login', methods=['GET', 'POST'])
def front_login():
    return redirect(url_for('main.login'))
    # if request.method == 'POST':
    #         user = UserInfo.query.filter_by(email=request.form.get('email'), user_role=3).first()

    #         if user:
    #             if check_password_hash(user.password, request.form.get('password')):
    #                 login_user(user)
    #                 setattr(user, 'no_of_logins', UserInfo.no_of_logins + 1)
    #                 # user.register_date(now)
    #                 db.session.commit()
    #                 db.session.flush()

    #                 if user.user_role == 3:
    #                     # return jsonify({'error':'0','msg':'Login successfully!'})
    #                     return redirect(url_for('main.dashboard'))
    #                 else:
    #                     return jsonify({'error':'0','msg':'You are not admin '})

    #             return jsonify({'error':'1','msg':'Invalid Credentials. Please try again!'})
    #         else:
    #             return jsonify({'error':'1','msg':'Email and Password is wrong'})

    # return jsonify({'error':'1','msg':'method not allowed'})


@front.route('/otp-msg', methods=['GET', 'POST'])
def verify_otp_msg():
    try:
        counter=0
        if session.get('uname') and session.get('email') and session.get('mobile') and session.get('apply_for') and session.get('lname'):
             if 'counter' not in session:
                session['counter'] = 0
             if request.method == 'POST':
                
                if session.get('otp') != request.form.get('otp'):
                    # return "<script> alert('4 attempts - then, ‘Sorry, you have not entered the correct PIN, you will need to restart') ; window.location.href = '/otp-msg' </script>"
                    session['counter'] = session.get('counter') + 1
                    # return str(session['counter'])
                    if session.get('counter') == 3:
                        session.pop('counter', None)
                        return "<script> alert('4 attempts - then, ‘Sorry, you have not entered the correct PIN, you will need to restart') ; window.location.href = '/landing' </script>"
                        # return redirect(url_for('front.landing'))
                    else:
                        return "<script> alert('sorry, you appear to have entered the wrong PIN.. Please try again..') ; window.location.href = '/otp-msg' </script>"

                if session.get('otp') == request.form.get('otp'):
                    '''
                    email = session['email']
                    uname = session['uname']
                    lname = session['lname']
                    # password = session['password']
                    mobile = session['mobile'].lstrip("0")
                    cust_url = session.get('apply_for')

                    # is_show_mobile = bool(session['is_show_mobile'])
                    # is_mobile_verified = session['is_mobile_verified']

                    new_user = UserInfo(last_name=lname,uname=uname, email=email, password=0, mobile=mobile, user_role=3, is_show_mobile=1,
                                        is_mobile_verified=1, no_of_logins=0,address=0,cano_url=cust_url
                                        )
                    db.session.add(new_user)
                    db.session.commit()

              
                    flash("Registration was successful", "success")
                    '''
                    return redirect(url_for('front.creat_pass'))
                # flash("Please fill mobile no first")
                # msg = "<script> alert('Please enter valid 4-Digit PIN'); </script>"
                    
                  
        return render_template('streetcube/vrotp.jinja2')

    except Exception as e:
        return str(e)




@front.route('/verified-msg', methods=['GET', 'POST'])
def verified_msg():
    return render_template('verified-msg.jinja2')



@front.route('/create/pass', methods=['GET', 'POST'])
def creat_pass():
    if request.method == 'POST':
        if session.get('uname') and session.get('email') and session.get('mobile') and session.get('apply_for') and session.get('lname') and session.get('otp'):
            email = session['email']
            uname = session['uname']
            lname = session['lname']
            # password = session['password']
            mobile = session['mobile'].lstrip("0")
            otp = session['otp']
            # return str(otp)
            cust_url = session.get('apply_for')
            hashed_password = generate_password_hash(request.form.get('pass'))
            # return str(hashed_password)
            password = hashed_password
            new_user = UserInfo(last_name=lname,uname=uname, email=email, password=password, mobile=mobile, user_role=3, is_show_mobile=1,
                                is_mobile_verified=1, no_of_logins=0,address=0,cano_url=cust_url
                                )
            db.session.add(new_user)
            db.session.commit()
            session['last_id'] = new_user.id
            # flash('Your password is successfully created...','success')
            return redirect(url_for('front.vr_usr'))
        else:
            flash('Oops somthing went wrong...','danger')
     
    return render_template('streetcube/passauth.jinja2')



@front.route('/vr/usr', methods=['GET', 'POST'])
def vr_usr():
    return render_template('streetcube/vrusr.jinja2')


@front.route('/gazebo/app/frm', methods=['GET', 'POST'])
def gazebo_app_frm():
    if request.method == 'POST':
        name_prfx = request.form.get('name_prfx')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        dob = request.form.get('dob')
        ide = session.get('last_id')
     
        ga_prt_one_up = UserInfo.query.filter_by(id= ide).first()
        if ga_prt_one_up:
            ga_prt_one_up.name_prfx = name_prfx
            ga_prt_one_up.uname = fname
            ga_prt_one_up.last_name = lname
            ga_prt_one_up.dob = dob
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_sec'))
            # flash('Part 1 is  successfully saved...','success')
        # else:
            # flash('Oops somthing went wrong...','danger')
    return render_template('streetcube/gazeboappfrm.jinja2')


@front.route('/gazebo/app/frm/sec', methods=['GET', 'POST'])
def gazebo_app_frm_sec():
    if request.method == 'POST':
        email  = request.form.get('email')
        hphone = request.form.get('hphone')
        mobile = request.form.get('telphone')
        zipcode = request.form.get('postcode')
        address = request.form.get('street')
        town = request.form.get('town')
        city = request.form.get('city')

        ga_prt_two_up = UserInfo.query.filter_by(id= session.get('last_id')).first()
        if ga_prt_two_up:
            ga_prt_two_up.email = email
            ga_prt_two_up.home_phone = hphone
            ga_prt_two_up.mobile = mobile
            ga_prt_two_up.zipcode = zipcode
            ga_prt_two_up.address = address
            ga_prt_two_up.town = town
            ga_prt_two_up.city = city
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_thr'))
            # flash('Part 2 is  successfully saved...','success')
        # else:
        #    flash('Oops somthing went wrong...','danger')
    return render_template('streetcube/gazeboappfrmsec.jinja2')



@front.route('/gazebo/app/frm/thr', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_thr():
    ga_prt_thr_up = Gazebo_process_3rd.query.filter_by(member_id = session.get('last_id')).first()
    if request.method == 'POST':
        nationality = request.form.get('nationality')
        passport_no = request.form.get('passport_no')
        national_insurance_no = request.form.get('national_insurance_no')
        known_medical_conditions = request.form.get('known_medical_conditions')
        next_of_kin_name = request.form.get('next_of_kin_name')
        next_of_kin_contact = request.form.get('next_of_kin_contact')
        
        ga_prt_thr_up = Gazebo_process_3rd.query.filter_by(member_id = session.get('last_id')).first()
        if not ga_prt_thr_up:
            member_id = session.get('last_id')
            db.session.add(Gazebo_process_3rd(member_id = member_id,nationality=nationality,passport_no=passport_no,national_insurance_no=national_insurance_no,known_medical_conditions=known_medical_conditions,next_of_kin_name=next_of_kin_name,next_of_kin_contact=next_of_kin_contact))
            db.session.commit()
            db.session.close()
            # flash('Part 3 is  successfully saved...','success')
            return redirect(url_for('front.gazebo_app_frm_frth'))
        else:
            ga_prt_thr_up.nationality = nationality
            ga_prt_thr_up.passport_no = passport_no
            ga_prt_thr_up.national_insurance_no = national_insurance_no
            ga_prt_thr_up.known_medical_conditions = known_medical_conditions
            ga_prt_thr_up.next_of_kin_name = next_of_kin_name
            ga_prt_thr_up.next_of_kin_contact = next_of_kin_contact
            db.session.commit()
            db.session.close()
            # flash('Oops somthing went wrong...','danger')
            return redirect(url_for('front.gazebo_app_frm_frth'))

    return render_template('streetcube/gazeboappfrmthr.jinja2',ga_prt_thr_up = ga_prt_thr_up)



@front.route('/gazebo/app/frm/frth', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_frth():
    ga_prt_frth_up = Gazebo_process_4th.query.filter_by(member_id = session.get('last_id')).first()
    food_style_list = Food_style_details.query.all()
    if request.method == 'POST':
        food_style = request.form.get('food_style')
        describe_food_style = request.form.get('describe_food_style')
        suplier_list = request.form.getlist('suplier_list')
        
        if not ga_prt_frth_up:
            member_id = session.get('last_id')
            db.session.add(Gazebo_process_4th(member_id=member_id,food_style=food_style,describe_food_style=describe_food_style,suplier_list= ','.join(suplier_list)))
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.sample_check_data'))
            # flash('Part 4 is  successfully saved...','success')
        else:
            ga_prt_frth_up.food_style = food_style
            ga_prt_frth_up.describe_food_style = describe_food_style
            ga_prt_frth_up.suplier_list = ','.join(suplier_list)
            db.session.commit()
            db.session.close()
            # flash('Oops somthing went wrong...','danger')
            return redirect(url_for('front.gazebo_app_frm_fifth'))
    else:
        return render_template('streetcube/gazeboappfrmfrth.jinja2',ga_prt_frth_up = ga_prt_frth_up,food_style_list = food_style_list)
    




@front.route('/gazebo/app/frm/fifth', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_fifth():
    ga_prt_5th_up = Gazebo_process_5th.query.filter_by(member_id = session.get('last_id')).first()
    if request.method == 'POST':
        is_new_project = request.form.get('is_new_project')
        menu_type = request.form.get('menu_type')
        business_operate = request.form.get('business_operate')
        operate_yrs = request.form.get('operate_yrs')
        street_loc = request.form.get('street_loc')
        pop_sel_item = request.form.get('pop_sel_item')
        avg_spent_client = request.form.get('avg_spent_client')
        staff_need = request.form.get('staff_need')
        day_hour_operate = request.form.get('day_hour_operate')
        is_formal_cat_quali = request.form.get('is_formal_cat_quali')

        ga_prt_5th_up = Gazebo_process_5th.query.filter_by(member_id = session.get('last_id')).first()
        if not ga_prt_5th_up:
            member_id = session.get('last_id')
            db.session.add(Gazebo_process_5th(member_id=member_id,is_new_project=bool(is_new_project),menu_type=menu_type,business_operate=business_operate,operate_yrs=operate_yrs,street_loc=street_loc,pop_sel_item=pop_sel_item,avg_spent_client=avg_spent_client,staff_need=staff_need,day_hour_operate=day_hour_operate,is_formal_cat_quali=bool(is_formal_cat_quali)))
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_sixth'))
            # flash('Part 5 is  successfully saved...','success')
        else:
            ga_prt_5th_up.is_new_project = bool(is_new_project)
            ga_prt_5th_up.menu_type = menu_type
            ga_prt_5th_up.business_operate = business_operate
            ga_prt_5th_up.operate_yrs = operate_yrs
            ga_prt_5th_up.street_loc = street_loc
            ga_prt_5th_up.pop_sel_item = pop_sel_item
            ga_prt_5th_up.avg_spent_client = avg_spent_client
            ga_prt_5th_up.staff_need = staff_need
            ga_prt_5th_up.day_hour_operate = day_hour_operate
            ga_prt_5th_up.is_formal_cat_quali = bool(is_formal_cat_quali)
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_sixth'))
            # flash('Oops somthing went wrong...','danger')
    return render_template('streetcube/gazeboappfrmfivth.jinja2',ga_prt_5th_up=ga_prt_5th_up)
    


@front.route('/gazebo/app/frm/sixth', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_sixth():
    ga_prt_6th_up = Gazebo_process_6th.query.filter_by(member_id = session.get('last_id')).first()
    if request.method == 'POST':
        proof_of_ncass_doc = request.files['proof_of_ncass_doc']
        cv_doc = request.files['cv_doc']
        level_2_hygiene_doc = request.files['level_2_hygiene_doc']
        covid_19_safety_doc = request.files['covid_19_safety_doc']
        health_safety_doc = request.files['health_safety_doc']
        first_aid_doc = request.files['first_aid_doc']
        fire_extinguisher_doc = request.files['fire_extinguisher_doc']

        try:
            ga_prt_6th_up = Gazebo_process_6th.query.filter_by(member_id = session.get('last_id')).first()
            if not ga_prt_6th_up:
                req_proof_of_ncass_doc = ''
                req_cv_doc = ''
                req_level_2_hygiene_doc = ''
                req_covid_19_safety_doc = ''
                req_health_safety_doc = ''
                req_first_aid_doc = ''
                req_fire_extinguisher_doc = ''
                if proof_of_ncass_doc and allowed_file(proof_of_ncass_doc.filename):
                    filename = secure_filename(proof_of_ncass_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    proof_of_ncass_doc.save(os.path.join(PROOF_OF_NCASS_TRAINING_OR_EQUIVALENT_DOC, renamefile))
                    req_proof_of_ncass_doc = renamefile


                if cv_doc and allowed_file(cv_doc.filename):
                    filename = secure_filename(cv_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    cv_doc.save(os.path.join(CV_DOC,renamefile))
                    req_cv_doc = renamefile



                if level_2_hygiene_doc and allowed_file(level_2_hygiene_doc.filename):
                    filename = secure_filename(level_2_hygiene_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    level_2_hygiene_doc.save(os.path.join(LEVEL_2_HYGIENE_TRAINING_DOC, renamefile))
                    req_level_2_hygiene_doc = renamefile


                if covid_19_safety_doc and allowed_file(covid_19_safety_doc.filename):
                    filename = secure_filename(covid_19_safety_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    covid_19_safety_doc.save(os.path.join(COVID_19_SAFETY_TRAINING_DOC, renamefile))
                    req_covid_19_safety_doc = renamefile


                if health_safety_doc and allowed_file(health_safety_doc.filename):
                    filename = secure_filename(health_safety_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    health_safety_doc.save(os.path.join(HEALTH_SAFETY_TRAINING_DOC, renamefile))
                    req_health_safety_doc = renamefile


                if first_aid_doc and allowed_file(first_aid_doc.filename):
                    filename = secure_filename(first_aid_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    first_aid_doc.save(os.path.join(FIRST_AID_TRAINING_DOC , renamefile))
                    req_first_aid_doc = renamefile


                if fire_extinguisher_doc and allowed_file(fire_extinguisher_doc.filename):
                    filename = secure_filename(fire_extinguisher_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    fire_extinguisher_doc.save(os.path.join(FIRE_EXTINGUISHER_ESSENTIALS_TRAINING_DOC ,renamefile))
                    req_fire_extinguisher_doc = renamefile

                member_id = session.get('last_id')
                db.session.add(Gazebo_process_6th(member_id=member_id,proof_of_ncass_doc=req_proof_of_ncass_doc,cv_doc=req_cv_doc,level_2_hygiene_doc=req_level_2_hygiene_doc,covid_19_safety_doc=req_covid_19_safety_doc,health_safety_doc=req_health_safety_doc,first_aid_doc=req_first_aid_doc,fire_extinguisher_doc=req_fire_extinguisher_doc))

                db.session.commit()
                db.session.close()
                return redirect(url_for('front.gazebo_app_frm_sevth'))
                # flash('Part 6 is  successfully saved...','success')
            # else:
                # flash('Oops somthing went wrong...','danger')
        except Exception as e:
            app.logger.error(str(e))
            return abort(500)    
    else:
        return render_template('streetcube/gazeboappfrmsixth.jinja2',ga_prt_6th_up=ga_prt_6th_up)


@front.route('/gazebo/app/frm/sevth', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_sevth():
    if request.method == 'POST':
        sustain_training_doc =  request.files['sustain_training_doc']
        haccp_training_doc  =  request.files['haccp_training_doc']
        lpg_gas_safe_doc  =  request.files['lpg_gas_safe_doc']
        copy_of_pass_doc  =  request.files['copy_of_pass_doc']
        proof_of_insu_doc  =  request.files['proof_of_insu_doc']
        about_exp   =  request.form.get('about_exp')
        try:
            ga_prt_7th_up = Gazebo_process_7th.query.filter_by(member_id = session.get('last_id')).first()
            req_sustain_training_doc = ''
            req_haccp_training_doc = ''
            req_lpg_gas_safe_doc = ''
            req_copy_of_pass_doc = ''
            req_proof_of_insu_doc = ''
            if not ga_prt_7th_up:
                if sustain_training_doc and allowed_file(sustain_training_doc.filename):
                    filename = secure_filename(sustain_training_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    sustain_training_doc.save(os.path.join(SUSTAINABILITY_TRAINING_DOC, renamefile))
                    req_sustain_training_doc = renamefile

                if haccp_training_doc and allowed_file(haccp_training_doc.filename):
                    filename = secure_filename(haccp_training_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    haccp_training_doc.save(os.path.join(HACCP_TRAINING_DOC, renamefile))
                    req_haccp_training_doc = renamefile

                if lpg_gas_safe_doc and allowed_file(lpg_gas_safe_doc.filename):
                    filename = secure_filename(lpg_gas_safe_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    lpg_gas_safe_doc.save(os.path.join(LPG_GAS_SAFETY_DOC, renamefile))
                    req_lpg_gas_safe_doc = renamefile

                if copy_of_pass_doc and allowed_file(copy_of_pass_doc.filename):
                    filename = secure_filename(copy_of_pass_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    copy_of_pass_doc.save(os.path.join(COPY_OF_PASSPORT_DOC, renamefile))
                    req_copy_of_pass_doc = renamefile
                    
                if proof_of_insu_doc and allowed_file(proof_of_insu_doc.filename):
                    filename = secure_filename(proof_of_insu_doc.filename)
                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    proof_of_insu_doc.save(os.path.join(PROOF_OF_INSU_DOC, renamefile))
                    req_proof_of_insu_doc = renamefile

                member_id = session.get('last_id')
                db.session.add(Gazebo_process_7th(member_id=member_id,sustain_training_doc=req_sustain_training_doc,haccp_training_doc=req_haccp_training_doc,about_exp=about_exp,lpg_gas_safe_doc=req_lpg_gas_safe_doc,copy_of_pass_doc=req_copy_of_pass_doc,proof_of_insu_doc=req_proof_of_insu_doc))
                db.session.commit()
                db.session.close()
                return redirect(url_for('front.gazebo_app_frm_eighth'))
            #     flash('Part 7 is  successfully saved...','success')
            # else:
            #     flash('Oops somthing went wrong...','danger')
        except Exception as e:
            app.logger.error(str(e))
            return abort(500)    
    else:
        return render_template('streetcube/gazeboappfrmseventh.jinja2')


@front.route('/gazebo/app/frm/eighth', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_eighth():
    ga_prt_8th_up = Gazebo_process_8th.query.filter_by(member_id = session.get('last_id')).first()
    if request.method == 'POST':
        company_brand_name = request.form.get('company_brand_name')
        reg_company_name = request.form.get('reg_company_name')
        reg_company_no = request.form.get('reg_company_no')
        reg_company_address = request.form.get('reg_company_address')
        reg_trading_name = request.form.get('reg_trading_name')
        name_of_your_operation = request.form.get('name_of_your_operation')
        retail_price = request.form.get('retail_price')
        kitchen_uses = request.form.get('kitchen_uses')
        serving_methods = request.form.get('serving_methods')
        other_kitchen_items = request.form.get('other_kitchen_items')
        all_the_equip_uses = request.form.get('all_the_equip_uses')
        drinks_serve = request.form.get('drinks_serve')
        cooking_method = request.form.get('cooking_method')

        # ga_prt_8th_up = UserInfo.query.filter_by(id = session.get('last_id')).first()
        ga_prt_8th_up = Gazebo_process_8th.query.filter_by(member_id = session.get('last_id')).first()
        if not ga_prt_8th_up:
            member_id = session.get('last_id')
            db.session.add(Gazebo_process_8th(member_id=member_id,company_brand_name=company_brand_name,reg_company_name=reg_company_name,reg_company_no=reg_company_no,reg_company_address=reg_company_address,reg_trading_name=reg_trading_name,name_of_your_operation=name_of_your_operation,retail_price=retail_price,kitchen_uses=kitchen_uses,serving_methods=serving_methods,other_kitchen_items=other_kitchen_items,all_the_equip_uses=all_the_equip_uses,drinks_serve=drinks_serve,cooking_method=cooking_method))
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_nineth'))
            # flash('Part 8 is  successfully saved...','success')
        else:
            ga_prt_8th_up.company_brand_name = company_brand_name
            ga_prt_8th_up.name_of_your_operation = name_of_your_operation
            ga_prt_8th_up.retail_price = retail_price
            ga_prt_8th_up.kitchen_uses = kitchen_uses
            ga_prt_8th_up.serving_methods =serving_methods
            ga_prt_8th_up.other_kitchen_items = other_kitchen_items
            ga_prt_8th_up.all_the_equip_uses = all_the_equip_uses
            ga_prt_8th_up.drinks_serve = drinks_serve
            ga_prt_8th_up.cooking_method = cooking_method
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_nineth'))
    return render_template('streetcube/gazeboappfrmeight.jinja2',ga_prt_8th_up=ga_prt_8th_up)


@front.route('/gazebo/app/frm/nineth', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_nineth():
    ga_prt_9th_up = Gazebo_process_9th.query.filter_by(member_id = session.get('last_id')).first()
    if request.method == 'POST':
        have_company_name = request.form.get('have_company_name')
        vat_reg = request.form.get('vat_reg') or ''
        delivery_agents = request.form.get('delivery_agents')
        about_your_business = request.form.get('about_your_business')
        length_of_trading = request.form.get('length_of_trading')
        desired_commence = request.form.get('desired_commence')

        # return str(session.get('last_id'))
        ga_prt_9th_up = Gazebo_process_9th.query.filter_by(member_id = session.get('last_id')).first()

        # return str(ga_prt_9th_up)
        if not ga_prt_9th_up:
            member_id = session.get('last_id')
            db.session.add(Gazebo_process_9th(member_id=member_id,have_company_name=have_company_name,vat_reg=vat_reg,delivery_agents=delivery_agents,about_your_business=about_your_business,length_of_trading=length_of_trading,desired_commence=desired_commence))
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_tenth'))
            # flash('Part 9 is  successfully saved...','success')
        else:
            ga_prt_9th_up.have_company_name = have_company_name
            ga_prt_9th_up.vat_reg = vat_reg
            ga_prt_9th_up.delivery_agents = delivery_agents
            ga_prt_9th_up.about_your_business = about_your_business
            ga_prt_9th_up.length_of_trading = length_of_trading
            ga_prt_9th_up.desired_commence = desired_commence
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_tenth'))
           
    return render_template('streetcube/gazeboappfrmnineth.jinja2',ga_prt_9th_up=ga_prt_9th_up)



@front.route('/gazebo/app/frm/tenth', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_tenth():
    ga_prt_10th_up = Gazebo_process_10th.query.filter_by(member_id = session.get('last_id')).first()
    if request.method == 'POST':
        daily_rental = request.form.get('daily_rental')
        clients_need = request.form.get('clients_need')
        turnover = request.form.get('turnover')

        ga_prt_10th_up = Gazebo_process_10th.query.filter_by(member_id = session.get('last_id')).first()
        if not ga_prt_10th_up:
            member_id = session.get('last_id')
            db.session.add(Gazebo_process_10th(member_id=member_id,daily_rental=daily_rental,clients_need=clients_need,turnover=turnover))
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_eleventh'))
            # flash('Part 9 is  successfully saved...','success')
        else:
            ga_prt_10th_up.daily_rental = daily_rental
            ga_prt_10th_up.clients_need = clients_need
            ga_prt_10th_up.turnover = turnover
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_eleventh'))

    return render_template('streetcube/gazeboappfrmtenth.jinja2',ga_prt_10th_up=ga_prt_10th_up)


@front.route('/gazebo/app/frm/eleventh', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_eleventh():
    ga_prt_11th_up = Gazebo_process_11th.query.filter_by(member_id = session.get('last_id')).first()
    if request.method == 'POST':
        specific_location = request.form.get('specific_location')
        land_owner = request.form.get('land_owner')
        jurisdict_authority = request.form.get('jurisdict_authority')
        is_storage_req = bool(request.form.get('is_storage_req'))
        ga_prt_11th_up = Gazebo_process_11th.query.filter_by(member_id = session.get('last_id')).first()
        if not ga_prt_11th_up:
            member_id = session.get('last_id')
            db.session.add(Gazebo_process_11th(member_id=member_id,specific_location=specific_location,land_owner=land_owner,jurisdict_authority=jurisdict_authority,is_storage_req=is_storage_req))
            db.session.commit()
            db.session.close()
            return redirect(url_for('front.gazebo_app_frm_twelfth'))
            # flash('Part 10 is  successfully saved...','success')
        else:
            ga_prt_11th_up.specific_location = specific_location
            ga_prt_11th_up.land_owner = land_owner
            ga_prt_11th_up.jurisdict_authority = jurisdict_authority
            ga_prt_11th_up.is_storage_req = is_storage_req
            return redirect(url_for('front.gazebo_app_frm_twelfth'))
    return render_template('streetcube/gazeboappfrmeleventh.jinja2',ga_prt_11th_up = ga_prt_11th_up)



@front.route('/gazebo/app/frm/twelfth', methods=['GET' ,'POST'])
@street_apply_required
def gazebo_app_frm_twelfth():
    msg = ''
    if request.method == 'POST':
        signature = request.files['signature']
        ga_prt_12th_up = Gazebo_process_12th.query.filter_by(member_id = session.get('last_id')).first()
        if not ga_prt_12th_up:
            try:
                if signature and allowed_file(signature.filename):
                    filename = secure_filename(signature.filename)
                    # signature.save(os.path.join(SIGNATURE,filename))

                    filetype, extension = splitext(filename)
                    renamefile = str(randomkey(25)).lower() + extension
                    signature.save(os.path.join(SIGNATURE, renamefile))

                    member_id = session.get('last_id')
                    db.session.add(Gazebo_process_12th(member_id=member_id,signature=renamefile))
                    db.session.commit()
                    db.session.close()
                    return redirect(url_for('main.dashboard'))
                    flash('You have successfully signed up!', 'success')
                # else:
                    # flash('Oops somthing went wrong...','danger')
            except Exception as e:
                return str(e)        
                # return redirect(url_for('front.gazebo_app_frm_twelfth'))   
        else:
            msg = "Oops somthing went wrong..."
    return render_template('streetcube/gazeboappfrmtwelfth.jinja2')


@front.route('/sample/check/data',methods=['GET','POST'])
def sample_check_data():
	products = ProductList.query.all()
	sample_check_data = SampleCheckData.query.filter_by(member_id = session.get('last_id')).all()
	if request.method == 'POST':
		choose_product = request.form.getlist('choose_product')

		ch_arr = []
		organic_produce = request.form.getlist('organic_produce')
		# return str(organic_produce)
		seasonal_produce = request.form.getlist('seasonal_produce')
		locally_grown = request.form.getlist('locally_grown')
		zero_plastic = request.form.getlist('zero_plastic')
		zero_waste_to_landfill = request.form.getlist('zero_waste_to_landfill')
		vegetable_meat_ratio = request.form.getlist('vegetable_meat_ratio')
		nutritional_content = request.form.getlist('nutritional_content')
		non_sugar_drinks = request.form.getlist('non_sugar_drinks')
		allergy_rating = request.form.getlist('allergy_rating')
		non_diary_drinks = request.form.getlist('non_diary_drinks')
		total_sus_score = request.form.getlist('total_sus_score')

		for i in range(len(choose_product)):
			add_sample_check_data = SampleCheckData(
										member_id= session.get('last_id'),choose_product=choose_product[i],
										organic_produce=organic_produce[i].replace(" ",""),seasonal_produce=seasonal_produce[i].replace(" ",""),
										locally_grown = locally_grown[i].replace(" ",""), zero_plastic = zero_plastic[i].replace(" ",""),
										zero_waste_to_landfill = zero_waste_to_landfill[i].replace(" ",""),vegetable_meat_ratio=vegetable_meat_ratio[i].replace(" ",""),
										nutritional_content=nutritional_content[i].replace(" ",""),
										non_sugar_drinks=non_sugar_drinks[i].replace(" ",""),allergy_rating=allergy_rating[i].replace(" ",""),
										non_diary_drinks=non_diary_drinks[i].replace(" ",""),
										total_sus_score=total_sus_score[i].replace(" ","")

									)
			
			db.session.add(add_sample_check_data)
			db.session.commit()


		# db.session.close()
		return redirect(url_for('front.gazebo_app_frm_fifth'))

	return render_template('streetcube/samplecheck.html',sample_check_data=sample_check_data,prod_list=products)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return str(o)
        if isinstance(o, date):
            return str(o)
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, time.struct_time):
            return datetime.fromtimestamp(time.mktime(o))
        # Any other serializer if needed
        return super(CustomJSONEncoder, self).default(o)



@front.route('/qlty-update', methods=['GET', 'POST'])
def qlty_update():
    if request.method == 'POST':
        qlty_id = request.form.get('qlty_id')
        organic_produce = request.form.get('organic_produce')
        seasonal_produce = request.form.get('seasonal_produce')
        locally_grown = request.form.get('locally_grown')
        zero_plastic = request.form.get('zero_plastic')
        zero_waste_to_landfill = request.form.get('zero_waste_to_landfill')
        vegetable_meat_ratio = request.form.get('vegetable_meat_ratio')
        nutritional_content = request.form.get('nutritional_content')
        non_sugar_drinks = request.form.get('non_sugar_drinks')
        allergy_rating = request.form.get('allergy_rating')
        non_diary_drinks = request.form.get('non_diary_drinks')
        total_sus_score = request.form.get('total_sus_score')
        exist_qlty = SampleCheckData.query.filter_by(id= qlty_id).first()
        if exist_qlty:
            exist_qlty.organic_produce = organic_produce
            exist_qlty.seasonal_produce = seasonal_produce
            exist_qlty.locally_grown = locally_grown
            exist_qlty.zero_plastic = zero_plastic
            exist_qlty.zero_waste_to_landfill = zero_waste_to_landfill
            exist_qlty.vegetable_meat_ratio = vegetable_meat_ratio
            exist_qlty.nutritional_content = nutritional_content
            exist_qlty.non_sugar_drinks = non_sugar_drinks
            exist_qlty.allergy_rating  = allergy_rating
            exist_qlty.non_diary_drinks = non_diary_drinks
            exist_qlty.total_sus_score = total_sus_score
            db.session.commit()
            db.session.close()
            return str('updated...')
@front.route('/qlty-delete/<int:id>',methods=['GET','POST'])
def qlty_delete(id):
    obj = SampleCheckData.query.filter_by(id=id).one()
    db.session.delete(obj)
    db.session.commit()
    return redirect(url_for('front.sample_check_data'))

@front.route('/qlty-show', methods=['GET', 'POST'])
def qlty_show():   
    if request.method == 'POST': 
        qlty_id = request.form.get('qlty_id')
        shows_qlty = SampleCheckData.query.filter_by(id = qlty_id).first()
        if shows_qlty:
            return jsonify({'choose_product':shows_qlty.choose_product,
                'organic_produce':float(shows_qlty.organic_produce),
                'seasonal_produce':float(shows_qlty.seasonal_produce),
                'locally_grown':float(shows_qlty.locally_grown),
                'zero_plastic':float(shows_qlty.zero_plastic),
                'zero_waste_to_landfill':float(shows_qlty.zero_waste_to_landfill),
                'vegetable_meat_ratio':float(shows_qlty.vegetable_meat_ratio),
                'nutritional_content':float(shows_qlty.nutritional_content),
                'non_sugar_drinks':float(shows_qlty.non_sugar_drinks),
                'allergy_rating':float(shows_qlty.allergy_rating),
                'non_diary_drinks':float(shows_qlty.non_diary_drinks),
                'total_sus_score':float(shows_qlty.total_sus_score),
                'qlty_id':shows_qlty.id,

                })
        else:
            return False
        # return str(shows_qlty.choose_product)
        
     

@front.route("/resend/otp")
def resend_otp():
    password_characters = string.digits
    otp = ''.join(random.choice(password_characters) for i in range(4))
    session['otp'] = otp
    # sms = "Your%20StreetCube%20mobile%20verification%204-digit%20pin:%20" + str(otp)
    sms = "Your StreetCube mobile verification 4-digit pin: " + str(otp)
    mobile = session.get('mobile')
    # gen_otp(sms, "%2b44" + mobile)
    send_sms("+91"+mobile,sms)
    return redirect(url_for('front.verify_otp_msg'))



@front.route('/check-reg-user-id', methods=['POST'])
def validate_reg_user_id():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        email_avali = UserInfo.query.filter_by(email=email).first()
        if email_avali:
            return 'false'
        else:
            return 'true'








   
