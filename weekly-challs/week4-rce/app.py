from flask import Flask, render_template, request
from os import popen

app = Flask(__name__, static_folder="static", static_url_path="/")

def valid_cmd(cmd):
    allowed_cmds = ['id', 'ls', 'whoami', 'pwd', 'exit']
    for i in allowed_cmds:
        if i in cmd:
            return True
    else:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input == 'exit':
            exit(0)
        else:
            if valid_cmd(user_input):
                result = popen(user_input).read()
            else:
                result = 'Malicious input!!\nAllowed commands are : id, ls, whoami, pwd'
        
        return "Sorry, since a few people did some unintended things, we took down shell access."
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

