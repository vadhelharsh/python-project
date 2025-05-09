from flask import Flask,render_template,request,flash, redirect,url_for
from database import Patient, engine, Session

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login" , methods =["POST", "GET"])
def login():
    return render_template("login_page.html")

@app.route('/fill_details', methods = ["POST"])
def fill_details():
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()
    if username == 'harsh' and password == '7043660314':
        return render_template('pateint_detail_form.html', username = username , password = password)
    else: 
        # message = "invalid login credentials"
        # flash(message)
        # return redirect(url_for('login'))
        return "invalid credentials."

@app.route('/family_login', methods = ["POST","GET"])
def family_login():
    return render_template('family_member_login.html')

@app.route('/show_details', methods = ["POST"])
def show_details():
    phone_number = request.form.get('phone_number').strip()
    session = Session()
    data = session.query(Patient).filter_by(emergencyNumber = phone_number).first()
    if data:
        return render_template('Familly_page.html', pateint_data = data)
    else: 
        return "Invalid Number Plz Check" 

@app.route('/submit_patient', methods= ["POST", "GET"])
def submit_patient():
    if request.method == "POST":
        patient_data  = {
            "firstname" : request.form.get('firstname'),
            "lastname" : request.form.get('lastname'),
            "age" : request.form.get('age'),
            "gender" : request.form.get('gender'),
            "hospitalLink" : request.form.get('hospital_link'),
            "emergencyNumber" : request.form.get('emergency_number'),
            "dateAndTime" : request.form.get('date_n_time'),
            "hospitalName" : request.form.get('hospital_name'),
            "wardName" : request.form.get('ward_name'),
            "bedNumber" : request.form.get('bed_number'),
            "currentCondition" : request.form.get('condition'),
            "fundRequired" : request.form.get('funds'),
            "Urgency" : request.form.get('Urgency'),
            "intialDiagnosis" : request.form.get('Initial_info')
        }
        # USING ** THE FUNCTION TO UNPACK THE DICT AND PASS IT TO THE CLASS
        submit_patient = Patient(**patient_data)
        session = Session()
        session.add(submit_patient)
        session.commit()
        return "Patient and its details added SUCCESSFULLY"

if __name__ == '__main__':
    app.run(debug=True)
