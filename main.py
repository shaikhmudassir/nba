from flask import Flask,render_template,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from itertools import cycle
import os
import csv
import math
import time
total=0

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/nba'
#app.config['UPLOAD_FOLDER'] = 'C:\\Python37\\Projects\\NBA\\files' #error
app.config['UPLOAD_FOLDER'] = app.root_path + '/files'

db = SQLAlchemy(app)

app.secret_key = 'MGMPOLYTECHNIC'

class Index(db.Model):
  Id = db.Column(db.Integer,primary_key=True)
  academicYear = db.Column(db.String(100),unique=False,nullable=False)
  semester = db.Column(db.Integer,unique=False,nullable=False)
  faculty = db.Column(db.String(100),unique=False,nullable=False)
  subject = db.Column(db.String(100),unique=False,nullable=False)
  subjectCode = db.Column(db.Integer,unique=False,nullable=False)
  abbreviation = db.Column(db.String(100),unique=False,nullable=False)
  courseSemester = db.Column(db.Integer,unique=False,nullable=False)
  coCode = db.Column(db.Integer,unique=False,nullable=False)
  ese_th = db.Column(db.Integer,unique=False,nullable=False)
  ese_prh = db.Column(db.Integer,unique=False,nullable=False)
  ct = db.Column(db.Integer,unique=False,nullable=False)
  mp = db.Column(db.Integer,unique=False,nullable=False)
  ese_pra = db.Column(db.Integer,unique=False,nullable=False)
  pr_pa = db.Column(db.Integer,unique=False,nullable=False)
  userId = db.Column(db.Integer,unique=False,nullable=False)
  filename = db.Column(db.String(100),unique=False,nullable=True)


class Login(db.Model):
  Id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(100),unique=False,nullable=False)
  password = db.Column(db.String(100),unique=False,nullable=False)


class Studentlist(db.Model):
  Id = db.Column(db.Integer,primary_key=True)
  rollNo = db.Column(db.Integer,unique=False,nullable=False)
  enrollNo = db.Column(db.Integer,unique=False,nullable=False)
  studentsName = db.Column(db.String(100),unique=False,nullable=False)
  fieldId = db.Column(db.Integer,unique=False,nullable=False)


class Comapping(db.Model):
  Id = db.Column(db.Integer,primary_key=True)
  coCode = db.Column(db.String(100),unique=False,nullable=False)
  statement = db.Column(db.String(100),unique=False,nullable=False)
  po1 = db.Column(db.Integer,unique=False,nullable=True)
  po2 = db.Column(db.Integer,unique=False,nullable=True)
  po3 = db.Column(db.Integer,unique=False,nullable=True)
  po4 = db.Column(db.Integer,unique=False,nullable=True)
  po5 = db.Column(db.Integer,unique=False,nullable=True)
  po6 = db.Column(db.Integer,unique=False,nullable=True)
  po7 = db.Column(db.Integer,unique=False,nullable=True)
  pso1 = db.Column(db.Integer,unique=False,nullable=True)
  pso2 = db.Column(db.Integer,unique=False,nullable=True)
  fieldId = db.Column(db.Integer,unique=False,nullable=False)


class Micro_project(db.Model):
  Id = db.Column(db.Integer,primary_key=True)
  Co1 = db.Column(db.Integer,unique=False,nullable=True) 
  Co2 = db.Column(db.Integer,unique=False,nullable=True)
  Co3 = db.Column(db.Integer,unique=False,nullable=True)
  Co4 = db.Column(db.Integer,unique=False,nullable=True)
  Co5 = db.Column(db.Integer,unique=False,nullable=True)
  fieldId = db.Column(db.Integer,unique=False,nullable=False)

class Total_micro_project(db.Model):
  Id = db.Column(db.Integer,primary_key=True)
  nostudents_attempted_Co1=db.Column(db.Integer,unique=False,nullable=False)
  nostudents_attempted_Co2=db.Column(db.Integer,unique=False,nullable=False)
  nostudents_attempted_Co3=db.Column(db.Integer,unique=False,nullable=False)
  nostudents_attempted_Co4=db.Column(db.Integer,unique=False,nullable=False)
  nostudents_attempted_Co5=db.Column(db.Integer,unique=False,nullable=False)
  nostudents_more_than_avgMarks_Co1=db.Column(db.Integer,unique=False,nullable=False)
  nostudents_more_than_avgMarks_Co2=db.Column(db.Integer,unique=False,nullable=False)
  nostudents_more_than_avgMarks_Co3=db.Column(db.Integer,unique=False,nullable=False)
  nostudents_more_than_avgMarks_Co4=db.Column(db.Integer,unique=False,nullable=False)
  nostudents_more_than_avgMarks_Co5=db.Column(db.Integer,unique=False,nullable=False)
  per_of_students_more_than_avgMarks_Co1=db.Column(db.Integer,unique=False,nullable=False)
  per_of_students_more_than_avgMarks_Co2=db.Column(db.Integer,unique=False,nullable=False)
  per_of_students_more_than_avgMarks_Co3=db.Column(db.Integer,unique=False,nullable=False)
  per_of_students_more_than_avgMarks_Co4=db.Column(db.Integer,unique=False,nullable=False)
  per_of_students_more_than_avgMarks_Co5=db.Column(db.Integer,unique=False,nullable=False)
  attainment_level_acheived_Co1=db.Column(db.Integer,unique=False,nullable=False)
  attainment_level_acheived_Co2=db.Column(db.Integer,unique=False,nullable=False)
  attainment_level_acheived_Co3=db.Column(db.Integer,unique=False,nullable=False)
  attainment_level_acheived_Co4=db.Column(db.Integer,unique=False,nullable=False)
  attainment_level_acheived_Co5=db.Column(db.Integer,unique=False,nullable=False)
  fieldId = db.Column(db.Integer,unique=False,nullable=False)

class Msbte(db.Model):
  Id=db.Column(db.Integer,primary_key=True)
  rollNo=db.Column(db.Integer,nullable=False)
  StudentName=db.Column(db.String(200),unique=False,nullable=True) 
  TH=db.Column(db.Integer,unique=False,nullable=True)
  PR=db.Column(db.Integer,unique=False,nullable=True)
  fieldId=db.Column(db.Integer,nullable=False)  
 

class Total_msbte(db.Model):
  Id=db.Column(db.Integer,primary_key=True)
  Total_TH=db.Column(db.Integer,unique=False,nullable=True)
  Total_PR=db.Column(db.Integer,unique=False,nullable=True)
  TH_Level=db.Column(db.Integer,unique=False,nullable=True)
  PR_Level=db.Column(db.Integer,unique=False,nullable=True)
  fieldId=db.Column(db.Integer,nullable=False) 


class Test1(db.Model):
  Id=db.Column(db.Integer,primary_key=True)
  rollNo=db.Column(db.Integer,nullable=False)
  StudentName=db.Column(db.String(200),unique=False,nullable=True)  
  CO1_1=db.Column(db.Integer,unique=False,nullable=True)
  CO1_2=db.Column(db.Integer,unique=False,nullable=True)
  CO1_3=db.Column(db.Integer,unique=False,nullable=True)
  CO2_1=db.Column(db.Integer,unique=False,nullable=True)
  CO2_2=db.Column(db.Integer,unique=False,nullable=True)
  CO2_3=db.Column(db.Integer,unique=False,nullable=True)
  CO3_1=db.Column(db.Integer,unique=False,nullable=True)
  CO3_2=db.Column(db.Integer,unique=False,nullable=True)
  CO3_3=db.Column(db.Integer,unique=False,nullable=True)
  CO3_4=db.Column(db.Integer,unique=False,nullable=True)
  CO3_5=db.Column(db.Integer,unique=False,nullable=True)
  fieldId=db.Column(db.Integer,nullable=False)  
  
class TotalTest1(db.Model):
  Id=db.Column(db.Integer,primary_key=True)
  Total_CO1_1=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO1_2=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO1_3=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO2_1=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO2_2=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO2_3=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO3_1=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO3_2=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO3_3=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO3_4=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO3_5=db.Column(db.Integer,unique=False,nullable=True)
  CO1_Level=db.Column(db.Integer,unique=False,nullable=True)
  CO2_Level=db.Column(db.Integer,unique=False,nullable=True)
  CO3_Level=db.Column(db.Integer,unique=False,nullable=True)
  fieldId=db.Column(db.Integer,nullable=False)  

class Test2(db.Model):
  Id=db.Column(db.Integer,primary_key=True)
  rollNo=db.Column(db.Integer,nullable=False)
  StudentName=db.Column(db.String(200),unique=False,nullable=True)  
  CO4_1=db.Column(db.Integer,unique=False,nullable=True)
  CO4_2=db.Column(db.Integer,unique=False,nullable=True)
  CO4_3=db.Column(db.Integer,unique=False,nullable=True)
  CO4_4=db.Column(db.Integer,unique=False,nullable=True)
  CO5_1=db.Column(db.Integer,unique=False,nullable=True)
  CO5_2=db.Column(db.Integer,unique=False,nullable=True)
  CO4_5=db.Column(db.Integer,unique=False,nullable=True)
  CO5_3=db.Column(db.Integer,unique=False,nullable=True)
  CO5_4=db.Column(db.Integer,unique=False,nullable=True)
  CO5_5=db.Column(db.Integer,unique=False,nullable=True)
  fieldId=db.Column(db.Integer,nullable=False)      

class TotalTest2(db.Model):
  Id=db.Column(db.Integer,primary_key=True)
  Total_CO4_1=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO4_2=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO4_3=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO4_4=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO5_1=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO5_2=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO4_5=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO5_3=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO5_4=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO5_5=db.Column(db.Integer,unique=False,nullable=True)
  CO4_Level=db.Column(db.Integer,unique=False,nullable=True)
  CO5_Level=db.Column(db.Integer,unique=False,nullable=True)
  fieldId=db.Column(db.Integer,nullable=False) 

class Prpa(db.Model):
  Id=db.Column(db.Integer,primary_key=True)
  rollNo=db.Column(db.Integer,nullable=False)
  StudentName=db.Column(db.String(200),unique=False,nullable=True)  
  CO1=db.Column(db.Integer,unique=False,nullable=True)
  CO2=db.Column(db.Integer,unique=False,nullable=True)
  CO3=db.Column(db.Integer,unique=False,nullable=True)
  CO4 =db.Column(db.Integer,unique=False,nullable=True)
  CO5=db.Column(db.Integer,unique=False,nullable=True)
  Marks_Obtained=db.Column(db.Integer,unique=False,nullable=True)
  fieldId=db.Column(db.Integer,nullable=False)

