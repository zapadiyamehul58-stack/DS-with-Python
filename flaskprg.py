from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <form method="POST" action="/return">
        <label>Enter your username:</label><br>
        <input type="text" name="username"><br>
        <label>Enter your marks :</label><br>
        <input type="text" name="marks"><br>
        <input type="submit" value="Submit">
    </form>
    '''

@app.route("/return", methods=["POST"])
def result():
    username = request.form.get("username")
    marks = request.form.get("marks")
    if marks >=35:
        ans ="PASS "
    else:
        ans= "fail "
    
    return f"""<h3>Submitted Details:</h3>
            Username: {username}<br>
            marks: {marks}<br>
            <br>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
