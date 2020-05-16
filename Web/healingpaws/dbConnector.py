import  time
from werkzeug.security import check_password_hash, generate_password_hash
from healingpaws import db
from healingpaws.models import User,Pets,Doctors,Appointments,Chat
from sqlalchemy import or_,and_


def checkUserExist(username):
    return not getUser(username) is None

def checkUserPassword(username,userPassword):
    users=getAllUser()
    for u in users:
        if(username==u.username and check_password_hash(u.passwordHash,userPassword)):
            return True
    return False

def addUser(username,password):
    u1=User(username=username,passwordHash=generate_password_hash(password))
    db.session.add(u1)
    db.session.commit()

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

def updateUserAccount(username,newaccount):
    User.query.filter_by(username=username).update({'user_level':int(newaccount)})
    db.session.commit()


def deleteUser(username):
    User.query.filter_by(username=username).delete()
    db.session.commit()

def getAllUser():
    return User.query.all()

def getAllDoctor():
    return User.query.filter(User.user_level==1).all()

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




def addPet(petname,ownername,petHealth,birthday):
    userid=getUser(ownername).id
    print('\033[44m')
    print('user id is :'+str(userid))
    print('\033[0m')
    p1=Pets(petsname=petname,owner=userid,health=petHealth,birthDay=birthday)
    db.session.add(p1)
    db.session.commit()
    return p1


def updatePet(petid,petname,petHealth,birthday):
    Pets.query.filter_by(id=petid).update({'petsname':petname,'health':petHealth,'birthDay':birthday})
    db.session.commit()
def deletePet(petid):
    Pets.query.filter_by(id=petid).delete()
    deletePetAppointment(petid)
    db.session.commit()

def getAllPets():
    return Pets.query.all()

def getUserPets(username):
    user=getUser(username)
    if user is None:
        return []
    if(user.user_level==2):
        return getAllPets()
    userid=getUser(username).id
    return Pets.query.filter_by(owner=userid).all()
def getPet(petid):
    return Pets.query.filter_by(id=petid).first()

def updateAppointmentTime(id,time):
    Appointments.query.filter_by(id=id).update({'time':time})
    db.session.commit()
    
def sortAppointment(appointments):
    for a in appointments:
        a.p=a.priority*3+getPet(a.pet).health
    appointments.sort(key=lambda x:x.p,reverse=True)
    
    for i in range(len(appointments)):
        appointments[i].time=int(8.0*i/len(appointments))
        updateAppointmentTime(appointments[i].id,appointments[i].time)
    return appointments

def sortAndUpdateAllAppointment():
    appointments=getAllAppointment()
    dic={}
    for a in appointments:
        if a.date:
            if dic.get(a.date) is None:
                dic[a.date]=[]
            dic[a.date].append(a)
    
    for aa in dic:
        sortAppointment(dic.get(aa))

def addDoctor(name,age,telphone,introduction):
    d1=Doctors(doctorname=name,age=age,telphone=telphone,introduction=introduction)
    db.session.add(d1)
    db.session.commit()

def updateDoctor(docid,name,age,telphone,introduction):
    Doctors.query.filter_by(id=docid).update({'doctorname':name,'age':age,'telphone':telphone,'introduction':introduction})
    db.session.commit()

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


def addAppointment(petid,doctorid,date,priority,hospital,status):
    a=Appointments(pet=petid,doctor=doctorid,date=date,priority=priority,hospital=hospital,status=status)
    db.session.add(a)
    db.session.commit()
    sortAndUpdateAllAppointment()

def updateAppointment(appointmentid,petid,doctorid,date,priority,hospital,status):
    Appointments.query.filter_by(id=appointmentid).update({'pet':petid,'doctor':doctorid,'date':date,'priority':priority,'hospital':hospital,'status':status})
    db.session.commit()
    sortAndUpdateAllAppointment()

def getPetAppointment(petid):
    return Appointments.query.filter_by(pet=petid).all()
def getDoctorAppointment(docid):
    return Appointments.query.filter_by(doctor=docid).all()

def getAllAppointment():
    return Appointments.query.all()

def getUserAppointment(username):
    if(getUser(username).user_level==2):
        return getAllAppointment()
    if(getUser(username).user_level==1):
        return getDoctorAppointment(getUser(username).id)

    pets=getUserPets(username)
    result=[]
    for p in pets:
        result+=getPetAppointment(p.id)
    return result

def getDateAppointment(date):
    return Appointments.query.filter(Appointments.date==date).all()

def getHospitalAppointment(hospital):
    return Appointments.query.filter(Appointments.hospital==hospital).all()

def deletePetAppointment(petid):
    Appointments.query.filter_by(pet=petid).delete()
    db.session.commit()
    sortAndUpdateAllAppointment()
    
def deleteAppointment(appointmentid):
    Appointments.query.filter_by(id=appointmentid).delete()
    db.session.commit()
    sortAndUpdateAllAppointment()


def chat(from_user,to_user,content):
    c=Chat(from_user=from_user,to_user=to_user,date=getTime(),content=content)
    db.session.add(c)
    db.session.commit()

def deleteChat(chatid):
    Chat.query.filter_by(id=chatid).delete()
    db.session.commit()

def updateChat(chatid,newcontent):
    Chat.query.filter_by(id=chatid).update({'content':newcontent})
    db.session.commit()

def getChat(usera,userb):
    return Chat.query.filter(
        or_(
        and_(Chat.from_user==usera, Chat.to_user==userb),
        and_(Chat.to_user==usera, Chat.from_user==userb))
        ).all()

def getAllChat():
    return Chat.query.all()

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