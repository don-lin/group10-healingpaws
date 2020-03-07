# from healingpaws import  app,DatabaseSecretConfig
# from healingpaws.dbConnector import *
# from flask import render_template,send_from_directory,request,session,redirect
# import os,random

# error_info=None

# def save_file(path,file,name):
#     if not file:
#         print("No file detected")
#         return
#     print('saving the files')
#     file_path = os.path.join(path,name)
#     print('FilePath:' + file_path)
#     file.save(file_path)

# def rand():
#     return random.random()

# def err_login():
#     global error_info
#     error_info='Please Log In First'
#     return redirect('/introduction')

# @app.errorhandler(404)
# def page_not_found(e):
#     return "<a href='/'>Page Not Found</a>",404


# @app.route('/login',methods=["GET","POST"])
# def login():
#     if(request.method=="POST"):
#         global error_info
#         if checkUserPassword(request.form.get('username'),request.form.get('password')):
#             session['username']=request.form.get("username")
#             if checkIfEmployee(request.form.get('username')):
#                 session['user_level'] = 'employee'
#                 return redirect('/employee_question')
#             else:
#                 session['user_level'] = 'customer'
#         else:
#             error_info='password wrong'
#         if not checkUserExist(request.form.get('username')):
#             error_info='username not exist'
#     return redirect("/introduction")

# @app.route('/reset',methods=["GET","POST"])
# def reset_password():
#     if(request.method=="POST"):
#         updateUserPassword(request.form.get('username'),request.form.get('password'))
#     return redirect("/introduction")

# @app.route('/logout',methods=["GET","POST"])
# def logout():
#     session.pop('username')
#     if session.get('user_level') is not None:
#         session.pop('user_level')
#     return 'log out success'


# @app.route('/appointment',methods=['GET','POST'])
# def appointment_page():
#     if not session.get('username'):
#         return err_login()

#     if(request.form.get("submit")=='add'):
#         addAppointment(request.form['pet_id'],request.form['doctor_id'],request.form['date'],request.form['emergency'],request.form['description'])
#     if(request.form.get("delete_appointment")):
#         deleteAppointment(request.form.get("delete_appointment"))
#     if(request.form.get("update_appointment")):
#         updateAppointment(request.form.get("update_appointment"),request.form['pet_id'],request.form['doctor_id'],request.form['date'])
#     user_in_db = getUser(session.get('username'))
#     doctors = getAllDoctors()
#     pets = getUserPets(user_in_db.username)
#     # 加入选择列表里
#     pets_list = [[p.id, p.petsname] for p in pets]
#     doctors_list = [[d.id, d.doctorname] for d in doctors]

#     appointments_in_db = getUserAppointment(session.get('username'))
#     appointment_list = []
#     for a in appointments_in_db:
#         # 自定义数组来规定传到前端的数据
#         appointment = []
#         pet_name = get_pet_by_id(a.pet).petsname
#         doctor_name = get_doctor_by_id(a.doctor).doctorname
#         date = a.date
#         appointment.append(pet_name)
#         appointment.append(doctor_name)
#         appointment.append(date)
#         appointment.append(a.id)
#         appointment_list.append(appointment)
#     print(appointment_list)

#     a = getUserAppointment(session.get('username'))
#     return render_template('appointments.html',username=session.get("username"),apppointments=appointment_list, pets_list=pets_list, doctors_list=doctors_list)

# @app.route('/employee_appointment',methods=['GET','POST'])
# def employee_appointment_page():
#     if not session.get('username'):
#         return err_login()
#     print(session.get('username'))
#     # if (request.form.get("submit") == 'add'):
#     #     addAppointment(request.form['pet_id'], request.form['doctor_id'], request.form['date'],
#     #                    request.form['emergency'], request.form['description'])
#     if (request.form.get("delete_appointment")):
#         deleteAppointment(request.form.get("delete_appointment"))
#     if (request.form.get("update_appointment")):
#         print('正在更新Appointment')
#         updateAppointment_e(request.form.get("update_appointment"), doctorid=request.form['doctor_id'],
#                           date=request.form['date'],time_slot=request.form['time_slot'],status=request.form['status'])

