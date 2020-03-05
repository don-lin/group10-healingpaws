import  time
from werkzeug.security import check_password_hash, generate_password_hash
from healingpaws import db
from healingpaws.models import User,Pets,Doctors,Appoinments


def checkUserExist(username):
    users=getAllUser()
    for u in users:
        if(username==u.username):
            return True
    return False

def checkUserPassword(username,userPassword):
    users=getAllUser()
    for u in users:
        if(username==u.username and check_password_hash(u.passwordHash,userPassword)):
            return True
    return False

def addUser(username,passwordHash):
    u1=User(username=username,passwordHash=passwordHash)
    db.session.add(u1)
    db.session.commit()

def addPet(petname,petHealth,birthday):
    p1=Pets(petsname=petname,health=petHealth,birthDay=birthday)
    db.session.add(p1)
    db.session.commit()

def addDoctor(name,age,telphone,introduction):
    d1=Doctors(doctorname=name,age=age,telphone=telphone,introduction=introduction)
    db.session.add(d1)
    db.session.commit()

# def addNewMessage(username,title,)

def getTime():
    return time.strftime("%Y/%m/%d  %I:%M:%S")

def genNewComment(username,content):
    result=username+"_;_"+getTime()+"_;_"+content+"_;_"
    return result


def filtMessage(username,messages):
    result=[]
    for m in messages:
        if(m.get('username')==username):
            result.append(m)
    return result


def updateUserBirthday(username,birthday):
    User.query.filter_by(username=username).update({'dateOfBirth':birthday})
    db.session.commit()
def updateUserEmail(username,email):
    User.query.filter_by(username=username).update({'email':email})
    db.session.commit()
def updateUserGender(username,isMale):
    User.query.filter_by(username=username).update({'isMale':isMale})
    db.session.commit()
def updateUserPassword(username,newPassword):
    newHash=generate_password_hash(newPassword)
    User.query.filter_by(username=username).update({'passwordHash':newHash})
    db.session.commit()

def updateDoctor(docid,name,age,telphone,introduction):
    Doctors.query.filter_by(id=docid).update({'doctorname':name,'age':age,'telphone':telphone,'introduction':introduction})
    db.session.commit()
def updatePet(petid,petname,petHealth,birthday):
    Pets.query.filter_by(id=petid).update({'petsname':petname,'health':petHealth,'birthDay':birthday})
    db.session.commit()
def deletePet(petid):
    Pets.query.filter_by(id=petid).delete()
    db.session.commit()
def deleteDoctor(docid):
    Doctors.query.filter_by(id=docid).delete()
    db.session.commit()
def deleteUser(username):
    User.query.filter_by(username=username).delete()
    db.session.commit()
def getAllUserNameList():
    users=getAllUser()
    result=[]
    for u in users:
        result.append(u.username)
    return result
def getAllUser():
    return User.query.all()
def getAllPets():
    return Pets.query.all()
def getAllDoctors():
    return Doctors.query.all()
def getUser(username):
    users=getAllUser()
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


def databaseDebug():
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