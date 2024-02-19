from flask import Flask, render_template, request, jsonify
import re
import subprocess

app = Flask(__name__)

def is_valid_input(cmd, arg):
    allowed_cmds = ['ls', 'grep']
    if cmd in allowed_cmds and re.match(r'^[a-zA-Z0-9\s-]+$', arg):
        return True
    else:
        return False


def is_valid_path(input_path):
    if input_path.startswith("/app/files/"):
        return True
    else:
        return False


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_command():
    cmd = request.form['cmd']
    arg = request.form['arg']
    path = request.form['path']
    
    if not is_valid_input(cmd, arg):
        return jsonify({'error': 'Data tampered: Invalid command or arguments'}), 400
    
    if not is_valid_path(path):
        return jsonify({'error': 'Path not allowed'}), 400
    
    try:
        result = subprocess.run([cmd, arg, path], capture_output=True, text=True)
        #print('running : ', cmd + ' ' + arg + ' ' + path + '\n')
        output = result.stdout
        return jsonify({'success': True, 'output': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)


