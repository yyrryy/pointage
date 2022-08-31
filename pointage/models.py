# create models
from pointage import db

class Functions(db.models):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    

class Employees(db.models):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    cin1=db.Column(db.String(30),nullable=False)
    cin2=db.Column(db.String(30),nullable=False)
    datestart=db.Column(db.DateTime,nullable=False)
    dateend=db.Column(db.DateTime,nullable=False)
    salary=db.Column(db.Integer,nullable=False)
    function_id=db.Column(db.Integer,db.ForeignKey('function.id'),nullable=False)
    function=db.relationship('Functions',backref='employees')
    

class Activities(db.models):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)

class Attendence(db.models):
    date=db.Column(db.DateTime,nullable=False)
    # employee will be a relationship with employees table
    employee_id=db.Column(db.Integer,db.ForeignKey('employees.id'),nullable=False)
    employee=db.relationship('Employees',backref=db.backref('attendence',lazy=True))
    hours=db.Column(db.Integer, nullabl=False)
    activity_id=db.Column(db.Integer,db.ForeignKey('activities.id'),nullable=False)
    activity=db.relationship('Activities',backref=db.backref('attendence',lazy=True))
    
