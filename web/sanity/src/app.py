from flask import Flask, render_template, redirect, request
import subprocess

app = Flask(__name__)

localhost = ['127.0.0.1', '::1', 'localhost', '0.0.0.0', '2130706433', '01111111 . 00000000 . 00000000 . 00000001']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/redirect', methods=['POST'])
def redirect_page():
    url = request.form.get('url', 'https://example.com/')

    if not url.startswith('http://'):
        return "Please use http only (beta app)"

    for i in localhost:
        if url.split('//')[1].startswith(i):
            return "Nope, next time!!"

    try:
        result = subprocess.check_output(['curl', url], text=True)
        return f"Curl command executed successfully with URL: {url}\nResult:\n{result}"
    except subprocess.CalledProcessError as e:
        return f"Error executing curl command with URL: {url}\nError: {e.output}"

@app.route('/yay')
def yay():
    if request.remote_addr != '127.0.0.1':
        return "Nope, only localhost can access this:)"
    else:
        return "\n<h1>quarkCTF{55RF_c4nt_b3-St0Pped_OFC}"

#print("\n\n\nNAME OF THE APP IS : ", __name__)
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
