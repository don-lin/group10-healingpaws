from healingpaws import db
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(64))
    passwordHash=db.Column(db.String(64))
    user_level=db.Column(db.Integer)
    email=db.Column(db.String,default="no email")
    dateOfBirth=db.Column(db.String,default="unknown birthday")
    isMale=db.Column(db.Boolean,default=True)

    pet=db.relationship('Pets',backref="pet_owner",lazy="dynamic")
    doctorInfo=db.relationship("Doctors",backref="doctor_user",lazy="dynamic")

    def __repr__(self):
        return "id : "+str(self.id)+" name : "+self.username+" email : "+self.email+" birthday : "+self.dateOfBirth+" male : "+str(self.isMale) +" level : "+str(self.user_level)+"\n"

class Pets(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    petsname=db.Column(db.String(64))
    owner=db.Column(db.Integer,db.ForeignKey('user.id'))
    health=db.Column(db.Integer,default=-1)
    birthDay=db.Column(db.String,default="unknown birthday")
    appoinment=db.relationship('Appoinments',backref="appoint_pet",lazy="dynamic")
    def __repr__(self):
        return "id : "+str(self.id)+" pet name : "+self.petsname+" owner : "+str(self.owner)+" health : "+str(self.health)+" birthday : "+self.birthDay +"\n"


class Doctors(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    userId=db.Column(db.Integer,db.ForeignKey("user.id"))
    doctorname=db.Column(db.String(64))
    age=db.Column(db.Integer)
    telphone=db.Column(db.String)
    introduction=db.Column(db.String)
    appoinment=db.relationship('Appoinments',backref="appoint_doctor",lazy="dynamic")
    def formatCode(self,format):
        return str(self.id)+format+self.doctorname+format+str(self.age)+format+self.telphone+format+self.introduction

    def __repr__(self):
        return "id : "+str(self.id)+" doctor name : "+self.doctorname+" age : "+str(self.age)+" telphone : "+self.telphone+" introduction : "+self.introduction +"\n"

class Appoinments(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    pet=db.Column(db.Integer,db.ForeignKey('pets.id'))
    doctor=db.Column(db.Integer,db.ForeignKey('doctors.id'))
    date=db.Column(db.String)
