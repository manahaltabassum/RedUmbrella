from flask import Flask,render_template, request, session, redirect, url_for,flash

app = Flask (__name__)

app.secret_key = 'secret'

userCode = "sasha"
passCode = "manahal"



@app.route('/', methods = ['POST', 'GET'])

def root():
    if session.has_key('user'):
        #return render_template('welcome.html', name= session['user'])
        return redirect(url_for('welcome', name = session['user']))
    else:
        return render_template('form.html')


@app.route('/welcome', methods = ['POST', 'GET'])

def welcome():
    
    currentUser = request.form['username']
    currentPass = request.form['password']
                               
    if currentUser  == userCode and currentPass == passCode:
        session['user'] = currentUser
        return render_template('welcome.html', name = currentUser)

    
    elif currentUser != userCode:  
        flash("Invalid username")
        return redirect(url_for('root'))
        # return render_template('error.html', errorMsg = "Username is wrong!")

    
    else:
        flash("Wrong password")
        return redirect(url_for('root'))
        #return render_template('error.html' , errorMsg = "Password is wrong!")

@app.route('/logOut' , methods = ['POST', 'GET'])

def logOut():
    session.pop('user')
    #return render_template('logOut.html')
    return redirect(url_for('root'))

if __name__ == '__main__':
    app.run(debug= True)
    
