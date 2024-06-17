from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///responses.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Respon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    job = db.Column(db.Text, nullable=False)
    limitation = db.Column(db.Text, nullable=False)
    digital = db.Column(db.Text, nullable=False)
    virtual = db.Column(db.Text, nullable=False)
    brille = db.Column(db.Text, nullable=False)
    software = db.Column(db.Text, nullable=False)
    funktionen = db.Column(db.Text, nullable=False)
    ziel = db.Column(db.Text, nullable=False)
    q_1 = db.Column(db.Boolean, nullable=False)
    q_2 = db.Column(db.Boolean, nullable=False)
    q_3 = db.Column(db.Boolean, nullable=False)
    q_4 = db.Column(db.Boolean, nullable=False)
    q_5 = db.Column(db.Boolean, nullable=False)
    q_6 = db.Column(db.Boolean, nullable=False)
    q_7 = db.Column(db.Boolean, nullable=False)
    q_8 = db.Column(db.Boolean, nullable=False)
    q_9 = db.Column(db.Boolean, nullable=False)
    q_10 = db.Column(db.Boolean, nullable=False)
    q_11 = db.Column(db.Boolean, nullable=False)
    q_12 = db.Column(db.Boolean, nullable=False)
    q_13 = db.Column(db.Boolean, nullable=False)
    q_14 = db.Column(db.Boolean, nullable=False)
    q_15 = db.Column(db.Boolean, nullable=False)
    q_16 = db.Column(db.Boolean, nullable=False)
    q_17 = db.Column(db.Boolean, nullable=False)
    q_18 = db.Column(db.Boolean, nullable=False)
    q_19 = db.Column(db.Boolean, nullable=False)
    q_20 = db.Column(db.Boolean, nullable=False)
    q_21 = db.Column(db.Boolean, nullable=False)
    q_21 = db.Column(db.Boolean, nullable=False)
    q_22 = db.Column(db.Boolean, nullable=False)
    q_23 = db.Column(db.Boolean, nullable=False)
    q_24 = db.Column(db.Boolean, nullable=False)
    q_25 = db.Column(db.Boolean, nullable=False)
    q_26 = db.Column(db.Boolean, nullable=False)
    q_27 = db.Column(db.Boolean, nullable=False)
    q_28 = db.Column(db.Boolean, nullable=False)
    q_29 = db.Column(db.Boolean, nullable=False)
    q_30 = db.Column(db.Boolean, nullable=False)
    q_31 = db.Column(db.Boolean, nullable=False)
    q_32 = db.Column(db.Boolean, nullable=False)
    q_33 = db.Column(db.Boolean, nullable=False)
    q_34 = db.Column(db.Boolean, nullable=False)
    q_35 = db.Column(db.Boolean, nullable=False)
    q_36 = db.Column(db.Boolean, nullable=False)
    q_37 = db.Column(db.Boolean, nullable=False)
    q_38 = db.Column(db.Boolean, nullable=False)
    q_39 = db.Column(db.Boolean, nullable=False)
    q_40 = db.Column(db.Boolean, nullable=False)
    q_41 = db.Column(db.Boolean, nullable=False)
    q_42 = db.Column(db.Boolean, nullable=False)
    q_43 = db.Column(db.Boolean, nullable=False)
    q_44 = db.Column(db.Boolean, nullable=False)
    q_45 = db.Column(db.Boolean, nullable=False)
    q_46 = db.Column(db.Boolean, nullable=False)
    q_47 = db.Column(db.Boolean, nullable=False)
    q_48 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_49 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_50 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_51 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_52 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_53 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_54 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_55 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_56 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_57 = db.Column(db.Integer, nullable=False)  # Change to Integer
    q_58 = db.Column(db.Text, nullable=False)
    q_59 = db.Column(db.Text, nullable=False)
    q_60 = db.Column(db.Text, nullable=False)
    q_61 = db.Column(db.Text, nullable=False)
    q_62 = db.Column(db.Text, nullable=False)
    q_63 = db.Column(db.Text, nullable=False)
    q_64 = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Respon {self.name}>'




@app.route("/")
def index():
    return render_template('index.html')