class Practical_prpa(db.Model):
  Id=db.Column(db.Integer,primary_key=True) 
  CO1=db.Column(db.Integer,unique=False,nullable=True)
  CO2=db.Column(db.Integer,unique=False,nullable=True)
  CO3=db.Column(db.Integer,unique=False,nullable=True)
  CO4 =db.Column(db.Integer,unique=False,nullable=True)
  CO5=db.Column(db.Integer,unique=False,nullable=True)
  Total=db.Column(db.Integer,unique=False,nullable=True)
  fieldId=db.Column(db.Integer,nullable=False) 

class Total_prpa(db.Model):
  Id=db.Column(db.Integer,primary_key=True)
  Total_CO1=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO2=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO3=db.Column(db.Integer,unique=False,nullable=True)
  Total_CO4 =db.Column(db.Integer,unique=False,nullable=True)
  Total_CO5=db.Column(db.Integer,unique=False,nullable=True)
  Level_CO1=db.Column(db.Integer,unique=False,nullable=True)
  Level_CO2=db.Column(db.Integer,unique=False,nullable=True)
  Level_CO3=db.Column(db.Integer,unique=False,nullable=True)
  Level_CO4 =db.Column(db.Integer,unique=False,nullable=True)
  Level_CO5=db.Column(db.Integer,unique=False,nullable=True)
  fieldId=db.Column(db.Integer,nullable=False)   

class Total_attainment(db.Model):
   Id=db.Column(db.Integer,primary_key=True)
   CO1_level=db.Column(db.Integer,unique=False,nullable=True)
   CO2_level=db.Column(db.Integer,unique=False,nullable=False)
   CO3_level=db.Column(db.Integer,unique=False,nullable=False)
   CO4_level=db.Column(db.Integer,unique=False,nullable=False)
   CO5_level=db.Column(db.Integer,unique=False,nullable=False)
   fieldId=db.Column(db.Integer,nullable=False) 


class Po_attainment(db.Model):
  Id=db.Column(db.Integer,primary_key=True)
  finalpo1=db.Column(db.Integer,unique=False,nullable=True)
  finalpo2=db.Column(db.Integer,unique=False,nullable=False)
  finalpo3=db.Column(db.Integer,unique=False,nullable=False)
  finalpo4=db.Column(db.Integer,unique=False,nullable=False)
  finalpo5=db.Column(db.Integer,unique=False,nullable=False)
  finalpo6=db.Column(db.Integer,unique=False,nullable=False)
  finalpo7=db.Column(db.Integer,unique=False,nullable=False)
  finalpo8=db.Column(db.Integer,unique=False,nullable=False)
  fieldId=db.Column(db.Integer,nullable=False) 

@app.route('/',methods=['GET','POST'])
def dashboard():
  # Following 4 line check user login or not
  if 'user_id' in session:
    pass
  else:
     return redirect('/login')

  select = Index.query.filter_by(userId=session['user_id'])

  return render_template('dashboard.html',rows=select)

@app.route('/index',methods=['GET','POST'])
def index(): 
  if 'user_id' in session:
    pass
  else:
    return redirect('/login')

  # Post Request Maybe Come From Index.html Or Dashboard.html
  if request.method == 'POST':
    academicYear = request.form.get('academicYear')  		
    semester = request.form.get('semester')
    faculty = request.form.get('faculty')
    subject = request.form.get('subject')
    subjectCode = request.form.get('subjectCode')
    abbreviation = request.form.get('abbreviation')
    courseSemester = request.form.get('courseSemester')
    coCode = request.form.get('coCode')
    ese_th = request.form.get('ese_th')
    ese_prh = request.form.get('ese_prh')
    ct = request.form.get('ct')
    mp = request.form.get('mp')
    ese_pra = request.form.get('ese_pra')
    pr_pa = request.form.get('pr_pa')
    tempId1 = request.form.get('tempId1')
    tempId2 = request.form.get('tempId2')
    new = request.form.get('new')

    # New Data Enter Into Index Table
    if new == "new":
      return render_template('index.html',row=None)

    
    # Continue Adding New Data Enter Into Index Table
    if tempId1 == '0':
      entry = Index(
        academicYear = academicYear,  		
        semester = semester,
        faculty = faculty,
        subject = subject,
        subjectCode = subjectCode,
        abbreviation = abbreviation,
        courseSemester = courseSemester,  		 
        coCode = coCode,
        ese_th = ese_th,
        ese_prh = ese_prh,
        ct = ct,
        mp = mp,
        ese_pra = ese_pra,
        pr_pa = pr_pa,
        userId = session['user_id']
      )
      db.session.add(entry)
      db.session.commit()

      select = Index.query.filter_by(userId = session['user_id'], subjectCode=subjectCode, academicYear=academicYear).first()
      session['field_id'] = select.Id

      return redirect('/student-list')

    # Updatig Data in Index table
    elif tempId2 != None:
      select = Index.query.filter_by(Id=tempId2).first()
      select.academicYear = academicYear  		
      select.semester = semester
      select.faculty = faculty
      select.subject = subject
      select.subjectCode = subjectCode
      select.abbreviation = abbreviation
      select.courseSemester = courseSemester
      select.coCode = coCode
      select.ese_th = ese_th
      select.ese_prh = ese_prh
      select.ct = ct
      select.mp = mp
      select.ese_pra = ese_pra
      select.pr_pa = pr_pa
      db.session.commit()
      return redirect('/student-list')
    else:
      if 'field_id' in session:
        session.pop('field_id')

      select = Index.query.filter_by(Id=tempId1).first()
      session['field_id'] = select.Id
      return render_template('index.html',row=select)
  
  # Dispaly Data of selected subject
  if 'field_id' in session:
    select = Index.query.filter_by(Id=session['field_id']).first()
    return render_template('index.html',row=select)
  
  return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)
  


@app.route('/login',methods=['GET','POST'])
def login():
  return render_template('login.html')


@app.route('/login/<string:var>',methods=['GET','POST'])
def loginCheck(var):
  # If var is 0 then perform Registration else perform login
  if var == '0':
    if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
      confirmPassword = request.form.get('confirmPassword')

      if password != confirmPassword:
        return render_template('validation.html',message="Confirm Password Does not match", serverSite=True)

      entry = Login(
        username = username,
        password = generate_password_hash(password),
      )

      db.session.add(entry)
      db.session.commit()
      
      select = Login.query.filter_by(username=username).first()

      if select == None or not check_password_hash(select.password, password):
        return render_template('validation.html',message="Username Or Password is Invalid", serverSite=True)

      session['user_id'] = select.Id
      return redirect('/')

  else:
    if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
      select = Login.query.filter_by(username=username).first()

      if select == None or not check_password_hash(select.password, password):
        return render_template('validation.html',message="Username Or Password is Invalid", serverSite=True)


      session['user_id'] = select.Id
      return redirect('/')

  return render_template('login.html')


@app.route('/student-list',methods=['GET','POST'])
def studentList():
  # Check Login Fieil Id
  if 'user_id' in session :
    pass
  else:
    return redirect('/login')
  if 'field_id' in session:
    pass
  else:
    return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)

  
  # what if file is get replaced ?
  
  # Upload Student list (csv/Execel file)
  select = Studentlist.query.filter_by(fieldId=session['field_id']).all()

  if request.method == 'POST' :
    f = request.files['filename']
    select = Index.query.filter_by(Id=session['field_id']).first()
    filename = select.abbreviation + select.academicYear + '.csv'
    select.filename = filename
    db.session.commit()
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(filename)))
    with open(app.config['UPLOAD_FOLDER'] + '\\' + select.filename,'r') as file:
      rows = csv.DictReader(file)
      if select != None:
        select = Studentlist.query.filter_by(fieldId=session['field_id']).delete()
        db.session.commit()
      for row in rows:
        entry = Studentlist(
          rollNo = row['Roll No.'],
          enrollNo = row['Enroll No.'],
          studentsName = row['Name of Students'], 
          fieldId = session['field_id'],
        )
        db.session.add(entry)
        db.session.commit()
    return redirect('/student-list')
  
  return render_template('student-list.html', rows=select)


@app.route('/mapping',methods=['GET','POST'])
def mapping():
  # Check Login Fieil Id
  if 'user_id' in session :
    pass
  else:
    return redirect('/login')
  if 'field_id' in session:
    pass
  else:
    return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)

  select = Comapping.query.filter_by(fieldId=session['field_id']).all()
  count = len(select)
  edit = None

  if request.method == 'POST':
    statement = request.form.get('statement')
    po1 = request.form.get('po1')
    po2 = request.form.get('po2')
    po3 = request.form.get('po3')
    po4 = request.form.get('po4')
    po5 = request.form.get('po5')
    po6 = request.form.get('po6')
    po7 = request.form.get('po7')
    pso1 = request.form.get('pso1')
    pso2 = request.form.get('pso2')
    Id = request.form.get('Id')
    edit = request.form.get('edit')

    select2 = Index.query.filter_by(Id=session['field_id']).first()
    coCode = select2.coCode + '.' + str(count + 1)
    if edit == 'edited': 
      select2 = Comapping.query.filter_by(Id=Id, fieldId=session['field_id']).first()
      select2.statement = statement
      select2.po1 = po1
      select2.po2 = po2
      select2.po3 = po3
      select2.po4 = po4
      select2.po5 = po5
      select2.po6 = po6
      select2.po7 = po7
      select2.pso1 = pso1
      select2.pso2 = pso2
      db.session.commit()
      return redirect('/mapping')
    elif edit != 'edit' :
      entry = Comapping(
        coCode = coCode,
        statement = statement,
        po1 = po1,
        po2 = po2,
        po3 = po3,
        po4 = po4,
        po5 = po5,
        po6 = po6,
        po7 = po7,
        pso1 = pso1,
        pso2 = pso2,
        fieldId = session['field_id']
      )
      db.session.add(entry)
      db.session.commit()
      return redirect('/mapping')
  
  if count > 0:
    total = {'c_po1':0,'c_po2':0,'c_po3':0,'c_po4':0,'c_po5':0,'c_po6':0,'c_po7':0,'c_pso1':0,'c_pso2':0}
    avg = {'a_po1':0,'a_po2':0,'a_po3':0,'a_po4':0,'a_po5':0,'a_po6':0,'a_po7':0,'a_pso1':0,'a_pso2':0}
    for row in select:
      total['c_po1'] += row.po1
      total['c_po2'] += row.po2
      total['c_po3'] += row.po3
      total['c_po4'] += row.po4
      total['c_po5'] += row.po5
      total['c_po6'] += row.po6
      total['c_po7'] += row.po7
      total['c_pso1'] += row.pso1
      total['c_pso2'] += row.pso2

    avg['a_po1'] = Round(total['c_po1'],count)
    avg['a_po2'] = Round(total['c_po2'],count)
    avg['a_po3'] = Round(total['c_po3'],count)
    avg['a_po4'] = Round(total['c_po4'],count)
    avg['a_po5'] = Round(total['c_po5'],count)
    avg['a_po6'] = Round(total['c_po6'],count)
    avg['a_po7'] = Round(total['c_po7'],count)
    avg['a_pso1'] = Round(total['c_pso1'],count)
    avg['a_pso2'] = Round(total['c_pso2'],count)
    
    if edit == 'edit':
      select2 = Comapping.query.filter_by(Id=Id, fieldId=session['field_id']).first()
      return render_template('mapping.html',rows=select,row=select2,total=total,avg=avg, edit=0)

    return render_template('mapping.html',rows=select,total=total,avg=avg, edit=None)
  return render_template('mapping.html',rows=select, edit=None)

