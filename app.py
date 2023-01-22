from flask import Flask,render_template, request, session, redirect
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
import bcrypt
from flask.helpers import url_for

app = Flask(__name__, template_folder='templates')
app.config['MONGO_DBNAME'] = 'genex'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/genex'
app.secret_key = 'sayali'
mongo = PyMongo(app)

db = MongoEngine()
db.init_app(app)  

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/logins" ,methods=['POST','GET'])
def login():
    return " login succesfull"

@app.route("/register_page" )
def registerhtml():
    return render_template('register.html')

@app.route('/register' ,methods=['POST','GET'])
def register_user():
    if request.method == 'POST':
        user= mongo.db.user
        
        existing_user = user.find_one({'username':request.form.get('username')}) 
        if existing_user is None:
            user.insert_one({'name': request.form.get('name'),'username' : request.form.get('username'),'dob':request.form.get('const {propertyName} = objectToDestruct;'),'phoneno' : request.form.get('phoneno'), 'password' :request.form.get('password')})
            session['username'] = request.form['username']
        else:
            return 'username already exists'
    return "registered"

@app.route('/user_login',methods=['POST','GET'])
def candidate():
    if request.method=='POST':
        user= mongo.db.user
        login_user = user.find_one({'username':request.form['username']})
        if login_user:
            if (request.form['password']) == login_user['password']:
                print(request.form['password'])
                print(login_user['password'])
                session['username'] = request.form['username']
                return render_template('login_success.html')
            return 'invalid password'
        return 'signup first'   
    return "login sucessful"

@app.route('/register_insert', methods=['POST'])
def register():
    if request.method == 'POST':
        user= mongo.db.user

        hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),bcrypt.gensalt())
        existing_user = user.find_one({'username':request.form.get('username')}) 
        if existing_user is None:
            user.insert_one({'name': request.form.get('name'),'username' : request.form.get('username'),'dob':request.form.get('const {propertyName} = objectToDestruct;'),'phoneno' : request.form.get('phoneno'), 'password' :hashpass})
            session['username'] = request.form['username']
        else:
            return 'username already exists'
    return redirect(url_for('candidate'))

    
if __name__ == "__main__":
    app.run(debug=True)