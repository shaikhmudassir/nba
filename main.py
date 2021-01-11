from flask import Flask,render_template,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import os
import csv
import math
import time
import array as array

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
  th = db.Column(db.Integer,unique=False,nullable=False)
  poe = db.Column(db.Integer,unique=False,nullable=False)
  tw = db.Column(db.Integer,unique=False,nullable=False)
  avgMarks = db.Column(db.Integer,unique=False,nullable=False)
  userId = db.Column(db.Integer,unique=False,nullable=False)
  filename = db.Column(db.String(100),unique=False,nullable=True)

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
  fieldId=db.Column(db.Integer,nullable=False)  

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


@app.route('/',methods=['GET','POST'])
def index():
  # Check Login 
  if 'user_id' in session:
    pass
  else:
    return redirect('/login')

  if request.method == 'POST':
    academicYear = request.form.get('academicYear')  		
    semester = request.form.get('semester')
    faculty = request.form.get('faculty')
    subject = request.form.get('subject')
    subjectCode = request.form.get('subjectCode')
    abbreviation = request.form.get('abbreviation')
    courseSemester = request.form.get('courseSemester')
    coCode = request.form.get('coCode')
    th = request.form.get('th')
    poe = request.form.get('poe')
    tw = request.form.get('tw')
    avgMarks = request.form.get('avgMarks')
    tempId1 = request.form.get('tempId1')
    tempId2 = request.form.get('tempId2')
    
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
        th = th,
        poe = poe,
        tw = tw,
        avgMarks = avgMarks,
        userId = session['user_id']
      )
      db.session.add(entry)
      db.session.commit()

      select = Index.query.filter_by(userId = session['user_id'], subjectCode=subjectCode, academicYear=academicYear).first()
      session['field_id'] = select.Id

      return redirect('/student-list')
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
      select.th = th
      select.poe = poe
      select.tw = tw
      select.avgMarks = avgMarks
      db.session.commit()
      return redirect('/student-list')
    else:
      if 'field_id' in session:
        session.pop('field_id')

      select = Index.query.filter_by(Id=tempId1).first()
      session['field_id'] = select.Id
      return render_template('index.html',row=select)
  
  if 'field_id' in session:
    select = Index.query.filter_by(Id=session['field_id']).first()
    return render_template('index.html',row=select)
  return render_template('index.html',row=None)



@app.route('/login',methods=['GET','POST'])
def login():
  return render_template('login.html')


@app.route('/login/<string:var>',methods=['GET','POST'])
def loginCheck(var):
  '''If var is 0 then perform Registration else perform login '''
  if var == '0':
    if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
      confirmPassword = request.form.get('confirmPassword')

      if password != confirmPassword:
        return ('<h1>Error</h1>')

      entry = Login(
        username = username,
        password = generate_password_hash(password),
      )

      db.session.add(entry)
      db.session.commit()
      
      select = Login.query.filter_by(username=username).first()

      if select == None or not check_password_hash(select.password, password):
        return ('<h1>Error</h1>')

      session['user_id'] = select.Id
      return redirect('/')

  else:
    if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
      select = Login.query.filter_by(username=username).first()

      if select == None or not check_password_hash(select.password, password):
        return ('<h1>Error</h1>')

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
    return ('<h1>Error</h1>')
  
  # what if file is get replaced ?
  
  # Upload Student list (csv/Execel file)
  if request.method == 'POST' :
    f = request.files['filename']
    select = Index.query.filter_by(Id=session['field_id']).first()
    filename = select.abbreviation + select.academicYear + '.csv'
    select.filename = filename
    db.session.commit()
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(filename)))
    with open(app.config['UPLOAD_FOLDER'] + '\\' + select.filename,'r') as file:
      rows = csv.DictReader(file)
      for row in rows:
        entry = Studentlist (
          rollNo = row['Roll No.'],
          enrollNo = row['Enroll No.'],
          studentsName = row['Name of Students'],
          fieldId = session['field_id'],
          userId = session['user_id']
        )
        db.session.add(entry)
        db.session.commit()
    return redirect('/student-list')
  
  select = Studentlist.query.filter_by(fieldId=session['field_id']).all()
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
    return ('<h1>Error</h1>')

  select = Comapping.query.filter_by(fieldId=session['field_id']).all()
  count = len(select)  
  print('select ',select)
  print('count', count)
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

    select = Index.query.filter_by(Id=session['field_id']).first()
    coCode = select.coCode + '.' + str(count + 1)

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
    return render_template('mapping.html',rows=select,total=total,avg=avg)
  return render_template('mapping.html',rows=select)

def Round(a, b):
  if (a / b) == 0.5:
    return 1
  return round(b)
def Counter(a):
  if a>=0:
    return 1
  else:
    return 0
def Average(a,b):
  if a>=1.14 and b==1:
    return 1
  elif a>=2.28 and b==2:
    return 1
  elif a>=3.42 and b==3:
    return 1
  elif a>=47.6 and b==4:
    return 1
  else:
    return 0
