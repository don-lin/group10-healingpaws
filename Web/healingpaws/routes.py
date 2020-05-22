from healingpaws import  app,qrcode,DatabaseSecretConfig
from healingpaws.dbConnector import *
from flask import render_template,send_from_directory,send_file,request,session,redirect
from healingpaws.nn import get_type
import os,random

error_info=None
success_info=None

app.add_template_global(getAllUser,'get_all_user')
app.add_template_global(getUserFromId,'get_user')
app.add_template_global(getPet,'get_pet')
app.add_template_global(getChat,'getChat')
#aaadsdssdssdsdsds
def gun():
    return session.get('username')

app.add_template_global(gun,'gun')

def flash_error():
    global error_info
    r=error_info
    error_info=None
    return r

def flash_success():
    global success_info
    r=success_info
    success_info=None
    return r

app.add_template_global(flash_success,'flash_success')
app.add_template_global(flash_error,'flash_error')

def getkind(petid):
    path=DatabaseSecretConfig.userimgdir+"/pet_icon_"+str(petid)+'.jpg'
    if not(os.path.exists(path)):
        return 'unknown'
    return get_type(path)

app.add_template_global(getkind,'getkind')

def L(html):
    if session.get('language')==1:
        return 'cn/'+html
    return html

def save_file(path,file,name):
    if not file:
        return
    print('saving the files: ',name)
    file_path = os.path.join(path,name)
    file.save(file_path)
    
    
    
def delete_file(path,name):
    print('deleting the files: ',name)
    try:
        file_path = os.path.join(path,name)
        os.remove(file_path)
    except:
        pass
    
def rand():
    return random.random()

def err_login():
    global error_info
    error_info='Please Log In First'
    return redirect('/introduction')

@app.errorhandler(404)
def page_not_found(e):
    return "<a href='/'>Page Not Found</a>",404

@app.route("/")
@app.route('/home')
@app.route("/introduction")
def homepage():
    print(request.url)
    
    return render_template(L('homepage/index.html'))

@app.route('/guestlogin',methods=["GET","POST"])
def guestlogin():
    session['username']='None'
    return redirect("/introduction")

@app.route('/login',methods=["GET","POST"])
def login():
    if(request.method=="POST"):
        global error_info
        if checkUserPassword(request.form.get('username'),request.form.get('password')):
            session['username']=request.form.get("username")
        else:
            error_info='password wrong'
        if not checkUserExist(request.form.get('username')):
            error_info='username not exist'
    return redirect("/introduction")

@app.route('/reset',methods=["GET","POST"])
def reset_password():
    if(request.method=="POST"):
        print(request.form)
        success_message('password has been reset')
        updateUserPassword(request.form.get('username'),request.form.get('password'))
    return redirect("/introduction")

@app.route('/check_type',methods=["GET","POST"])
def send_type():
    if request.method=='POST':
        save_file(DatabaseSecretConfig.userimgdir,request.files.get('image'),'type.jpg')
        save_file(DatabaseSecretConfig.basedir,request.files.get('image'),'type.jpg')
    type= get_type(DatabaseSecretConfig.userimgdir+"/"+'type.jpg')
    return render_template(L('pettype.html'),pettype=type,rand=rand())
@app.route('/logout',methods=["GET","POST"])
def logout():
    success_message(session.get('username')+' log out success')
    session.pop('username')
    return 'log out success'


@app.route('/cl',methods=["GET","POST"])
def change_language():
    if session.get('language')==1:
        session['language']=0
    else:
        session['language']=1
    success_message('change language success, current language is '+['english','chinese'][session.get('language')])
    return 'change language success'

def count_pet_appointment(petid):
    return len(getPetAppointment(petid))
app.add_template_global(count_pet_appointment,'count_pet_appointment')

def count_doc_appointment(docid):
    return len(getDoctorAppointment(docid))
app.add_template_global(count_doc_appointment,'count_doc_appointment')

def deal_appointment_request(form):
    print(form)
    if(form.get("submit")=='add'):
        if not form.get('pet_id'):
            global error_info
            error_info='you must select a pet'
            return;
        addAppointment(form.get('pet_id'),form.get('doctor_id'),form.get('date'),form.get('emergency_level'),form.get('hospital'),form.get('status'))
    if(form.get("delete_appointment")):
        deleteAppointment(form.get("delete_appointment"))
    if(form.get("update_appointment")):
        updateAppointment(form.get("update_appointment"),form.get('pet_id'),form.get('doctor_id'),form.get('date'),form.get('emergency_level'),form.get('hospital'),form.get('status'))

@app.route('/appointment/date/<date>',methods=['GET','POST'])
def appointment_date_page(date):
    if not session.get('username'):
        return err_login()
    deal_appointment_request(request.form)

    return render_template(L('appointments.html'),
    apppointments=getDateAppointment(date),pets=getUserPets(session.get('username')),allpets=getAllPets(),
    user=getUser(session.get("username")),doctors=getAllDoctor(),rand=rand())