def Round(a, b):
  if (a / b) == 0.5:
    return 1
  return round(b)
def Counter(a):
  if a>=0:
    return 1
  else:
    return 0
def Round1(a):
  if a - round(a)==.5:
    return round(a+.1)
  else:
   return round(a)

def Average(a,b):
  if a>=1.14 and b==1:
    return 1
  elif a>=2.28 and b==2:
    return 1
  elif a>=3.42 and b==3:
    return 1
  elif a>=47.6 and b==4:
    return 1
  elif a>=34 and b==5:
    return 1
  elif a>=7 and b==6:
    return 1
  elif a>=10 and b==7:
    return 1
  else:
    return 0
def Percentage(a,b):
  if b>0:
    return round((a/b),2)*100
  else:
    return 0
def Level(a):
  if a in range(1,50):
    return 1
  elif a in range (50,70):
    return 2
  elif a>=70:
    return 3
  else: 
    return 0
i=0


@app.route('/test1',methods=['GET','POST'])
def test1():
      # Check Login Fieil Id
    if 'user_id' in session :
      pass
    else:
      return redirect('/login')
    if 'field_id' in session:
      pass
    else:
      return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)

    total = {'co1_1':0,'co1_2':0,'co1_3':0,'co2_1':0,'co2_2':0,'co2_3':0,'co3_1':0,'co3_2':0,'co3_3':0,'co3_4':0,'co3_5':0}
    avg = {'co1_1':0,'co1_2':0,'co1_3':0,'co2_1':0,'co2_2':0,'co2_3':0,'co3_1':0,'co3_2':0,'co3_3':0,'co3_4':0,'co3_5':0}
    per = {'co1_1':0,'co1_2':0,'co1_3':0,'co2_1':0,'co2_2':0,'co2_3':0,'co3_1':0,'co3_2':0,'co3_3':0,'co3_4':0,'co3_5':0}
    att_per={'co1':0,'co2':0,'co3':0}
    level={'co1':0,'co2':0,'co3':0}
    codes = Comapping.query.filter_by(fieldId=session['field_id']).all()
    inp_rollno=[]
    rollnos=[]
    present=[]
    ids=[]
    names=[]
    count = 0
    for rows in codes:
     count+=1
    if count<5:
      return render_template('validation.html',message="Fill the remaining data or first check the CO attainment page", serverSite=True)
    entries=Test1.query.filter_by(fieldId=session["field_id"]).all()
    select = Studentlist.query.filter_by(fieldId=session["field_id"]).all()
    if select!=[]:
      for rn in select:
        rollnos.append(rn.rollNo)
        names.append(rn.studentsName)
        ids.append(rn.Id)
      if entries!=[]:
        for rn in entries:
          present.append(rn.rollNo)
        rn=rollnos.index(present[-1])
        if rn+1 < len(rollnos):
          rollno=rollnos[rn+1]
          name=names[rn+1]
          s_id=[rn+2]
        else:
          rollno=0
      else:
        rollno=rollnos[0]
        name=names[0]
        s_id=ids[0]
        rn=-1
    else:
      return render_template('validation.html',message="Please Upload Student List", serverSite=True)

    get_entry=Test1.query.filter_by(fieldId=session["field_id"]).all()
    if get_entry!=[]:
      for row in get_entry:
       # Getting attempted count
         total["co1_1"]+=Counter(row.CO1_1) 
         total["co1_2"]+=Counter(row.CO1_2)
         total["co1_3"]+=Counter(row.CO1_3)
         total["co2_1"]+=Counter(row.CO2_1)
         total["co2_2"]+=Counter(row.CO2_2)
         total["co2_3"]+=Counter(row.CO2_3)
         total["co3_1"]+=Counter(row.CO3_1)
         total["co3_2"]+=Counter(row.CO3_2)
         total["co3_3"]+=Counter(row.CO3_3)
         total["co3_4"]+=Counter(row.CO3_4)
         total["co3_5"]+=Counter(row.CO3_5)
      # Getting more thn average count
         avg["co1_1"]+=Average(row.CO1_1,1)
         avg["co1_2"]+=Average(row.CO1_2,1)
         avg["co1_3"]+=Average(row.CO1_3,1)
         avg["co2_1"]+=Average(row.CO2_1,1)
         avg["co2_2"]+=Average(row.CO2_2,1)
         avg["co2_3"]+=Average(row.CO2_3,1)
         avg["co3_1"]+=Average(row.CO3_1,2)
         avg["co3_2"]+=Average(row.CO3_2,2)
         avg["co3_3"]+=Average(row.CO3_3,2)
         avg["co3_4"]+=Average(row.CO3_4,2)
         avg["co3_5"]+=Average(row.CO3_5,2)
    # Getting percentage of more than avg
      per["co1_1"]=Percentage(avg["co1_1"],total["co1_1"])
      per["co1_2"]=Percentage(avg["co1_2"],total["co1_2"])
      per["co1_3"]=Percentage(avg["co1_3"],total["co1_3"])
      per["co2_1"]=Percentage(avg["co2_1"],total["co2_1"])
      per["co2_2"]=Percentage(avg["co2_2"],total["co2_2"])
      per["co2_3"]=Percentage(avg["co2_3"],total["co2_3"])
      per["co3_1"]=Percentage(avg["co3_1"],total["co3_1"])
      per["co3_2"]=Percentage(avg["co3_2"],total["co3_2"])
      per["co3_3"]=Percentage(avg["co3_3"],total["co3_3"])
      per["co3_4"]=Percentage(avg["co3_4"],total["co3_4"])
      per["co3_5"]=Percentage(avg["co3_5"],total["co3_5"])
    # Getting attainment percentage 
      att_per["co1"]=round(((per["co1_1"]+per["co1_2"]+per["co1_3"])/3),2)
      att_per["co2"]=round(((per["co2_1"]+per["co2_2"]+per["co3_3"])/3),2)
      att_per["co3"]=round(((per["co3_1"]+per["co3_2"]+per["co3_3"]+per["co3_4"]+per["co3_5"])/5),2)
      #Getting levels
      level["co1"]=Level(att_per["co1"])
      level["co2"]=Level(att_per["co2"])
      level["co3"]=Level(att_per["co3"])
    ## Collecing row data ##
    if(request.method=="POST"):
       entries=Test1.query.filter_by(fieldId=session["field_id"]).all()
       for row in entries:
         if row.StudentName in request.form:
           inp_rollno.append(Test1.query.filter_by(StudentName=row.StudentName,fieldId=session["field_id"]).first())
       if inp_rollno!=[]:
        for inp in inp_rollno: 
         for i in range(1,12):
            update=request.form.get(str(inp.rollNo)+str(i))
            if update!= "":
             present=Test1.query.filter_by(rollNo=inp.rollNo,fieldId=session["field_id"]).first()
             if i==1:
              present.CO1_1=update
             elif i==2:
              present.CO1_2=update
             elif i==3:
              present.CO1_3=update
             elif i==4:
              present.CO2_1=update
             elif i==5:
              present.CO2_2=update
             elif i==6:
              present.CO2_3=update
             elif i==7:
              present.CO3_1=update
             elif i==8:
              present.CO3_2=update
             elif i==9:
              present.CO3_3=update
             elif i==10:
              present.CO3_4=update
             elif i==11:
              present.CO3_5=update
             db.session.commit()
            else:
              pass
        return redirect('/test1')
       elif "entry" in request.form:
          total = {'co1_1':0,'co1_2':0,'co1_3':0,'co2_1':0,'co2_2':0,'co2_3':0,'co3_1':0,'co3_2':0,'co3_3':0,'co3_4':0,'co3_5':0}
          avg = {'co1_1':0,'co1_2':0,'co1_3':0,'co2_1':0,'co2_2':0,'co2_3':0,'co3_1':0,'co3_2':0,'co3_3':0,'co3_4':0,'co3_5':0}
          per = {'co1_1':0,'co1_2':0,'co1_3':0,'co2_1':0,'co2_2':0,'co2_3':0,'co3_1':0,'co3_2':0,'co3_3':0,'co3_4':0,'co3_5':0}
          att_per={'co1':0,'co2':0,'co3':0}
          level={'co1':0,'co2':0,'co3':0}
          co1_1=request.form.get("co1.1")
          co1_2=request.form.get("co1.2")
          co1_3=request.form.get("co1.3")
          co2_1=request.form.get("co2.1")
          co2_2=request.form.get("co2.2")
          co2_3=request.form.get("co2.3")
          co3_1=request.form.get("co3.1")
          co3_2=request.form.get("co3.2")
          co3_3=request.form.get("co3.3")
          co3_4=request.form.get("co3.4")
          co3_5=request.form.get("co3.5")
          cos=Test1(
          rollNo=rollno,
          StudentName=name,
          CO1_1=co1_1,
          CO1_2=co1_2,
          CO1_3=co1_3,
          CO2_1=co2_1,
          CO2_2=co2_2,
          CO2_3=co2_3,
          CO3_1=co3_1,
          CO3_2=co3_2,
          CO3_3=co3_3,
          CO3_4=co3_4,
          CO3_5=co3_5,
          fieldId=session['field_id']
          )
          ## Storing data in DB  ##
          db.session.add(cos)
          db.session.commit()
          time.sleep(1)
          entries=Test1.query.filter_by(fieldId=session["field_id"]).all()
          for row in entries:
            # Getting attempted count
              total["co1_1"]+=Counter(row.CO1_1) 
              total["co1_2"]+=Counter(row.CO1_2)
              total["co1_3"]+=Counter(row.CO1_3)
              total["co2_1"]+=Counter(row.CO2_1)
              total["co2_2"]+=Counter(row.CO2_2)
              total["co2_3"]+=Counter(row.CO2_3)
              total["co3_1"]+=Counter(row.CO3_1)
              total["co3_2"]+=Counter(row.CO3_2)
              total["co3_3"]+=Counter(row.CO3_3)
              total["co3_4"]+=Counter(row.CO3_4)
              total["co3_5"]+=Counter(row.CO3_5)
                    # Getting more thn average count
              avg["co1_1"]+=Average(row.CO1_1,1)
              avg["co1_2"]+=Average(row.CO1_2,1)
              avg["co1_3"]+=Average(row.CO1_3,1)
              avg["co2_1"]+=Average(row.CO2_1,1)
              avg["co2_2"]+=Average(row.CO2_2,1)
              avg["co2_3"]+=Average(row.CO2_3,1)
              avg["co3_1"]+=Average(row.CO3_1,2)
              avg["co3_2"]+=Average(row.CO3_2,2)
              avg["co3_3"]+=Average(row.CO3_3,2)
              avg["co3_4"]+=Average(row.CO3_4,2)
              avg["co3_5"]+=Average(row.CO3_5,2)
        #  Getting percentage of more than avg
          per["co1_1"]=Percentage(avg["co1_1"],total["co1_1"])
          per["co1_2"]=Percentage(avg["co1_2"],total["co1_2"])
          per["co1_3"]=Percentage(avg["co1_3"],total["co1_3"])
          per["co2_1"]=Percentage(avg["co2_1"],total["co2_1"])
          per["co2_2"]=Percentage(avg["co2_2"],total["co2_2"])
          per["co2_3"]=Percentage(avg["co2_3"],total["co2_3"])
          per["co3_1"]=Percentage(avg["co3_1"],total["co3_1"])
          per["co3_2"]=Percentage(avg["co3_2"],total["co3_2"])
          per["co3_3"]=Percentage(avg["co3_3"],total["co3_3"])
          per["co3_4"]=Percentage(avg["co3_4"],total["co3_4"])
          per["co3_5"]=Percentage(avg["co3_5"],total["co3_5"])
        # Getting attainment percentage 
          att_per["co1"]=round(((per["co1_1"]+per["co1_2"]+per["co1_3"])/3),2)
          att_per["co2"]=round(((per["co2_1"]+per["co2_2"]+per["co3_3"])/3),2)
          att_per["co3"]=round(((per["co3_1"]+per["co3_2"]+per["co3_3"]+per["co3_4"]+per["co3_5"])/5),2)
          #Getting levels
          level["co1"]=Level(att_per["co1"])
          level["co2"]=Level(att_per["co2"])
          level["co3"]=Level(att_per["co3"])
          entries=Test1.query.filter_by(fieldId=session["field_id"]).all()
          if entries!=[]:
             load=TotalTest1.query.filter_by(fieldId=session["field_id"]).all()
             if load!=[]:
                load=TotalTest1.query.filter_by(fieldId=session["field_id"]).first()
                load.Total_CO1_1=total["co1_1"]
                load.Total_CO1_2=total["co1_2"]
                load.Total_CO1_3=total["co1_3"]
                load.Total_CO2_1=total["co2_1"]
                load.Total_CO2_2=total["co2_2"]
                load.Total_CO2_3=total["co2_3"]
                load.Total_CO3_1=total["co3_1"]
                load.Total_CO3_2=total["co3_2"]
                load.Total_CO3_3=total["co3_3"]
                load.Total_CO3_4=total["co3_4"]
                load.Total_CO3_5=total["co3_5"]
                load.CO1_Level=level["co1"]
                load.CO2_Level=level["co2"]
                load.CO3_Level=level["co3"]
                load.fieldId=session["field_id"]
                db.session.commit()
             else:
              total_entry=TotalTest1(
              Total_CO1_1=total["co1_1"],
              Total_CO1_2=total["co1_2"],
              Total_CO1_3=total["co1_3"],
              Total_CO2_1=total["co2_1"],
              Total_CO2_2=total["co2_2"],
              Total_CO2_3=total["co2_3"],
              Total_CO3_1=total["co3_1"],
              Total_CO3_2=total["co3_2"],
              Total_CO3_3=total["co3_3"],
              Total_CO3_4=total["co3_4"],
              Total_CO3_5=total["co3_5"],
              CO1_Level=level["co1"],
              CO2_Level=level["co2"],
              CO3_Level=level["co3"],
              fieldId=session['field_id']
              )
              db.session.add(total_entry)
              db.session.commit()
          if (rn+2)<len(rollnos):
            return render_template('test1.html',codes=codes,level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=rollnos[rn+2],name=names[rn+2],id=ids[rn+2])
          else:
            return render_template('test1.html',codes=codes,level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=0)
    if rollno==0:
      return render_template('test1.html',codes=codes,level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=0)      
    if request.method=="GET":
      return render_template('test1.html',codes=codes,level=level,att_per=att_per,total=total,rows=entries,avg=avg,per=per,rollno=rollno,name=name,id=s_id)


