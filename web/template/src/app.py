from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

f = open('flag2.txt','r')

@app.get('/')
def index():
    result = '''
        <link rel="stylesheet" href="style.css" />
        <div class="container">
            <p> >Can i come in ? </p>
            <p> >Sure , Just close the door behind you</p>
            <form method="POST">
                <input type="text" name="text">
                <input type="submit" value="Submit">
            </form>
        </div>
    '''
    return render_template_string(result)

@app.post('/')
def submiti():
    result = '''
        <link rel="stylesheet" href="style.css" />
        <div class="container">
            <h1>Keep going</h1>
            <p></p>
            <form method="POST">
                <input type="text" name="text">
                <input type="submit" value="Submit">
            </form>
            <p>Output: %s</p>
        </div>
    '''
    output=request.form.get('text', '')
    print(output)
    return render_template_string(result % output)

os.remove('flag2.txt')
@app.get('/style.css')
def style():
    return '''
        * {
            font-family: 'Helvetica Neue', sans-serif;
            box-sizing: border-box;
        }

        html, body { margin: 0; }

        .container {
            padding: 2rem;
            width: 90%;
            max-width: 900px;
            margin: auto;
        }

        input:not([type="submit"]) {
            width: 100%;
            padding: 8px;
            margin: 8px 0;
        }
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