@app.route('/appointment/pet/<petid>',methods=['GET','POST'])
def appointment_pet_page(petid):
    if not session.get('username'):
        return err_login()
    deal_appointment_request(request.form)

    return render_template(L('appointments.html'),
    apppointments=getPetAppointment(petid),pets=getUserPets(session.get('username')),allpets=getAllPets(),
    user=getUser(session.get("username")),doctors=getAllDoctor(),rand=rand())

@app.route('/appointment/pure/doc/<docname>',methods=['GET','POST'])
def appointment_pure_doctor_page(docname):

    return render_template(L('doc-appointment.html'),
    apppointments=getDoctorAppointment(getUser(docname).id),doctors=getAllDoctor(),rand=rand())

@app.route('/appointment/pure/date/<date>',methods=['GET','POST'])
def appointment_pure_date_page(date):

    return render_template(L('doc-appointment.html'),
    apppointments=getDateAppointment(date),doctors=getAllDoctor(),rand=rand())

@app.route('/appointment/pure/hospital/<hos>',methods=['GET','POST'])
def appointment_pure_hospital_page(hos):

    return render_template(L('doc-appointment.html'),
    apppointments=getHospitalAppointment(hos),doctors=getAllDoctor(),rand=rand())

@app.route('/appointment/doctor/<docid>',methods=['GET','POST'])
def appointment_doctor_page(docid):
    if not session.get('username'):
        return err_login()
    deal_appointment_request(request.form)

    return render_template(L('appointments.html'),
    apppointments=getDoctorAppointment(docid),pets=getUserPets(session.get('username')),allpets=getAllPets(),
    user=getUser(session.get("username")),doctors=getAllDoctor(),rand=rand())

@app.route('/appointment',methods=['GET','POST'])
def appointment_page():

    if not session.get('username'):
        return err_login()
    deal_appointment_request(request.form)

    return render_template(L('appointments.html'),
    apppointments=getUserAppointment(session.get('username')),pets=getUserPets(session.get('username')),allpets=getAllPets(),
    user=getUser(session.get("username")),doctors=getAllDoctor(),rand=rand())

def success_message(success_hint):
    global success_info
    success_info=success_hint

@app.route("/changea",methods=["GET","POST"])
def upgrade_account():
    if(request.method=="POST"):
        nt=int(request.form.get('newtype'))
        success_message('your new account type is '+['user','doctor','employee'][nt])
        updateUserAccount(request.form.get('username'),nt)
    return redirect("/introduction")

@app.route("/info/<username>",methods=["GET","POST"])
def user_info(username):
    return render_template(L("info.html"),user=getUser(username))

@app.route("/profile",methods=["GET","POST"])
def profile_page():
    if not session.get('username'):
        return err_login()

    if request.method=='POST':
        print(request.form)
        uname=session.get('username')
        print(uname)
        save_file(DatabaseSecretConfig.userimgdir,request.files.get('icon'),uname+'.jpg')
        updateUserBirthday(uname,request.form.get('date'))
        updateUserEmail(uname,request.form.get('mail'))
        updateUserGender(uname,request.form.get('gender')=='male')
        print(request.form.get('gender'))
        
    username=session.get('username')
    return render_template(L("profile.html"),rand=rand(),user=getUser(username),appointments=getUserAppointment(username),pets=getUserPets(username),username=username)
@app.route("/pets",methods=["GET","POST"])
def pets_page():
    if not session.get('username'):
        return err_login()

    if(request.form.get("submit")=='add'):
        p=addPet(request.form.get('pet_name'),session.get('username'),int(request.form.get('pet_health')),request.form.get('pet_birthday'))
        print(request.files.get('pet_icon'))    
        save_file(DatabaseSecretConfig.userimgdir,request.files.get('pet_icon'),"pet_icon_"+str(p.id)+'.jpg')
    if(request.form.get("delete_pet")):
        deletePet(request.form.get("delete_pet"))
        delete_file(DatabaseSecretConfig.userimgdir,"pet_icon_"+request.form.get("delete_pet")+'.jpg')
    if(request.form.get("update_pet")):
        updatePet(request.form.get("update_pet"),request.form.get('pet_name'),int(request.form.get('pet_health')),request.form.get('pet_birthday'))
        save_file(DatabaseSecretConfig.userimgdir,request.files.get('pet_icon'),"pet_icon_"+request.form.get("update_pet")+'.jpg')

    return render_template(L("pets.html"),pets=getUserPets(session.get('username')),rand=rand())

#@app.route("/introduction")
def introduction_page():
    return render_template(L("introduction.html"))

    
@app.route("/doctors")
def doctors_page():
    return render_template(L("doctors.html"),users=getAllDoctor(),rand=rand())