def Percentage(a,b):
  if b>0:
    return round((a/b),2)
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
      return ('<h1>Error</h1>')
    total = {'co1_1':0,'co1_2':0,'co1_3':0,'co2_1':0,'co2_2':0,'co2_3':0,'co3_1':0,'co3_2':0,'co3_3':0,'co3_4':0,'co3_5':0}
    avg = {'co1_1':0,'co1_2':0,'co1_3':0,'co2_1':0,'co2_2':0,'co2_3':0,'co3_1':0,'co3_2':0,'co3_3':0,'co3_4':0,'co3_5':0}
    per = {'co1_1':0,'co1_2':0,'co1_3':0,'co2_1':0,'co2_2':0,'co2_3':0,'co3_1':0,'co3_2':0,'co3_3':0,'co3_4':0,'co3_5':0}
    att_per={'co1':0,'co2':0,'co3':0}
    level={'co1':0,'co2':0,'co3':0}
    inp_rollno=[]
    rollnos=[]
    present=[]
    ids=[]
    names=[]
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
          return render_template('test1.html',rows=entries)
      else:
        rollno=rollnos[0]
        name=names[0]
        s_id=ids[0]
        rn=-1
    else:
      return "<h1>UPLOAD STUDENTLIST </h1>"
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
       entries=Studentlist.query.filter_by(fieldId=session["field_id"]).all()
       for row in entries:
         if row.studentsName in request.form:
           inp_rollno.append(Studentlist.query.filter_by(studentsName=row.studentsName,fieldId=session["field_id"]).first())
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
            return render_template('test1.html',level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=rollnos[rn+2],name=names[rn+2],id=ids[rn+2])
          else:
            return render_template('test1.html',level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=0)
    else:
      return render_template('test1.html',level=level,att_per=att_per,total=total,rows=entries,avg=avg,per=per,rollno=rollno,name=name,id=s_id)



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
      return ('<h1>Error</h1>')
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
          return render_template('test2.html',rows=entries)
      else:
        rollno=rollnos[0]
        name=names[0]
        s_id=ids[0]
        rn=-1
  else:
        return "<h1>Upload StudentList</h1>"
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
    entries=Studentlist.query.filter_by(fieldId=session["field_id"]).all()
    for row in entries:
         if row.studentsName in request.form:
           inp_rollno.append(Studentlist.query.filter_by(studentsName=row.studentsName,fieldId=session["field_id"]).first())
    if inp_rollno!=[]:
        for inp in inp_rollno: 
          for i in range(1,12):
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
         aavg["co4_5"]+=Average(row.CO4_5,3)
         aavg["co5_3"]+=Average(row.CO5_3,3)
         aavg["co5_4"]+=Average(row.CO5_4,3)
         aavg["co5_5"]+=Average(row.CO5_5,3)
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
       return render_template('test2.html',level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=rollnos[rn+2],name=names[rn+2],id=ids[rn+2])
      else:
       return render_template('test2.html',level=level,att_per=att_per,total=total,avg=avg,per=per,rows=entries,rollno=0)
  else:
      return render_template('test2.html',level=level,att_per=att_per,total=total,rows=entries,avg=avg,per=per,rollno=rollno,name=name,id=s_id)

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
      return ('<h1>Error</h1>')
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
    for row in entries:
        total["th"]+=Counter(row.TH)
        total["pr"]+=Counter(row.PR)
        avg["th"]+=Average(row.TH,4)
        avg["pr"]+=Average(row.PR,4)
    per["th"]=Percentage(avg["th"],total["th"])
    per["pr"]=Percentage(avg["pr"],total["pr"])
    level["th"]=Level(per["th"])
    level["pr"]=Level(per["pr"])
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
          return render_template('msbte.html',rows=entries)
      else:
        rollno=rollnos[0]
        name=names[0]
        s_id=ids[0]
        rn=-1
    else:
      return "<h1>Upload Student List</h1>"
    if request.method=="POST":
     entries=Studentlist.query.filter_by(fieldId=session["field_id"]).all()
     for row in entries:
         if row.studentsName in request.form:
           inp_rollno.append(Studentlist.query.filter_by(studentsName=row.studentsName,fieldId=session["field_id"]).first())
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
        avg["pr"]+=Average(row.PR,4)
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
    return render_template('msbte.html',rows=entries,level=level,total=total,avg=avg,per=per,rollno=rollno,name=name,id=s_id)


@app.route('/a',methods=['GET','POST'])
def no():
  return render_template('login.html')


@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
  if 'user_id' in session:
    pass
  else:
     return redirect('/login')

  select = Index.query.filter_by(userId=session['user_id'])
  return render_template('dashboard.html',rows=select)


@app.route('/logout')
def logout():
  if 'user_id' in session:
    session.pop('user_id')

  if 'field_id' in session:
    session.pop('field_id')

  return redirect('/login')


if __name__ == '__main__':
  app.run(debug=True)