@app.route('/test2',methods=['GET','POST'])
def test2():
   # Check Login Fieil Id
  if 'user_id' in session :
      pass
  else:
      return redirect('/login')
  if 'field_id' in session:
      pass
  else:
      return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)

  total = {'co4_1':0,'co4_2':0,'co4_3':0,'co4_4':0,'co5_1':0,'co5_2':0,'co4_5':0,'co5_3':0,'co5_4':0,'co5_5':0}
  avg = {'co4_1':0,'co4_2':0,'co4_3':0,'co4_4':0,'co5_1':0,'co5_2':0,'co4_5':0,'co5_3':0,'co5_4':0,'co5_5':0}
  per = {'co4_1':0,'co4_2':0,'co4_3':0,'co4_4':0,'co5_1':0,'co5_2':0,'co4_5':0,'co5_3':0,'co5_4':0,'co5_5':0}
  att_per={'co4':0,'co5':0}
  level={'co4':0,'co5':0}
  inp_rollno=[]
  rollnos=[]
  present=[]
  ids=[]
  names=[]
  codes = Comapping.query.filter_by(fieldId=session['field_id']).all()
  count = 0
  for rows in codes:
    count+=1
  if count<5:
    return render_template('validation.html',message="Fill the remaining data or first check the CO attainment page", serverSite=True)
  entries=Test2.query.filter_by(fieldId=session["field_id"]).all()
  select = Studentlist.query.filter_by(fieldId=session["field_id"]).all()
  if select!=[]:
      for rn in select:
        rollnos.append(rn.rollNo)
        names.append(rn.studentsName)
        ids.append(rn.Id)
      if entries!=[]:
        for rn in entries:
          present.append(rn.rollNo)
        rn=rollnos.index(present[-1])
        if rn+1 < len(rollnos):
          rollno=rollnos[rn+1]
          name=names[rn+1]
          s_id=[rn+2]
        else:
         rollno=0
      else:
        rollno=rollnos[0]
        name=names[0]
        s_id=ids[0]
        rn=-1
  else:
        return render_template('validation.html',message="Please Upload Student List", serverSite=True)

  get_entry=Test2.query.filter_by(fieldId=session["field_id"]).all()
  if get_entry!=[]:
      for row in get_entry:
       # Getting attempted count
         total["co4_1"]+=Counter(row.CO4_1) 
         total["co4_2"]+=Counter(row.CO4_2)
         total["co4_3"]+=Counter(row.CO4_3)
         total["co4_4"]+=Counter(row.CO4_4)
         total["co5_1"]+=Counter(row.CO5_1)
         total["co5_2"]+=Counter(row.CO5_2)
         total["co4_5"]+=Counter(row.CO4_5)
         total["co5_3"]+=Counter(row.CO5_3)
         total["co5_4"]+=Counter(row.CO5_4)
         total["co5_5"]+=Counter(row.CO5_5)
      # Getting more thn average count
         avg["co4_1"]+=Average(row.CO4_1,1)
         avg["co4_2"]+=Average(row.CO4_2,1)
         avg["co4_3"]+=Average(row.CO4_3,1)
         avg["co4_4"]+=Average(row.CO4_4,1)
         avg["co5_1"]+=Average(row.CO5_1,1)
         avg["co5_2"]+=Average(row.CO5_2,1)
         avg["co4_5"]+=Average(row.CO4_5,3)
         avg["co5_3"]+=Average(row.CO5_3,3)
         avg["co5_4"]+=Average(row.CO5_4,3)
         avg["co5_5"]+=Average(row.CO5_5,3)
    # Getting percentage of more than avg
      per["co4_1"]=Percentage(avg["co4_1"],total["co4_1"])
      per["co4_2"]=Percentage(avg["co4_2"],total["co4_2"])
      per["co4_3"]=Percentage(avg["co4_3"],total["co4_3"])
      per["co4_4"]=Percentage(avg["co4_4"],total["co4_4"])
      per["co5_1"]=Percentage(avg["co5_1"],total["co5_1"])
      per["co5_2"]=Percentage(avg["co5_2"],total["co5_2"])
      per["co4_5"]=Percentage(avg["co4_5"],total["co4_5"])
      per["co5_3"]=Percentage(avg["co5_3"],total["co5_3"])
      per["co5_4"]=Percentage(avg["co5_4"],total["co5_4"])
      per["co5_5"]=Percentage(avg["co5_5"],total["co5_5"])
    # Getting attainment percentage 
      att_per["co4"]=round(((per["co4_1"]+per["co4_2"]+per["co4_3"]+per["co4_4"]+per["co4_5"])/5),2)
      att_per["co5"]=round(((per["co5_1"]+per["co5_2"]+per["co5_3"]+per["co5_4"]+per["co5_5"])/5),2)
      #Getting levels
      level["co4"]=Level(att_per["co4"])
      level["co5"]=Level(att_per["co5"])
    ## Collecing row data ##
  if(request.method=="POST"):
    entries=Test2.query.filter_by(fieldId=session["field_id"]).all()
    for row in entries:
         if row.StudentName in request.form:
           inp_rollno.append(Test2.query.filter_by(StudentName=row.StudentName,fieldId=session["field_id"]).first())
    if inp_rollno!=[]:
        for inp in inp_rollno: 
          for i in range(1,11):
            update=request.form.get(str(inp.rollNo)+str(i))
            if update!= "":
             present=Test2.query.filter_by(rollNo=inp.rollNo,fieldId=session["field_id"]).first()
             if i==1:
              present.CO4_1=update
             elif i==2:
              present.CO4_2=update
             elif i==3:
              present.CO4_3=update
             elif i==4:
              present.CO4_4=update
             elif i==5:
              present.CO5_1=update
             elif i==6:
              present.CO4_5=update
             elif i==7:
              present.CO5_1=update
             elif i==8:
              present.CO5_2=update
             elif i==9:
              present.CO5_3=update
             elif i==10:
              present.CO5_4=update
             db.session.commit()
            else:
              pass
        return redirect('/test2')
    elif "entry" in request.form:
     total = {'co4_1':0,'co4_2':0,'co4_3':0,'co4_4':0,'co5_1':0,'co5_2':0,'co4_5':0,'co5_3':0,'co5_4':0,'co5_5':0}
     avg = {'co4_1':0,'co4_2':0,'co4_3':0,'co4_4':0,'co5_1':0,'co5_2':0,'co4_5':0,'co5_3':0,'co5_4':0,'co5_5':0}
     per = {'co4_1':0,'co4_2':0,'co4_3':0,'co4_4':0,'co5_1':0,'co5_2':0,'co4_5':0,'co5_3':0,'co5_4':0,'co5_5':0}
     att_per={'co4':0,'co5':0}
     level={'co4':0,'co5':0}
     co4_1=request.form.get("co4_1")
     co4_2=request.form.get("co4_2")
     co4_3=request.form.get("co4_3")
     co4_4=request.form.get("co4_4")
     co5_1=request.form.get("co5_1")
     co5_2=request.form.get("co5_2")
     co4_5=request.form.get("co4_5")
     co5_3=request.form.get("co5_3")
     co5_4=request.form.get("co5_4")
     co5_5=request.form.get("co5_5")
     cos=Test2(
     rollNo=rollno,
     StudentName=name,
     CO4_1=co4_1,
     CO4_2=co4_2,
     CO4_3=co4_3,
     CO4_4=co4_4,
     CO5_1=co5_1,
     CO5_2=co5_2,
     CO4_5=co4_5,
     CO5_3=co5_3,
     CO5_4=co5_4,
     CO5_5=co5_5,
     fieldId=session['field_id']
     )
     ## Storing data in DB  ##
     db.session.add(cos)
     db.session.commit()
     time.sleep(1)
     entries=Test2.query.filter_by(fieldId=session["field_id"]).all()
     for row in entries:
       # Getting attempted count
         total["co4_1"]+=Counter(row.CO4_1) 
         total["co4_2"]+=Counter(row.CO4_2)
         total["co4_3"]+=Counter(row.CO4_3)
         total["co4_4"]+=Counter(row.CO4_4)
         total["co5_1"]+=Counter(row.CO5_1)
         total["co5_2"]+=Counter(row.CO5_2)
         total["co4_5"]+=Counter(row.CO4_5)
         total["co5_3"]+=Counter(row.CO5_3)
         total["co5_4"]+=Counter(row.CO5_4)
         total["co5_5"]+=Counter(row.CO5_5)
     # Getting more thn average count
         avg["co4_1"]+=Average(row.CO4_1,1)
         avg["co4_2"]+=Average(row.CO4_2,1)
         avg["co4_3"]+=Average(row.CO4_3,1)
         avg["co4_4"]+=Average(row.CO4_4,1)
         avg["co5_1"]+=Average(row.CO5_1,1)
         avg["co5_2"]+=Average(row.CO5_2,1)
         avg["co4_5"]+=Average(row.CO4_5,3)
         avg["co5_3"]+=Average(row.CO5_3,3)
         avg["co5_4"]+=Average(row.CO5_4,3)
         avg["co5_5"]+=Average(row.CO5_5,3)
    # Getting percentage of more than avg
     per["co4_1"]=Percentage(avg["co4_1"],total["co4_1"])
     per["co4_2"]=Percentage(avg["co4_2"],total["co4_2"])
     per["co4_3"]=Percentage(avg["co4_3"],total["co4_3"])
     per["co4_4"]=Percentage(avg["co4_4"],total["co4_4"])
     per["co5_1"]=Percentage(avg["co5_1"],total["co5_1"])
     per["co5_2"]=Percentage(avg["co5_2"],total["co5_2"])
     per["co4_5"]=Percentage(avg["co4_5"],total["co4_5"])
     per["co5_3"]=Percentage(avg["co5_3"],total["co5_3"])
     per["co5_4"]=Percentage(avg["co5_4"],total["co5_4"])
     per["co5_5"]=Percentage(avg["co5_5"],total["co5_5"])
    # Getting attainment percentage 
     att_per["co4"]=round(((per["co4_1"]+per["co4_2"]+per["co4_3"]+per["co4_4"]+per["co4_5"])/5),2)
     att_per["co5"]=round(((per["co5_1"]+per["co5_2"]+per["co5_3"]+per["co5_4"]+per["co5_5"])/5),2)
    # Getting levels
     level["co4"]=Level(att_per["co4"])
     level["co5"]=Level(att_per["co5"])
     if entries!=[]:
      load=TotalTest2.query.filter_by(fieldId=session["field_id"]).all()
      if load!=[]:
          load=TotalTest2.query.first()
          load.Total_CO4_1=total["co4_1"]
          load.Total_CO4_2=total["co4_2"]
          load.Total_CO4_3=total["co4_3"]
          load.Total_CO4_4=total["co4_4"]
          load.Total_CO5_1=total["co5_1"]
          load.Total_CO5_2=total["co5_2"]
          load.Total_CO4_5=total["co4_5"]
          load.Total_CO5_3=total["co5_3"]
          load.Total_CO5_4=total["co5_4"]
          load.Total_CO5_5=total["co5_5"]
          load.CO4_Level=level["co4"]
          load.CO5_Level=level["co5"]
          load.fieldId=session["field_id"]
          db.session.commit()
      else:
          total_entry=TotalTest2(
          Total_CO4_1=total["co4_1"],
          Total_CO4_2=total["co4_2"],
          Total_CO4_3=total["co4_3"],
          Total_CO4_4=total["co4_4"],
          Total_CO5_1=total["co5_1"],
          Total_CO5_2=total["co5_2"],
          Total_CO4_5=total["co4_5"],
          Total_CO5_3=total["co5_3"],
          Total_CO5_4=total["co5_4"],
          Total_CO5_5=total["co5_5"],
          CO4_Level=level["co4"],
          CO5_Level=level["co5"],
          fieldId=session['field_id']
          )
          db.session.add(total_entry)
          db.session.commit()
      if (rn+2)<len(rollnos):
       return render_template('test2.html',codes=codes,level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=rollnos[rn+2],name=names[rn+2],id=ids[rn+2])
      else:
       return render_template('test2.html',codes=codes,level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=0)
  if rollno==0:
    return render_template('test2.html',codes=codes,level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=0)
  if request.method=="GET":
        return render_template('test2.html',codes=codes,level=level,att_per=att_per,total=total,rows=entries,avg=avg,per=per,rollno=rollno,name=name,id=s_id)