#     #构建的appointment_list根据appointment的id顺序
#     appointments_in_db = getAllAppointment()
#     #构建一个list传输数据到前端
#     appointments_list = []
#     for a_in_db in appointments_in_db:
#         a = []
#         a_id = a_in_db.id
#         pet_id = a_in_db.pet
#         user_id = get_pet_by_id(pet_id).owner
#         user_name = getUserFromId(user_id).username
#         pet_name = get_pet_by_id(pet_id).petsname
#         doc_id = a_in_db.doctor
#         doc_name = get_doctor_by_id(doc_id).doctorname
#         date = a_in_db.date
#         time_slot = a_in_db.time_slot
#         status = a_in_db.status
#         des = a_in_db.description
#         a = [a_id, user_id, user_name, pet_id, pet_name, doc_id, doc_name, date, time_slot, status, des]
#         appointments_list.append(a)

#     doctors = getAllDoctors()
#     doctors_list = [[d.id, d.doctorname] for d in doctors]
#     print(appointments_list)
#     return render_template('employee_appointments.html', appointments=appointments_list, doctors_list=doctors_list, username=session.get("username"))


# @app.route("/profile",methods=["GET","POST"])
# def profile_page():
#     if not session.get('username'):
#         return err_login()

#     if request.method=='POST':
#         print(request.form)
#         save_file(DatabaseSecretConfig.userimgdir,request.files.get('icon'), session.get('username')+'.jpg')
#         updateUserBirthday(request.form.get('username'),request.form.get('date'))
#         updateUserEmail(request.form.get('username'),request.form.get('mail'))
#         updateUserGender(request.form.get('username'),request.form.get('gender')=='male')
        
#     username=session.get('username')
#     return render_template("profile.html",rand=rand(),user=username,appointments=getUserAppointment(username),pets=getUserPets(username),username=username)
# @app.route("/pets",methods=["GET","POST"])
# def pets_page():
#     if not session.get('username'):
#         return err_login()
#     if(request.form.get("submit")=='add'):
#         #获取新pet的id
#         new_pet_id = addPet(request.form['pet_name'],session.get('username'),4,request.form['pet_birthday'])
#         dir_name = 'pet_' + '' + str(new_pet_id) + '.jpg'
#         save_file(DatabaseSecretConfig.petimgdir, request.files.get('icon'), dir_name)
#     if(request.form.get("delete_pet")):
#         deletePet(request.form.get("delete_pet"))
#     if(request.form.get("update_pet")):
#         updatePet(request.form.get("update_pet"),request.form['pet_name'],int(request.form['pet_health']),request.form['pet_birthday'])
#         pet_id = request.form.get("update_pet")
#         print("更新pet id为" + str(pet_id))
#         dir_name = 'pet_' + '' + str(pet_id) + '.jpg'
#         save_file(DatabaseSecretConfig.petimgdir, request.files.get('icon'), dir_name)

#     return render_template("pets.html",username=session.get("username"),pets=getUserPets(session.get('username')))

# @app.route("/employee_pets",methods=["GET","POST"])
# def employee_pets_page():
#     if not session.get('username'):
#         return err_login()
#     if (request.form.get("update_pet")):
#         updatePet_e(request.form.get("update_pet"), int(request.form['pet_health']))

#     return render_template("employee_pets.html",pets=getAllPets(), username = session.get('username'))

# @app.route("/")
# @app.route("/introduction")
# def introduction_page():
#     global error_info
#     a=error_info
#     error_info=None
#     print(session.get('user_level'))
#     if session.get('user_level') is not None:
#         if session['user_level'] == 'employee':
#             return redirect('/employee_questions_list')
#     return render_template("introduction.html",username=session.get("username"),error_info=a)

# @app.route("/doctors")
# def doctors_page():
#     return render_template("doctors.html",username=session.get("username"),users=getAllUser(),rand=rand())

# @app.route("/register",methods=["GET","POST"])
# def register():
#     if(request.method=="POST"):
#         username=request.form.get('username')
#         password=request.form.get('password')
#         if(checkUserExist(request.form.get('username'))):
#             print('exist')
#             global error_info
#             error_info='user name exist'
#             return redirect("/introduction")
#         addUser(username,password)
#         session['username']=request.form.get("username")
#     return redirect("/introduction")

# @app.route("/locations")
# def location_page():
#     return render_template("locations.html",username=session.get("username"))


# @app.route("/manage")
# def manager_page():
#     return render_template("manager.html",users=getAllUser())


# @app.route("/android/doctors",methods=["POST"])
# def send_android_doctors():
#     doc_list=getAllDoctors()
#     result=""
#     for d in doc_list:
#         result+=d.formatCode("ccddll")+"dlcc"
#     return result

# @app.route("/cover")
# def cover_route():
# 	return render_template("cover.html",username=session.get("username"))

