from healingpaws import db
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(64))
    passwordHash=db.Column(db.String(64))
    user_level=db.Column(db.Integer,default=0)
    email=db.Column(db.String,default="no email")
    dateOfBirth=db.Column(db.String,default="unknown birthday")
    isMale=db.Column(db.Boolean,default=True)


    def __repr__(self):
        return "id : "+str(self.id)+" name : "+self.username+" email : "+self.email+" birthday : "+self.dateOfBirth+" male : "+str(self.isMale) +" level : "+str(self.user_level)+"\n"

class Pets(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    petsname=db.Column(db.String(64))
    owner=db.Column(db.Integer)
    health=db.Column(db.Integer,default=-1)
    birthDay=db.Column(db.String,default="unknown birthday")
    def formatCode(self,format):
        return str(self.id)+format+self.petsname+format+self.birthDay+format+str(self.health)
    def __repr__(self):
        return "id : "+str(self.id)+" pet name : "+self.petsname+" owner : "+str(self.owner)+" health : "+str(self.health)+" birthday : "+self.birthDay +"\n"


class Doctors(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    userId=db.Column(db.Integer)
    doctorname=db.Column(db.String(64))
    age=db.Column(db.Integer)
    telphone=db.Column(db.String)
    introduction=db.Column(db.String)
    def formatCode(self,format):
        return str(self.id)+format+self.doctorname+format+str(self.age)+format+self.telphone+format+self.introduction

    def __repr__(self):
        return "id : "+str(self.id)+" doctor name : "+self.doctorname+" age : "+str(self.age)+" telphone : "+self.telphone+" introduction : "+self.introduction +"\n"

class Appointments(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    pet=db.Column(db.Integer)
    doctor=db.Column(db.Integer)
    date=db.Column(db.String)
    priority=db.Column(db.Integer)
    hospital=db.Column(db.Integer)
    status=db.Column(db.Integer)
    time=db.Column(db.Integer,default=0)

    def __repr__(self):
        return 'id: '+str(self.id)+' pet: '+str(self.pet)+' doctor: '+str(self.doctor)+' date: '+str(self.date)


class Chat(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    from_user=db.Column(db.String)
    to_user=db.Column(db.String)
    date=db.Column(db.String)
    content=db.Column(db.String)

    def prepare_send(self,key):
        return str(self.id)+key+str(self.from_user)+key+str(self.to_user)+key+self.date+key+self.content

    def __repr__(self):
        return 'from: '+str(self.from_user)+' to: '+str(self.to_user)+" "+self.date+" content: "+self.content+'\n'