@app.route('/msbte',methods=['GET','POST'])
def msbte():
  # Check Login Fieil Id
    if 'user_id' in session :
      pass
    else:
      return redirect('/login')
    if 'field_id' in session:
      pass
    else:
      return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)

    total={'th':0,'pr':0}
    avg={'th':0,'pr':0}
    per={'th':0,'pr':0}
    level={'th':0,'pr':0}
    inp_rollno=[]
    rollnos=[]
    present=[]
    ids=[]
    names=[]
    entries=Msbte.query.filter_by(fieldId=session["field_id"]).all()
    select = Studentlist.query.filter_by(fieldId=session["field_id"]).all()
    if select!=[]:
      for rn in select:
        rollnos.append(rn.rollNo)
        names.append(rn.studentsName)
        ids.append(rn.Id)
      if entries!=[]:
        for rn in entries:
          present.append(rn.rollNo)
        rn=rollnos.index(present[-1])
        if rn+1 < len(rollnos):
          rollno=rollnos[rn+1]
          name=names[rn+1]
          s_id=[rn+2]
        else:
          rollno=0
      else:
        rollno=rollnos[0]
        name=names[0]
        s_id=ids[0]
        rn=-1
    else:
      return render_template('validation.html',message="Please Upload Student List", serverSite=True)
    
    for row in entries:
        total["th"]+=Counter(row.TH)
        total["pr"]+=Counter(row.PR)
        avg["th"]+=Average(row.TH,4)
        avg["pr"]+=Average(row.PR,5)
    per["th"]=Percentage(avg["th"],total["th"])
    per["pr"]=Percentage(avg["pr"],total["pr"])
    level["th"]=Level(per["th"])
    level["pr"]=Level(per["pr"])
    if request.method=="POST":
     entries=Msbte.query.filter_by(fieldId=session["field_id"]).all()
     for row in entries:
         if row.StudentName in request.form:
           inp_rollno.append(Msbte.query.filter_by(StudentName=row.StudentName,fieldId=session["field_id"]).first())
     if inp_rollno!=[]:
        for inp in inp_rollno: 
          for i in range(1,12):
            update=request.form.get(str(inp.rollNo)+str(i))
            if update!= "":
             present=Msbte.query.filter_by(rollNo=inp.rollNo,fieldId=session["field_id"]).first()
             if i==1:
              present.TH=update
             elif i==2:
              present.PR=update
             db.session.commit()
            else:
              pass
        return redirect('/msbte')
     elif "entry" in request.form:
      total={'th':0,'pr':0}
      avg={'th':0,'pr':0}
      per={'th':0,'pr':0}
      level={'th':0,'pr':0}
      th=request.form.get("th")
      pr=request.form.get("pr")
      enter=Msbte(
        rollNo=rollno,
        StudentName=name,
        TH=th,
        PR=pr,
        fieldId=session["field_id"]
      )
      db.session.add(enter)
      db.session.commit()
      entries=Msbte.query.filter_by(fieldId=session["field_id"]).all()
      for row in entries:
        total["th"]+=Counter(row.TH)
        total["pr"]+=Counter(row.PR)
        avg["th"]+=Average(row.TH,4)
        avg["pr"]+=Average(row.PR,5)
      per["th"]=Percentage(avg["th"],total["th"])
      per["pr"]=Percentage(avg["pr"],total["pr"])
      level["th"]=Level(per["th"])
      level["pr"]=Level(per["pr"])
      if entries!=[]:
       load=Total_msbte.query.filter_by(fieldId=session["field_id"]).all()
       if load!=[]:
          load=Total_msbte.query.filter_by(fieldId=session["field_id"]).first()
          load.Total_TH=total["th"]
          load.Total_PR=total["pr"]
          load.TH_Level=level["th"]
          load.PR_Level=level["pr"]
          load.fieldId=session["field_id"]
          db.session.commit()
       else:
          total_entry=Total_msbte(
          Total_TH=total["th"],
          Total_PR=total["pr"],
          TH_Level=level["th"],
          PR_Level=level["pr"],
          fieldId=session['field_id']
          )
          db.session.add(total_entry)
          db.session.commit()
      if (rn+2)<len(rollnos):
       return render_template('msbte.html',level=level,total=total,avg=avg,per=per,rows=entries,rollno=rollnos[rn+2],name=names[rn+2],id=ids[rn+2])
      else:
       return render_template('msbte.html',level=level,total=total,avg=avg,per=per,rows=entries,rollno=0)
    if rollno==0:
      return render_template('msbte.html',level=level,total=total,avg=avg,per=per,rows=entries,rollno=0)
    if request.method=="GET":
     return render_template('msbte.html',rows=entries,level=level,total=total,avg=avg,per=per,rollno=rollno,name=name,id=s_id)

