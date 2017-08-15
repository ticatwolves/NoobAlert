from flask import Flask,render_template,request,redirect,url_for,session,flash

#from MySQLdb import escape_string as thwart
#from passlib.hash import sha256_crypt

import NoobAlertDB

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',myfunction=show)

@app.route('/message')
def messages():
    return redirect(url_for('home'))


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/<username>')
def user(username):
    check = NoobAlertDB.checkavability(username)
    if check:
        return "No User Found"
    return render_template('postmsg.html',uname=username)

@app.route('/message/<username>',methods=['POST','GET'])
def addmessage(username):
    if request.method == "POST":
        if (request.form['msg']):
            NoobAlertDB.addmsg(username,request.form['msg'])
            return redirect(url_for('thanks'))

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        if (request.form['username'] and request.form['password']):
            username = request.form['username']
            password = request.form['password']
            ps = NoobAlertDB.getloginDetails(username)
            if(ps==password):
                session['logged']=True
                session['username'] =username

            flash("Invalid Password or user name")
            return redirect(url_for('home'))

            data = ""
            #if(sha256_crypt.verify(password,data)):
            #    session['logged_in'] = True
            #    session['username'] = username
            #    return redirect(url_for('user'))
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session['logged'] = False
    session['username'] = ""
    return redirect(url_for("home"))


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        uname=request.form['username']
        password=request.form['password']
        email = request.form['email']
        cpassword = request.form['confirm-password']
        if(uname and password and email and cpassword):
            if(cpassword==password):
                check = NoobAlertDB.checkavability(uname)
                if check:
                    NoobAlertDB.addUsers(uname,password,email)
                else:
                    flash('User Name not available')
                return redirect(url_for('home'))
            flash("Password didn't match")
            return redirect(url_for('home'))
    return redirect(url_for('home'))

@app.errorhandler(404)
def page_not_found(e):
    #flash("Page Not Found")
    return render_template('404.html')

@app.errorhandler(405)
def page_not_found(e):
    #flash("Method not allowed")
    return render_template('405.html')

@app.errorhandler(400)
def page_not_found(e):
    #flash("Method not allowed")
    return render_template('400.html')


def show(user):
    msg = NoobAlertDB.showmessage(user)
    return msg


app.secret_key = '1502772593#@@#FDSNGVSDVFBNHJMDCS531383#@$@Rr42e23'
app.config['SESSION_TYPE'] = 'filesystem'
app.run()
