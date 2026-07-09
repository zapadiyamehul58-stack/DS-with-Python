from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

css = """
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%);
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0;
        color: #f5f5f5;
    }
    .card {
        background: #24243e;
        padding: 40px;
        border-radius: 16px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4);
        width: 360px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    h2, h3 {
        margin-bottom: 24px;
        color: #fff;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    .input-group {
        margin-bottom: 20px;
        text-align: left;
    }
    label {
        display: block;
        margin-bottom: 8px;
        font-size: 13px;
        color: #b3b3cc;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    input[type="text"], input[type="password"] {
        width: 100%;
        padding: 12px;
        background: #1a1a2e;
        border: 1px solid #3f3f5f;
        border-radius: 8px;
        box-sizing: border-box;
        font-size: 15px;
        color: #fff;
        transition: border-color 0.3s;
    }
    input[type="text"]:focus, input[type="password"]:focus {
        border-color: #7f5af0;
        outline: none;
    }
    button {
        width: 100%;
        padding: 12px;
        background: #7f5af0;
        border: none;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        cursor: pointer;
        transition: background 0.3s, transform 0.2s;
        margin-top: 10px;
    }
    button:hover {
        background: #9272f2;
        transform: translateY(-1px);
    }
    .error {
        color: #ff5c5c;
        margin-bottom: 15px;
        font-size: 14px;
        background: rgba(255, 92, 92, 0.1);
        padding: 10px;
        border-radius: 6px;
        border: 1px solid rgba(255, 92, 92, 0.2);
    }
    .welcome-user {
        color: #2cb67d;
        font-size: 28px;
        font-weight: bold;
        margin: 15px 0;
    }
    
    /* --- CSS Smooth Animation --- */
    .animate-app {
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.1) forwards;
    }
    
    @keyframes popIn {
        from {
            opacity: 0;
            transform: scale(0.92) translateY(20px);
        }
        to {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }
</style>
"""

login_form = css + """
<div class="card animate-app">
    <h2>App Login</h2>
    
    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}

    <form method="POST" action="/login">
        <div class="input-group">
            <label>Username</label>
            <input type="text" name="username" autocomplete="off" required>
        </div>
        <div class="input-group">
            <label>Password</label>
            <input type="password" name="password" required>
        </div>
        <button type="submit">Sign In</button>
    </form>
</div>
"""

user_dashbord = css + """
<div class="card animate-app">
    <h3>User Dashboard</h3>
    <p style="color: #94a1b2; margin: 0;">Welcome back,</p>
    <p class="welcome-user">{{ username }}</p>
    
    <hr style="border: 0; border-top: 1px solid #3f3f5f; margin: 25px 0;">
    
    <p style="font-size: 15px; color: #94a1b2;">Authorization Status: <strong style="color: #2cb67d;">● Online</strong></p>
    <br>
    <a href="/" style="text-decoration: none; color: #7f5af0; font-size: 14px; font-weight: bold;">Secure Logout</a>
</div>
"""

@app.route("/")
def home():
    return render_template_string(login_form )

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
   
    if username == "mehul" and password == "123":
        return redirect(url_for("dashboard", user=username))
    else:
        return render_template_string(login_form, error="Invalid Username or Password!")

@app.route("/dashboard")
def dashboard():
    username = request.args.get("user")
    if not username:
        return redirect(url_for("home"))
    return render_template_string(user_dashbord, username=username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