@app.route('/prpa',methods=['GET','POST'])
def prpa():
  # Check Login Fieil Id
    if 'user_id' in session :
      pass
    else:
      return redirect('/login')
    if 'field_id' in session:
      pass
    else:
      return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)

    Practical = {'co1':0,'co2':0,'co3':0,'co4':0,'co5':0,'total':0}
    Prac_avg = {'co1':0,'co2':0,'co3':0,'co4':0,'co5':0,'total':0}
    Prac_max = {'co1':0,'co2':0,'co3':0,'co4':0,'co5':0,'total':0}
    total = {'co1':0,'co2':0,'co3':0,'co4':0,'co5':0,'total':0}
    avg = {'co1':0,'co2':0,'co3':0,'co4':0,'co5':0}
    per ={'co1':0,'co2':0,'co3':0,'co4':0,'co5':0}
    level={'co1':0,'co2':0,'co3':0,'co4':0,'co5':0}
    test=Practical_prpa.query.filter_by(fieldId=session["field_id"]).first()
    rollnos=[]
    inp_rollno=[]
    present=[]
    fetch=[]
    ids=[]
    names=[]
    codes = Comapping.query.filter_by(fieldId=session['field_id']).all()
    count = 0
    for rows in codes:
      count+=1
    if count<5:
      return render_template('validation.html',message="Fill the remaining data or first check the CO attainment page", serverSite=True)
    select=Studentlist.query.filter_by(fieldId=session["field_id"]).all()
    entries=Prpa.query.filter_by(fieldId=session["field_id"]).all()
    if select!=[]:
      for rn in select:
        rollnos.append(rn.rollNo)
        names.append(rn.studentsName)
        ids.append(rn.Id)
      if entries!=[]:
        for rn in entries:
          present.append(rn.rollNo)
        rn=rollnos.index(present[-1])
        if rn+1 < len(rollnos):
          rollno=rollnos[rn+1]
          name=names[rn+1]
          s_id=[rn+2]
        else:
         rollno=0
      else:
        rollno=rollnos[0]
        name=names[0]
        s_id=ids[0]
        rn=-1
    else:
      return render_template('validation.html',message="Please Upload Student List", serverSite=True)

    practical=Practical_prpa.query.filter_by(fieldId=session["field_id"]).first()
    if practical!=None:
       Practical["co1"]=practical.CO1
       Practical["co2"]=practical.CO2
       Practical["co3"]=practical.CO3
       Practical["co4"]=practical.CO4
       Practical["co5"]=practical.CO5
       Practical["total"]=int(Practical["co1"])+int(Practical["co2"])+int(Practical["co3"])+int(Practical["co4"])+int(Practical["co5"])
       Prac_avg["co1"]=round(((Practical["co1"]/Practical["total"])*100),2)
       Prac_avg["co2"]=round(((Practical["co2"]/Practical["total"])*100),2)
       Prac_avg["co3"]=round(((Practical["co3"]/Practical["total"])*100),2)
       Prac_avg["co4"]=round(((Practical["co4"]/Practical["total"])*100),2)
       Prac_avg["co5"]=round(((Practical["co5"]/Practical["total"])*100),2)
       Prac_avg["total"]=Prac_avg["co1"]+Prac_avg["co2"]+Prac_avg["co3"]+Prac_avg["co4"]+Prac_avg["co5"]
       Prac_max["co1"]=Round1(((int(Prac_avg["co1"])/100)*50))
       Prac_max["co2"]=Round1(((int(Prac_avg["co2"])/100)*50))
       Prac_max["co3"]=Round1(((int(Prac_avg["co3"])/100)*50))
       Prac_max["co4"]=Round1(((int(Prac_avg["co4"])/100)*50))
       Prac_max["co5"]=Round1(((int(Prac_avg["co5"])/100)*50))
       Prac_max["total"]=Prac_max["co1"]+Prac_max["co2"]+Prac_max["co3"]+Prac_max["co4"]+Prac_max["co5"]
    entries=Prpa.query.filter_by(fieldId=session["field_id"]).all()
    select = Studentlist.query.filter_by(fieldId=session["field_id"]).all()
    if entries!=[]:
      for row in entries:
        # Getting attempted count
          total["co1"]+=Counter(row.CO1) 
          total["co2"]+=Counter(row.CO2)
          total["co3"]+=Counter(row.CO3)
          total["co4"]+=Counter(row.CO4)
          total["co5"]+=Counter(row.CO5)
          total["total"]=row.CO1+row.CO2+row.CO3+row.CO4+row.CO5
      # Getting more thn average count
          avg["co1"]+=Average(row.CO1,6)
          avg["co2"]+=Average(row.CO2,6)
          avg["co3"]+=Average(row.CO3,7)
          avg["co4"]+=Average(row.CO4,6)
          avg["co5"]+=Average(row.CO5,7)
    #  Getting percentage of more than avg
      per["co1"]=Percentage(avg["co1"],total["co1"])
      per["co2"]=Percentage(avg["co2"],total["co2"])
      per["co3"]=Percentage(avg["co3"],total["co3"])
      per["co4"]=Percentage(avg["co4"],total["co4"])
      per["co5"]=Percentage(avg["co5"],total["co5"])
    #   Getting levels
      level["co1"]=Level(per["co1"])
      level["co2"]=Level(per["co2"])
      level["co3"]=Level(per["co3"])
      level["co4"]=Level(per["co4"])
      level["co5"]=Level(per["co5"])
    if request.method=="POST":
     if "add" in request.form:
       Practical["co1"]=request.form.get("prac1")
       Practical["co2"]=request.form.get("prac2")
       Practical["co3"]=request.form.get("prac3")
       Practical["co4"]=request.form.get("prac4")
       Practical["co5"]=request.form.get("prac5")
       Practical["total"]=int(Practical["co1"])+int(Practical["co2"])+int(Practical["co3"])+int(Practical["co4"])+int(Practical["co5"])
       pracs=Practical_prpa(
         CO1=Practical["co1"],
         CO2=Practical["co2"],
         CO3=Practical["co3"],
         CO4=Practical["co4"],
         CO5=Practical["co5"],
         Total=Practical["total"],
         fieldId=session['field_id']
       )
       db.session.add(pracs)
       db.session.commit()
       return redirect('/prpa')
       practical=Practical_prpa.query.filter_by(fieldId=session["field_id"]).first()
     else:
      entries=Prpa.query.filter_by(fieldId=session["field_id"]).all()
      for row in entries:
         if row.StudentName in request.form:
           inp_rollno.append(Prpa.query.filter_by(StudentName=row.StudentName,fieldId=session["field_id"]).first())
      if inp_rollno!=[]:
        for inp in inp_rollno: 
          for i in range(1,2):
            update=request.form.get(str(inp.rollNo)+str(i))
            if update!= "":
             present=Prpa.query.filter_by(rollNo=inp.rollNo,fieldId=session["field_id"]).first()
             if i==1:
              present.Marks_Obtained=update
              present.CO1=round((int(update)*(Prac_avg["co1"]/100)))
              present.CO2=round((int(update)*(Prac_avg["co2"]/100)))
              present.CO3=round((int(update)*(Prac_avg["co3"]/100)))
              present.CO4=round((int(update)*(Prac_avg["co4"]/100)))
              present.CO5=round((int(update)*(Prac_avg["co5"]/100)))
             db.session.commit()
            else:
              pass
        return redirect('/prpa')
      elif "entry" in request.form:
        total = {'co1':0,'co2':0,'co3':0,'co4':0,'co5':0}
        avg = {'co1':0,'co2':0,'co3':0,'co4':0,'co5':0}
        per ={'co1':0,'co2':0,'co3':0,'co4':0,'co5':0}
        level={'co1':0,'co2':0,'co3':0,'co4':0,'co5':0}
        marks=request.form.get("marks")
        co1=round((int(marks)*(Prac_avg["co1"]/100)))
        co2=round((int(marks)*(Prac_avg["co2"]/100)))
        co3=round((int(marks)*(Prac_avg["co3"]/100)))
        co4=round((int(marks)*(Prac_avg["co4"]/100)))
        co5=round((int(marks)*(Prac_avg["co5"]/100)))
        cos=Prpa(
        rollNo=rollno,
        StudentName=name,
        CO1=co1,
        CO2=co2,
        CO3=co3,
        CO4=co4,
        CO5=co5,
        Marks_Obtained=marks,
        fieldId=session['field_id']
        )
        ## Storing data in DB  ##
        db.session.add(cos)
        db.session.commit()
        time.sleep(1)
        entries=Prpa.query.filter_by(fieldId=session["field_id"]).all()
        practical=Practical_prpa.query.filter_by(fieldId=session["field_id"]).first() 
        for row in entries:
          # Getting attempted count
            total["co1"]+=Counter(row.CO1) 
            total["co2"]+=Counter(row.CO2)
            total["co3"]+=Counter(row.CO3)
            total["co4"]+=Counter(row.CO4)
            total["co5"]+=Counter(row.CO5)
        # Getting more thn average count
            avg["co1"]+=Average(row.CO1,6)
            avg["co2"]+=Average(row.CO2,6)
            avg["co3"]+=Average(row.CO3,7)
            avg["co4"]+=Average(row.CO4,6)
            avg["co5"]+=Average(row.CO5,7)
    #    Getting percentage of more than avg
        per["co1"]=Percentage(avg["co1"],total["co1"])
        per["co2"]=Percentage(avg["co2"],total["co2"])
        per["co3"]=Percentage(avg["co3"],total["co3"])
        per["co4"]=Percentage(avg["co4"],total["co4"])
        per["co5"]=Percentage(avg["co5"],total["co5"])
    #    Getting levels
        level["co1"]=Level(per["co1"])
        level["co2"]=Level(per["co2"])
        level["co3"]=Level(per["co3"])
        level["co4"]=Level(per["co4"])
        level["co5"]=Level(per["co5"])
        if entries!=[]:
         load=Total_prpa.query.filter_by(fieldId=session["field_id"]).all()
         if load!=[]:
             load=Total_prpa.query.first()
             load.Total_CO1=total["co1"]
             load.Total_CO2=total["co2"]
             load.Total_CO3=total["co3"]
             load.Total_CO4=total["co4"]
             load.Total_CO5=total["co5"]
             load.Level_CO1=level["co1"]
             load.Level_CO2=level["co2"]
             load.Level_CO3=level["co3"]
             load.Level_CO4=level["co4"]
             load.Level_CO5=level["co5"]
             load.fieldId=session["field_id"]
             db.session.commit()
         else:
             total_entry=Total_prpa(
             Total_CO1=total["co1"],
             Total_CO2=total["co2"],
             Total_CO3=total["co3"],
             Total_CO4=total["co4"],
             Total_CO5=total["co5"],
             Level_CO1=level["co1"],
             Level_CO2=level["co2"],
             Level_CO3=level["co3"],
             Level_CO4=level["co4"],
             Level_CO5=level["co5"],
             fieldId=session['field_id']
             )
             db.session.add(total_entry)
             db.session.commit()
             practical=Practical_prpa.query.filter_by(fieldId=session["field_id"]).first()
        if (rn+2)<len(rollnos):
          return render_template('prpa.html',codes=codes,practical=practical,level=level,total=total,avg=avg,per=per,\
          rows=entries,rollno=rollnos[rn+2],name=names[rn+2],id=ids[rn+2],Prac_avg=Prac_avg,Prac_max=Prac_max)
        else:
          return render_template('prpa.html',codes=codes,practical=practical,level=level,total=total,avg=avg,per=per,rows=entries,rollno=0,Prac_avg=Prac_avg,Prac_max=Prac_max)
    if rollno==0:
      return render_template('prpa.html',codes=codes,practical=practical,level=level,total=total,avg=avg,per=per,rows=entries,rollno=0,Prac_avg=Prac_avg,Prac_max=Prac_max)
    if request.method=="GET":
      return render_template('prpa.html',codes=codes,rows=entries,level=level,total=total,practical=practical, \
    avg=avg,per=per,rollno=rollno,name=name,id=s_id,Prac_avg=Prac_avg,Prac_max=Prac_max)