# @app.route("/admin",methods=["GET","POST"])
# def pet_page():
#     if(request.form.get("submit")=='1'):
#         addPet(request.form['pet_name'],session.get('username'),int(request.form['pet_health']),request.form['pet_birthday'])
#     if(request.form.get("submit")=='2'):
#         addDoctor(request.form['doctor_name'],int(request.form['age']),request.form['doctor_telphone'],request.form['doctor_introduction'])
#     if(request.form.get("delete_pet")):
#         deletePet(request.form.get("delete_pet"))
#     if(request.form.get("delete_doctor")):
#         deleteDoctor(request.form.get("delete_doctor"))
#     if(request.form.get("update_doctor")):
#         updateDoctor(request.form.get("update_doctor"),request.form['doctor_name'],int(request.form['age']),request.form['doctor_telphone'],request.form['doctor_introduction'])
#     if(request.form.get("update_pet")):
#         updatePet(request.form.get("update_pet"),request.form['pet_name'],int(request.form['pet_health']),request.form['pet_birthday'])
#     return render_template("admin.html", pet_list=getAllPets(),doctor_list=getAllDoctors())

# @app.route("/employee_questions_list",methods=["GET","POST"])
# def employee_questions_list():
#     if not session.get('username'):
#         return err_login()
#     questions_in_db = getAllQuestions()
#     #传到前端的数据
#     questions = []
#     for q_in_db in questions_in_db:
#         user_in_db = getUserFromId(q_in_db.user)
#         #检测是否是customer
#         if user_in_db.user_level == 0:
#             qid = q_in_db.id
#             username = user_in_db.username
#             last_reply = get_last_reply(qid)
#             reply_content = last_reply.content
#             q = []
#             print("用户id是" + str(user_in_db.id))
#             print("qid是" + str(qid))
#             q.append(qid)
#             q.append(username)
#             q.append(reply_content)
#             questions.append(q)
#     print(questions)
#     return render_template("employee_questions_list.html",questions=questions)

# @app.route("/employee_question/<int:id>",methods=["GET","POST"])
# def employee_question(id):
#     if not session.get('username'):
#         return err_login()

#     print("User Name"+session.get('username'))

#     if request.method == 'POST':
#         if request.values.get('type') == 'e_reply':
#             content = request.values.get('content')
#             #数据库刷新
#             ##为什么是3？？？？？？这个地方为什么不打印 草尼玛
#             addReply(user_id=getUser(session.get('username')).id, content=content, q_id=id)
#             return content
#     #数据库读取
#     #目前只读为id为1的
#     q_id = id
#     replies_in_db = get_replies_by_question(q_id=q_id)
#     replies = []
#     for r_in_db in replies_in_db:
#         r = []
#         r.append(q_id)
#         r.append(getUserFromId(r_in_db.user).username)
#         r.append(r_in_db.content)
#         replies.append(r)
#     return render_template("employee_question.html", replies = replies, username = session.get('username'), qid=id)

# @app.route("/customer_question",methods=["GET","POST"])
# def customer_question():
#     if not session.get('username'):
#         return err_login()

#     print("User Name"+session.get('username'))

#     if request.method == 'POST':
#         if request.values.get('type') == 'reply':
#             content = request.values.get('content')
#             #数据库刷新
#             addReply(user_id=getUser(session.get('username')).id, content=content, q_id=get_question_by_user(user=getUser(session.get('username')).id).id)
#             return content
#     #数据库读取
#     #目前只读为id为1的
#     q_id = get_question_by_user(user=getUser(session.get('username')).id).id
#     print("qid = " + str(q_id))
#     replies_in_db = get_replies_by_question(q_id=q_id)
#     print(replies_in_db)
#     replies = []
#     for r_in_db in replies_in_db:
#         r = []
#         r.append(q_id)
#         r.append(getUserFromId(r_in_db.user).username)
#         r.append(r_in_db.content)
#         replies.append(r)
#     return render_template("customer_question.html", replies = replies, username = session.get('username'))

# @app.route('/css/<filename>')
# def get_css(filename):
#     return send_from_directory(DatabaseSecretConfig.cssdir,filename)
# @app.route('/img/<filename>')
# def get_img(filename):
#     return send_from_directory(DatabaseSecretConfig.imgdir,filename)

# @app.route('/img/<filename>')
# def get_pet_img(filename):
#     return send_from_directory(DatabaseSecretConfig.petimgdir,filename)

# @app.route('/icon/<rand>/<filename>')
# def get_icon(rand,filename):
#     return send_from_directory(DatabaseSecretConfig.userimgdir,filename)

# @app.route('/js/<filename>')
# def get_js(filename):
#     return send_from_directory(DatabaseSecretConfig.jsdir,filename)
