from appdir import db
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(64))
    passwordHash=db.Column(db.String(64))
    email=db.Column(db.String,default="no email")
    dateOfBirth=db.Column(db.String,default="unknown birthday")
    isMale=db.Column(db.Boolean,default=True)

    pet=db.relationship('Pets',backref="pet_owner",lazy="dynamic")

    def __repr__(self):
        return "id = "+str(self.id)+" name="+self.username+" password="+self.passwordHash+\
        " email="+self.email+" birthday="+self.dateOfBirth+" male="+str(self.isMale) + "\n"

class Pets(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    petsname=db.Column(db.String(64))
    owner=db.Column(db.Integer,db.ForeignKey('user.id'))
    health=db.Column(db.Integer,default=-1)
    birthDay=db.Column(db.String,default="unknown birthday")
    appoinment=db.relationship('Appoinments',backref="appoint_pet",lazy="dynamic")


class Doctors(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    doctorname=db.Column(db.String(64))
    age=db.Column(db.Integer)
    telphone=db.Column(db.String)
    appoinment=db.relationship('Appoinments',backref="appoint_doctor",lazy="dynamic")

class Appoinments(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    pet=db.Column(db.Integer,db.ForeignKey('pets.id'))
    doctor=db.Column(db.Integer,db.ForeignKey('doctors.id'))
    date=db.Column(db.String)
