from flask import Flask,render_template,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import os
import csv
import math

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
        entry = Studentlist(
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
  return round(a/b)


@app.route('/test1',methods=['GET','POST'])
def test():
  return render_template('test1.html')


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
