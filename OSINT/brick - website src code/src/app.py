from flask import Flask, request, redirect, render_template, session
import pyotp
import urllib.parse
import os

app = Flask(__name__)
app.secret_key = os.urandom(128)

SECRET_KEY = "DVMQS3XJYBJE3JRJ"

def verify(otp, email):
    if len(otp) <= 6 and str(otp).isdigit():
        totp = pyotp.TOTP(SECRET_KEY)
        return totp.verify(otp) and email == 'tombrickctf@gmail.com'
    else:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    error = None  # Initialize error message
    if request.method == "POST":
        email = request.form.get("email")
        otp = request.form.get("otp")
        if verify(otp, email):
            session['otp_verified'] = True
            return redirect("/flag.txt")
        else:
            error = True
    return render_template("index.html", error=error)

@app.route("/flag.txt")
def flag():
    if session.get('otp_verified'):
        return "quarkCTF{05int-c4n_b3_d4nger0Us-#be_safe}"
    else:
        return "Access denied. Please verify OTP first."

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
