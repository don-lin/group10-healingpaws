import  time
from werkzeug.security import check_password_hash, generate_password_hash
from healingpaws import db
from healingpaws.models import User,Pets,Doctors,Appointments,Question,Reply


def checkUserExist(username):
    return not getUser(username) is None

#检查这个用户是否是员工
def checkIfEmployee(username):
    user = getUser(username)
    if user.user_level == 2:
        return True
    else:
        return False

def checkUserPassword(username,userPassword):
    users=getAllUser()
    for u in users:
        if(username==u.username and check_password_hash(u.passwordHash,userPassword)):
            return True
    return False


def addUser(username,password):
    u1=User(username=username,passwordHash=generate_password_hash(password),user_level=0)
    add_question(u1.id)
    db.session.add(u1)
    db.session.commit()
#sadasdwaodpkl,;adawdwdasdasdsadasdasdasdsdasdasdasdasdsasdadssdas

def updateUserBirthday(username,birthday):
    if not birthday:
        return
    User.query.filter_by(username=username).update({'dateOfBirth':birthday})
    db.session.commit()
def updateUserEmail(username,email):
    if not email:
        return
    User.query.filter_by(username=username).update({'email':email})
    db.session.commit()
def updateUserGender(username,isMale):
    User.query.filter_by(username=username).update({'isMale':isMale})
    db.session.commit()
def updateUserPassword(username,newPassword):
    newHash=generate_password_hash(newPassword)
    User.query.filter_by(username=username).update({'passwordHash':newHash})
    db.session.commit()

def deleteUser(username):
    User.query.filter_by(username=username).delete()
    db.session.commit()

def getAllUser():
    return User.query.all()

def getAllCustomer():
    return User.query.filter_by(user_level=0).all()

def getUser(username):
    users=User.query.filter_by(username=username).all()
    for u in users:
        if u.username==username:
            return u
    return None

def getUserFromId(userid):
    users=getAllUser()
    for u in users:
        if u.id==userid:
            return u
    return None

def showUsers(users):
    for u in users:
        print(u)

def getAllUserNameList():
    users=getAllUser()
    result=[]
    for u in users:
        result.append(u.username)
    return result



#这个函数更改为返回添加的这个pet的id
def addPet(petname,ownername,petHealth,birthday):
    userid=getUser(ownername).id
    print('\033[44m')
    print('user id is :'+str(userid))
    print('\033[0m')
    p1=Pets(petsname=petname,owner=userid,health=petHealth,birthDay=birthday)
    db.session.add(p1)
    db.session.commit()
    return p1.id


def updatePet(petid,petname,petHealth,birthday):
    Pets.query.filter_by(id=petid).update({'petsname':petname,'health':petHealth,'birthDay':birthday})
    db.session.commit()

#employee专用
def updatePet_e(petid,petHealth):
    Pets.query.filter_by(id=petid).update({'health':petHealth})
    db.session.commit()

def deletePet(petid):
    Pets.query.filter_by(id=petid).delete()
    db.session.commit()

def getAllPets():
    return Pets.query.all()

def getAllQuestions():
    return Question.query.all()

def getAllReplies():
    return Reply.query.all()

def getUserPets(username):
    userid=getUser(username).id
    return Pets.query.filter_by(owner=userid).all()


def addDoctor(name,age,telphone,introduction):
    d1=Doctors(doctorname=name,age=age,telphone=telphone,introduction=introduction)
    db.session.add(d1)
    db.session.commit()

def updateDoctor(docid,name,age,telphone,introduction):
    Doctors.query.filter_by(id=docid).update({'doctorname':name,'age':age,'telphone':telphone,'introduction':introduction})
    db.session.commit()

def getAllDoctors():
    return Doctors.query.all()

def deleteDoctor(docid):
    Doctors.query.filter_by(id=docid).delete()
    db.session.commit()


def genNewComment(username,content):
    result=username+"_;_"+getTime()+"_;_"+content+"_;_"
    return result


def filtMessage(username,messages):
    result=[]
    for m in messages:
        if(m.get('username')==username):
            result.append(m)
    return result