@app.route('/micro_project',methods=['GET','POST'])
def micro_project():
   # Check Login Fieil Id
  if 'user_id' in session :
    pass
  else:
    return redirect('/login')
  if 'field_id' in session:
    pass
  else:
    return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)

  select = Micro_project.query.filter_by(fieldId=session['field_id']).all()
  select2 = Micro_project.query.filter_by(fieldId=session['field_id']).all()
  select1 = Studentlist.query.filter_by(fieldId=session['field_id']).all() 
  select3=  Total_micro_project.query.filter_by(fieldId=session['field_id']).first()
  select4=  Total_micro_project.query.filter_by(fieldId=session['field_id']).all()
  select5 = Comapping.query.filter_by(fieldId=session['field_id']).all()
  count = len(select)
  counter=0
  Co1_Count=0
  Co2_Count=0
  Co3_Count=0
  Co4_Count=0
  Co5_Count=0
  totalMarks_Co1=0
  totalMarks_Co2=0
  totalMarks_Co3=0
  totalMarks_Co4=0
  totalMarks_Co5=0
  Co1_more_avg=0
  Co2_more_avg=0
  Co3_more_avg=0
  Co4_more_avg=0
  Co5_more_avg=0
  Co1_attainment=0
  Co2_attainment=0
  Co3_attainment=0
  Co4_attainment=0
  Co5_attainment=0
  Co1_per=0
  Co2_per=0
  Co3_per=0
  Co4_per=0
  Co5_per=0
  studentCount=0
  presentCount=0
  memCount=0
  vemCount=0
  forLength=0
  identifierfor=1
  identifier=[]
  for_identity=[]
  present=[]
  studentsenterna=[]
  studentsenterro=[]
  presentName=[]
  presentRoll=[]
  for row in select:
    studentCount+=1

  for row in select1:
    if memCount<studentCount:
      studentsenterna.append(row.studentsName)
      studentsenterro.append(row.rollNo)
      vemCount+=1
    memCount+=1 

  ##for the fullfillment of the list error out of index ((required not to be deleted)
  for i in range(0,1):
    presentName.append("")
    presentRoll.append(0)

  for row in select1:
    if vemCount==presentCount:
     presentName[0]=row.studentsName
     presentRoll[0]=row.rollNo
     break   
    presentCount+=1  

  if request.method == 'POST':
      identifierfor=request.form.get('Id')
      for_identity=Micro_project.query.filter_by(fieldId=session['field_id']).all()
      for rect in for_identity:
        if str(rect.Id) in request.form:
          identifier.append(Micro_project.query.filter_by(Id=rect.Id,fieldId=session["field_id"]).first())
      if identifier!=[]:
        for edits in identifier:
          present=Micro_project.query.filter_by(Id=edits.Id,fieldId=session["field_id"]).first()
          present.Co1=request.form.get(str(1)+str(present.Id))
          present.Co2=request.form.get(str(2)+str(present.Id))
          present.Co3=request.form.get(str(3)+str(present.Id))
          present.Co4=request.form.get(str(4)+str(present.Id))
          present.Co5=request.form.get(str(5)+str(present.Id))
          db.session.commit()
          
      if "entry" in request.form:  
          Co1 = request.form.get('co1')
          Co2 = request.form.get('co2')
          Co3 = request.form.get('co3')
          Co4 = request.form.get('co4')
          Co5 = request.form.get('co5')
          forLength=len(select)
          entry = Micro_project(
          Co1=Co1,
          Co2=Co2,
          Co3=Co3,
          Co4=Co4,
          Co5=Co5,
          fieldId = session['field_id'],
          )
          db.session.add(entry)
          db.session.commit()
      
      for row in select2:
       counter+=1
       if row.Co1!=-1:
         Co1_Count+=1 
         totalMarks_Co1=5+(row.Co1)
         if row.Co1>5: 
           Co1_more_avg+=1
       if row.Co2!=-1:
         Co2_Count+=1
         totalMarks_Co2=totalMarks_Co2+(row.Co2) 
         if row.Co2>5:
          Co2_more_avg+=1
       if row.Co3!=-1:
         Co3_Count+=1
         totalMarks_Co3=totalMarks_Co3+(row.Co3) 
         if row.Co3>5:
           Co3_more_avg+=1
       if row.Co4!=-1:
         Co4_Count+=1
         totalMarks_Co4=totalMarks_Co4+(row.Co4)
         if row.Co4>5:
           Co4_more_avg+=1
       if row.Co5!=-1:
         Co5_Count+=1
         totalMarks_Co5=totalMarks_Co5+(row.Co5)
         if row.Co5>5:
           Co5_more_avg+=1 
      if Co1_more_avg!=0:
       Co1_per =round((Co1_more_avg/Co1_Count)*100)
      if Co2_more_avg!=0: 
       Co2_per =round((Co2_more_avg/Co2_Count)*100)
      if Co3_more_avg!=0:
       Co3_per =round((Co3_more_avg/Co3_Count)*100)
      if Co4_more_avg!=0:
       Co4_per =round((Co4_more_avg/Co4_Count)*100)
      if Co5_more_avg!=0:
       Co5_per =round((Co5_more_avg/Co5_Count)*100)
    
      if Co1_per>1 and Co1_per<50:
        Co1_attainment=1
      elif Co1_per>49 and Co1_per<70:
        Co2_attainment=2 
      elif Co1_per>70:
        Co3_attainment=3
      else:
        Co4_attainment=0      

      if select3!=None:
       select3.nostudents_attempted_Co1=Co1_Count
       select3.nostudents_attempted_Co2=Co2_Count
       select3.nostudents_attempted_Co3=Co3_Count
       select3.nostudents_attempted_Co4=Co4_Count
       select3.nostudents_attempted_Co5=Co5_Count 
       select3.nostudents_more_than_avgMarks_Co1=Co1_more_avg 
       select3.nostudents_more_than_avgMarks_Co2=Co2_more_avg
       select3.nostudents_more_than_avgMarks_Co3=Co3_more_avg 
       select3.nostudents_more_than_avgMarks_Co4=Co4_more_avg
       select3.nostudents_more_than_avgMarks_Co5=Co5_more_avg
       select3.per_of_students_more_than_avgMarks_Co1=Co1_per
       select3.per_of_students_more_than_avgMarks_Co2=Co2_per
       select3.per_of_students_more_than_avgMarks_Co3=Co3_per
       select3.per_of_students_more_than_avgMarks_Co4=Co4_per
       select3.per_of_students_more_than_avgMarks_Co5=Co5_per
       select3.attainment_level_acheived_Co1=Co1_attainment
       select3.attainment_level_acheived_Co2=Co2_attainment
       select3.attainment_level_acheived_Co3=Co3_attainment
       select3.attainment_level_acheived_Co4=Co4_attainment
       select3.attainment_level_acheived_Co5=Co5_attainment
       db.session.commit()
      else:
       entry=Total_micro_project(
       nostudents_attempted_Co1=Co1_Count,
       nostudents_attempted_Co2=Co2_Count,
       nostudents_attempted_Co3=Co3_Count,
       nostudents_attempted_Co4=Co4_Count,
       nostudents_attempted_Co5=Co5_Count,
       nostudents_more_than_avgMarks_Co1=Co1_more_avg,
       nostudents_more_than_avgMarks_Co2=Co2_more_avg,
       nostudents_more_than_avgMarks_Co3=Co3_more_avg,
       nostudents_more_than_avgMarks_Co4=Co4_more_avg,
       nostudents_more_than_avgMarks_Co5=Co5_more_avg,
       per_of_students_more_than_avgMarks_Co1=Co1_per,
       per_of_students_more_than_avgMarks_Co2=Co2_per,
       per_of_students_more_than_avgMarks_Co3=Co3_per,
       per_of_students_more_than_avgMarks_Co4=Co4_per,
       per_of_students_more_than_avgMarks_Co5=Co5_per,
       attainment_level_acheived_Co1=Co1_attainment,
       attainment_level_acheived_Co2=Co2_attainment,
       attainment_level_acheived_Co3=Co3_attainment,
       attainment_level_acheived_Co4=Co4_attainment,
       attainment_level_acheived_Co5=Co5_attainment,
       fieldId = session['field_id'],
      )
       db.session.add(entry)
       db.session.commit()

      return redirect('/micro_project')
      
  return render_template('micro_project.html',rows=select,rows2=select4,rows3=select5,length=forLength,stuententerName=studentsenterna,studentsenterro=studentsenterro,studentPresentna=presentName,studentPresentro=presentRoll)
  
  

