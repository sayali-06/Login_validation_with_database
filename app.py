from flask import Flask,render_template, request, session, redirect
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
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
        pass1 = request.form.get('password')
        pass2 = request.form.get('cpassword')
        
        existing_user = user.find_one({'username':request.form.get('username')}) 
        if existing_user is None:
            if pass1 == pass2:
                user.insert_one({'name': request.form.get('name'),'username' : request.form.get('username'),'dob':request.form.get('const {propertyName} = objectToDestruct;'),'phoneno' : request.form.get('phoneno'), 'password' :request.form.get('password')})
                session['username'] = request.form['username']
            else:
                return "password mismatch"
        else:
            return 'username already exists'
    return redirect(url_for('home'))

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
    return "login unsucessful"

    
if __name__ == "__main__":
    app.run(debug=True)