@app.route("/submit", methods = ["POST"])
def submit():
    name = request.form['name']
    age = request.form['age']
    gender= request.form['gender']
    job = request.form['job']
    limitation = request.form['limitation']
    digital = request.form['digital']
    virtual = request.form['virtual']
    brille = request.form['brille']
    software = request.form['software']
    funktionen = request.form['funktionen']
    ziel = request.form['ziel']
    q_1 = True if request.form['q_1'] == 'Ja' else False
    q_2 = True if request.form['q_2'] == 'Ja' else False
    q_3 = True if request.form['q_3'] == 'Ja' else False
    q_4 = True if request.form['q_4'] == 'Ja' else False
    q_5 = True if request.form['q_5'] == 'Ja' else False
    q_6 = True if request.form['q_6'] == 'Ja' else False
    q_7 = True if request.form['q_7'] == 'Ja' else False
    q_8 = True if request.form['q_8'] == 'Ja' else False
    q_9 = True if request.form['q_9'] == 'Ja' else False
    q_10 = True if request.form['q_10'] == 'Ja' else False
    q_11 = True if request.form['q_11'] == 'Ja' else False
    q_12 = True if request.form['q_12'] == 'Ja' else False
    q_13 = True if request.form['q_13'] == 'Ja' else False
    q_14 = True if request.form['q_14'] == 'Ja' else False
    q_15 = True if request.form['q_15'] == 'Ja' else False
    q_16 = True if request.form['q_16'] == 'Ja' else False
    q_17 = True if request.form['q_17'] == 'Ja' else False
    q_18 = True if request.form['q_18'] == 'Ja' else False
    q_19 = True if request.form['q_19'] == 'Ja' else False
    q_20 = True if request.form['q_20'] == 'Ja' else False
    q_21 = True if request.form['q_21'] == 'Ja' else False
    q_22 = True if request.form['q_22'] == 'Ja' else False
    q_23 = True if request.form['q_23'] == 'Ja' else False
    q_24 = True if request.form['q_24'] == 'Ja' else False
    q_25 = True if request.form['q_25'] == 'Ja' else False
    q_26 = True if request.form['q_26'] == 'Ja' else False
    q_27 = True if request.form['q_27'] == 'Ja' else False
    q_28 = True if request.form['q_28'] == 'Ja' else False
    q_29 = True if request.form['q_29'] == 'Ja' else False
    q_30 = True if request.form['q_30'] == 'Ja' else False
    q_31 = True if request.form['q_31'] == 'Ja' else False
    q_32 = True if request.form['q_32'] == 'Ja' else False
    q_33 = True if request.form['q_33'] == 'Ja' else False
    q_34 = True if request.form['q_34'] == 'Ja' else False
    q_35 = True if request.form['q_35'] == 'Ja' else False
    q_36 = True if request.form['q_36'] == 'Ja' else False
    q_37 = True if request.form['q_37'] == 'Ja' else False
    q_38 = True if request.form['q_38'] == 'Ja' else False
    q_39 = True if request.form['q_39'] == 'Ja' else False
    q_40 = True if request.form['q_40'] == 'Ja' else False
    q_41 = True if request.form['q_41'] == 'Ja' else False
    q_42 = True if request.form['q_42'] == 'Ja' else False
    q_43 = True if request.form['q_43'] == 'Ja' else False
    q_44 = True if request.form['q_44'] == 'Ja' else False
    q_45 = True if request.form['q_45'] == 'Ja' else False
    q_46 = True if request.form['q_46'] == 'Ja' else False
    q_47 = True if request.form['q_47'] == 'Ja' else False
    q_48 = int(request.form['q_48']) if 'q_48' in request.form else None
    q_49 = int(request.form['q_49']) if 'q_49' in request.form else None
    q_50 = int(request.form['q_50']) if 'q_50' in request.form else None
    q_51 = int(request.form['q_51']) if 'q_51' in request.form else None
    q_52 = int(request.form['q_52']) if 'q_52' in request.form else None
    q_53 = int(request.form['q_53']) if 'q_53' in request.form else None
    q_54 = int(request.form['q_54']) if 'q_54' in request.form else None
    q_55 = int(request.form['q_55']) if 'q_55' in request.form else None
    q_56 = int(request.form['q_56']) if 'q_56' in request.form else None
    q_57 = int(request.form['q_57']) if 'q_57' in request.form else None
    q_58= request.form['q_58']
    q_59= request.form['q_59']
    q_60= request.form['q_60']
    q_61= request.form['q_61']
    q_62= request.form['q_62']
    q_63= request.form['q_63']
    q_64= request.form['q_64']

    response = Respon(name=name, age=age, gender=gender, job=job, limitation=limitation, digital=digital, virtual=virtual, brille=brille, software=software, funktionen=funktionen, ziel=ziel, 
    q_1=q_1, q_2=q_2, q_3=q_3, q_4=q_4, q_5=q_5, q_6=q_6,q_7=q_7,q_8=q_8, q_9=q_9, q_10=q_10, q_11=q_11, q_12=q_12,q_13=q_13, q_14=q_14, q_15=q_15, q_16=q_16, q_17=q_17,q_18=q_18, q_19=q_19, q_20=q_20,
    q_21=q_21, q_22=q_22, q_23=q_23, q_24=q_24, q_25=q_25, q_26=q_26, q_27=q_27, q_28=q_28, q_29=q_29, q_30=q_30, q_31=q_31, q_32=q_32, q_33=q_33, q_34=q_34, q_35=q_35, q_36=q_36, q_37=q_37,
    q_38=q_38, q_39=q_39, q_40=q_40, q_41=q_41, q_42=q_42, q_43=q_43, q_44=q_44, q_45=q_45, q_46=q_46, q_47=q_47, q_48=q_48, q_49=q_49, q_50=q_50, q_51=q_51, q_52=q_52, q_53=q_53, q_54=q_54
    , q_55=q_55, q_56=q_56, q_57=q_57, q_58=q_58, q_59=q_59, q_60=q_60, q_61=q_61, q_62=q_62, q_63=q_63, q_64=q_64 )
    db.session.add(response)
    db.session.commit()

    return ' Vielen Dank für deine Eingabe'

@app.route("/results")
def results():
    database = Respon.query.all()
    total_responses = len(database)
    average_age = round(sum([response.age for response in database]) / total_responses, 1)
    unique_names = len(set([response.name for response in database]))
    return render_template("results.html", database=database, total_responses=total_responses, average_age=average_age, unique_names=unique_names)


    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