@app.route('/co_attainment',methods=['GET','POST'])
def co_attainment():
   # Check Login Fieil Id
  if 'user_id' in session :
    pass
  else:
    return redirect('/login')
  if 'field_id' in session:
    pass
  else:
    return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)

  select= Comapping.query.filter_by(fieldId=session['field_id']).all()
  select_test1=TotalTest1.query.filter_by(fieldId=session['field_id']).all()
  select_test2=TotalTest2.query.filter_by(fieldId=session['field_id']).all()
  select_mico = Total_micro_project.query.filter_by(fieldId=session['field_id']).all()
  select_msbte=Total_msbte.query.filter_by(fieldId=session['field_id']).all()
  select_prpa=Total_prpa.query.filter_by(fieldId=session['field_id']).all()
  select_attainment=Total_attainment.query.filter_by(fieldId=session['field_id']).first()
  attainment_class=[]
  attainment_prpa=[]
  attainment_internal=[]
  attainment_external=[]
  final_assesment=[]
  enternal=0
  external=0
  CO1_Level=0
  CO2_Level=0
  CO3_Level=0
  CO4_Level=0
  CO5_Level=0
  count=0
  for rows in select:
    count+=1
  if count<5:
      return render_template('validation.html',message="Fill the remaining data or first check the CO attainment page", serverSite=True)

  for i in range(1,6):
   if select_test1!=None:
     for rows in select_test1:
       if i==1:
          attainment_class.append(rows.CO1_Level)
       if i==2:
         attainment_class.append(rows.CO2_Level)
       if i==3:
         attainment_class.append(rows.CO3_Level)
     for rows in select_test2:   
       if i==4:
          attainment_class.append(rows.CO4_Level)
       if i==5:
          attainment_class.append(rows.CO5_Level) 
  for i in range(1,6):
   if select_prpa!=None:
     for rows in select_prpa:
       if i==1:
          attainment_prpa.append(rows.Level_CO1)
       if i==2:
         attainment_prpa.append(rows.Level_CO2)
       if i==3:
         attainment_prpa.append(rows.Level_CO3)  
       if i==4:
          attainment_prpa.append(rows.Level_CO4)
       if i==5:
          attainment_prpa.append(rows.Level_CO5)  
  for j in range(0,5):
    if attainment_class!=[] and attainment_prpa!=[]: 
      if attainment_class[j]!=None and attainment_prpa[j]!=None: 
         attainment_internal.append(Round1((attainment_class[j]+attainment_prpa[j])/2))
  if select_msbte!=None:  
    for row in select_msbte:
      attainment_external.append(Round1((row.TH_Level+row.PR_Level)/2)) 
  for k in range(0,5):
    if attainment_internal!=[] and attainment_external!=[]:
      enternal=int(attainment_internal[k])
      external=int(attainment_external[0])
      final_assesment.append(Round1((0.4*float(enternal))+(0.6*float(external)))) 
  if select_attainment!=[] and final_assesment!=[]: 
    for t in range(1,6): 
      if t==1:
        select_attainment.CO1_level=final_assesment[t]
      elif t==2:  
        select_attainment.CO2_level=final_assesment[t]
      elif t==3:  
        select_attainment.CO3_level=final_assesment[t]
      elif t==4:  
        select_attainment.CO4_level=final_assesment[t]
      elif t==5:  
        select_attainment.CO5_level=final_assesment[t]

      db.session.commit()    
  else:
    if final_assesment!=[]:
     for t in range(1,6):
       if t==1:
         CO1_Level=final_assesment[0]
       elif t==2:  
         CO2_Level=final_assesment[1]
       elif t==3:  
         CO3_Level=final_assesment[2]
       elif t==4:  
         CO4_Level=final_assesment[3]
       elif t==5:  
         CO5_Level=final_assesment[4]
       
    entry=Total_attainment(
      CO1_level=CO1_Level,
      CO2_level=CO2_Level,
      CO3_level=CO3_Level,
      CO4_level=CO4_Level,
      CO5_level=CO5_Level,
      fieldId=session['field_id']
    )
    db.session.add(entry)
    db.session.commit()     
    
  return render_template('co_attainment.html',rows=select,rows1=select_test1,rows2=select_test2,rows3=select_mico,rows4=select_msbte,attainment_external=attainment_external,attainment_prpa=attainment_prpa,attainment_internal=attainment_internal,final_assesment=final_assesment)   

@app.route('/po_attainment',methods=['GET','POST'])
def po_attainment():
   # Check Login Fieil Id
  if 'user_id' in session :
    pass
  else:
    return redirect('/login')
  if 'field_id' in session:
    pass
  else:
    return render_template('validation.html',message="Please Selecet Any Subject Otherwise Create New Subject", serverSite=True)

  select= Comapping.query.filter_by(fieldId=session['field_id']).first()
  select5= Comapping.query.filter_by(fieldId=session['field_id']).all()
  select_index=Index.query.filter_by(Id=session['field_id']).first()
  select_attainment=Total_attainment.query.filter_by(fieldId=session['field_id']).first()
  po_attainment=Po_attainment.query.filter_by(fieldId=session['field_id']).first()
  co_map=[]
  final_assesment=[]
  coCode=[]
  final_pos=[]
  total_level=[]
  count=0
  iterator=0
  for rows in select5:
    count+=1
  if count<5:
      return render_template('validation.html',message="Fill the remaining data or first check the CO attainment page", serverSite=True)

      
  for rows in select5:
    co_map.append(rows.coCode)
  
  final_assesment.append(select_attainment.CO1_level)
  final_assesment.append(select_attainment.CO2_level)
  final_assesment.append(select_attainment.CO3_level)
  final_assesment.append(select_attainment.CO4_level)
  final_assesment.append(select_attainment.CO5_level)
  coCode.append(select_index.coCode)
  ##for the fullfillment of the list error out of index ((required not to be deleted)
  for i in range(0,9):
    final_pos.append(0)
    total_level.append(0)
  for rows in select5:  
    total_level[0]+=rows.po1
    total_level[1]+=rows.po2
    total_level[2]+=rows.po3
    total_level[3]+=rows.po4
    total_level[4]+=rows.po5
    total_level[5]+=rows.po6
    total_level[6]+=rows.po7
    total_level[7]+=rows.pso1
    total_level[8]+=rows.pso2
    
  for rows in select5:
    final_pos[0]+=final_assesment[iterator]*rows.po1
    final_pos[1]+=(final_assesment[iterator]*rows.po2)
    final_pos[2]+=(final_assesment[iterator]*rows.po3)
    final_pos[3]+=(final_assesment[iterator]*rows.po4)
    final_pos[4]+=(final_assesment[iterator]*rows.po5)
    final_pos[5]+=(final_assesment[iterator]*rows.po6)
    final_pos[6]+=(final_assesment[iterator]*rows.po7)
    final_pos[7]+=(final_assesment[iterator]*rows.pso1)
    final_pos[8]+=(final_assesment[iterator]*rows.pso2)
    iterator+=1
  total_level = [1,1,1,1,1,1,1,1,1]
  for y in range(0,9):
    final_pos[y]=final_pos[y]/total_level[y]   

  if po_attainment!=None and final_pos!=[]: 
    for t in range(0,9): 
      if t==1:
       po_attainment.finalpo1=final_pos[t]
      elif t==2:  
       po_attainment.finalpo2=final_pos[t]
      elif t==3:  
       po_attainment.finalpo3=final_pos[t]
      elif t==4:  
       po_attainment.finalpo4=final_pos[t]
      elif t==5:  
       po_attainment.finalpo5=final_pos[t]
      elif t==6:  
       po_attainment.finalpo6=final_pos[t]
      elif t==7:  
       po_attainment.finalpo7=final_pos[t] 
      elif t==8:  
       po_attainment.finalpo8=final_pos[t]
    db.session.commit()    
  else:
    if final_pos!=[]:
     for t in range(0,9):
       if t==1:
         finalpo1=final_pos[t]
       elif t==2:  
         finalpo2=final_pos[t]
       elif t==3:  
         finalpo3=final_pos[t]
       elif t==4:  
         finalpo4=final_pos[t]
       elif t==5:  
         finalpo5=final_pos[t]
       elif t==6:  
         finalpo6=final_pos[t]
       elif t==7:  
         finalpo7=final_pos[t]
       elif t==8:  
         finalpo8=final_pos[t]   
           
    entry=Po_attainment(
      finalpo1=finalpo1,
      finalpo2=finalpo2,
      finalpo3=finalpo3,
      finalpo4=finalpo4,
      finalpo5=finalpo5,
      finalpo6=finalpo6,
      finalpo7=finalpo7,
      finalpo8=finalpo8,
      fieldId=session['field_id']
    )
    db.session.add(entry)
    db.session.commit()   

  return render_template('po_attainment.html',rows=co_map,final_assesment=final_assesment,co_mapping=select5,coCode=coCode,po_direct=final_pos)   


@app.route('/a',methods=['GET','POST'])
def no():
  return render_template('validation.html',message="This is CS50", serverSite=True)

@app.route('/logout')
def logout():
  if 'user_id' in session:
    session.pop('user_id')

  if 'field_id' in session:
    session.pop('field_id')

  return redirect('/login')


if __name__ == '__main__':
  app.run(debug=True)