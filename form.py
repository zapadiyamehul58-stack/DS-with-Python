from flask import Flask , rander_template, request,redirect, _for
app = Flask(__name__)
@app.route('/')
def hello():
    return rander_emplete('login.html')
@app.route('/login',method=["POST"])
def login():
    unm=request.form.get('username')
    pas=request.form.get('password')

    if unm=="admin" and password=="123":
        return rander_template('dashbord.html')
    else:
        return redirecr(ulr_for('home.html'))
if __name__=='__main__':
    app.run(debug=True)