def getTime():
    return time.strftime("%Y/%m/%d  %I:%M:%S")

# 添加一个新的question
def add_question(user):
    q1 = Question(user=user,title="What's up")
    db.session.add(q1)
    db.session.commit()

#为每一个用户创建一个channel,这里假如已经创建过了就会忽律
def add_questions_for_all_users():
    #这里只为customer创建信道
    all_customer = User.query.filter_by(user_level=0).all()
    for c in all_customer:
        #如果该用户还没有channel就创建一个question
        if not check_user_channel(c.id):
            print("add_questions_for_all_users")
            add_question(c.id)

#检查是否为该用户创建channel
def check_user_channel(user_id):
    q = Question.query.filter_by(user=user_id).first()
    print(q)
    if q is None:
        print("为用户id " + str(user_id) + " 创建聊天信道")
        return False
    else:
        print("用户id " + str(user_id) + " 已经有聊天信道了")
        return True

def addReply(user_id, content, q_id):
    r = Reply(user=user_id, content=content, question_id=q_id)
    db.session.add(r)
    db.session.commit()


def addAppointment(petid,doctorid,date,emergency,description):
    a=Appointments(pet=petid,doctor=doctorid,date=date,emergency=emergency,description=description)
    db.session.add(a)
    db.session.commit()

def updateAppointment(appointmentid,petid,doctorid,date):
    Appointments.query.filter_by(id=appointmentid).update({'pet':petid,'doctor':doctorid,'date':date})
    db.session.commit()

#员工操作的更新
def updateAppointment_e(appointmentid,doctorid,date,time_slot,status):
    Appointments.query.filter_by(id=appointmentid).update({'doctor':doctorid,'date':date,'time_slot':time_slot,'status':status})
    db.session.commit()

#根据Pet找Appointment
def getPetsAppointment(petid):
    return Appointments.query.filter_by(pet=petid).all()

def getAllAppointment():
    return Appointments.query.all()

def getUserAppointment(username):
    pets=getUserPets(username)
    result=[]
    for p in pets:
        result+=getPetsAppointment(p.id)
    return result

def get_question_by_user(user):
    if check_user_channel(user):
        print("get_question_by_user")
        return Question.query.filter_by(user=user).first()
    else:
        add_question(user=user)
        return Question.query.filter_by(user=user).first()

def get_question_by_id(id):
    questions = getAllQuestions()
    for q in questions:
        if q.id == id:
            return q
    return None

def get_replies_by_question(q_id):
    replies = getAllReplies()
    result = []
    # print(replies)
    # print(replies[0])
    #无故报错 说reply对象不可迭代？

    for i in range(len(replies)):
        r = replies[i]
        if r.question_id == q_id:
            result.append(r)
    return result

#获取该的question的最后一个relpy
def get_last_reply(q_id):
    replies = get_replies_by_question(q_id)
    return replies[len(replies)-1]

def get_pet_by_id(pet_id):
    pets = Pets.query.filter_by(id=pet_id).all()
    for p in pets:
        if p.id == pet_id:
            return p
    return None

def get_doctor_by_id(doctor_id):
    doctors = Doctors.query.filter_by(id=doctor_id).all()
    for d in doctors:
        if d.id == doctor_id:
            return d
    return None

def deleteAppointment(appointmentid):
    Appointments.query.filter_by(id=appointmentid).delete()
    db.session.commit()



def databaseDebug():
    #调试数据库
    addUser("donlin", "000")
    showUsers(getAllUser())

    updateUserBirthday("donlin", "1998")
    showUsers(getAllUser())

    updateUserEmail("donlin", "donlin@qq.com")
    showUsers(getAllUser())

    updateUserGender("donlin", True)
    showUsers(getAllUser())

    print(checkUserExist("donlin"))
    print(checkUserExist("donlin1"))

    deleteUser("donlin")
    showUsers(getAllUser())

def checkHashLoop(hash):
    pass_hash=generate_password_hash("hello")
    print("hash is ")
    print(pass_hash)
    while True:
        i=input()
        print("check result:")
        print(check_password_hash(pass_hash,i))