@app.route("/users")
def users_page():
    return render_template(L("users.html"),users=getAllUser(),rand=rand())

@app.route("/register",methods=["GET","POST"])
def register():
    if(request.method=="POST"):
        username=request.form.get('username')
        password=request.form.get('password')
        if(checkUserExist(request.form.get('username'))):
            print('exist')
            global error_info
            error_info='user name exist'
            return redirect("/introduction")
        addUser(username,password)
        success_message(username+" register success, the account already logged in")
        session['username']=request.form.get("username")
    return redirect("/introduction")

@app.route("/locations")
def location_page():
    return render_template(L("locations.html"))

@app.route("/getchat/<fromuser>/<touser>",methods=["GET","POST"])
def get_chat(fromuser,touser):
    chats=getChat(fromuser,touser)
    result=""
    for c in chats:
        result+=c.prepare_send("donlin_send_key")+"donlin_split_key"
    return result
    
@app.route("/chat1/<touser>")
def chat_page1(touser):
    return render_template(L("chat1.html"),chatto=touser)

def deal_chat(fromuser,touser,form):
    if(form.get("content")):
        if(form.get("updateid")):
            updateChat(int(form.get("updateid")),form.get("content"))
        else:
            chat(fromuser,touser,form.get("content"))
    if(form.get("delid")):
        deleteChat(int(form.get("delid")))

@app.route("/chat/<touser>",methods=["GET","POST"])
def chat_page(touser):
    if(request.method=="POST"):
        #print(request.form)
        fromuser=session.get('username')
        fromuser = 'None' if fromuser is None else fromuser
        deal_chat(fromuser,touser,request.form)
        return get_chat(fromuser,touser)
    return render_template(L("chat.html"),chatto=touser)

@app.route("/comment/<touser>",methods=["GET","POST"])
def comment_user(touser):
    if(request.method=="POST"):
        fromuser='commentor'
    deal_chat(fromuser,touser,request.form) 
    return redirect('/doctors')


@app.route("/manage")
def manager_page():
    return render_template(L("manager.html"),users=getAllUser())


@app.route("/android/doctors",methods=["GET","POST"])
def send_android_doctors():
    doc_list=getAllDoctor()
    result=""
    for d in doc_list:
        result+=d.formatCode("ccddll")+"dlcc"
    return result

@app.route("/android/pets",methods=["GET","POST"])
def send_android_pets():
    pet_list=getAllPets()
    result=""
    for p in pet_list:
        result+=p.formatCode("ccddll")+"dlcc"
    return result

@app.route("/cover")
def cover_route():
	return render_template(L("cover.html"))



@app.route("/admin",methods=["GET","POST"])
def pet_page():
    print(request.form)
    if(request.form.get("submit")=='1'):
        addPet(request.form['pet_name'],session.get('username'),int(request.form['pet_health']),request.form['pet_birthday'])
    if(request.form.get("submit")=='2'):
        addDoctor(request.form['doctor_name'],int(request.form['age']),request.form['doctor_telphone'],request.form['doctor_introduction'])
    if(request.form.get("delete_pet")):
        deletePet(request.form.get("delete_pet"))
    if(request.form.get("delete_doctor")):
        deleteDoctor(request.form.get("delete_doctor"))
    if(request.form.get("update_doctor")):
        updateDoctor(request.form.get("update_doctor"),request.form['doctor_name'],int(request.form['age']),request.form['doctor_telphone'],request.form['doctor_introduction'])
    if(request.form.get("update_pet")):
        updatePet(request.form.get("update_pet"),request.form['pet_name'],int(request.form['pet_health']),request.form['pet_birthday'])
    return render_template(L("admin.html"), pet_list=getAllPets(),doctor_list=getAllDoctor())


@app.route('/css/<filename>')
def get_css(filename):
    return send_from_directory(DatabaseSecretConfig.cssdir,filename)
@app.route('/homepage/<filename>')
def get_home(filename):
    return send_from_directory(DatabaseSecretConfig.homedir,filename)
@app.route('/fonts/<filename>')
def get_home_fonts(filename):
    return send_from_directory(DatabaseSecretConfig.homedir,filename)
@app.route('/img/<filename>')
def get_img(filename):
    return send_from_directory(DatabaseSecretConfig.imgdir,filename)
    
    
@app.route('/icon/<rand>/<filename>')
def get_rand_icon(rand,filename):
    if not(os.path.exists((DatabaseSecretConfig.userimgdir+"/"+filename))):
        return get_img('t2.png')
    return send_from_directory(DatabaseSecretConfig.userimgdir,filename)
@app.route('/icon/<filename>')
def get_icon(filename):
    return get_rand_icon(0,filename)

@app.route('/js/<filename>')
def get_js(filename):
    return send_from_directory(DatabaseSecretConfig.jsdir,filename)
    
@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")


