import os
from flask import Flask, render_template

app = Flask(__name__)

'''
@app.route('/')
def home():
	content= <h1>This is Home Page.<h1>
	<h2>By Holly</h2>
	return content

@app.route('/hello')
def hello():
	return "Hello World!"

@app.route('/<username>')
def hello_user(username):
    return "Hello,"+username

'''

def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            # fn = os.path.join(path, name)
            tree['children'].append(dict(name=name))
            # if os.path.isdir(fn):
            #    tree['children'].append(make_tree(fn))
            # else:
            #    tree['children'].append(dict(name=name))
    return tree

@app.route('/')
def dirtree():
    path = os.path.expanduser(u'~')
    return render_template('dirtree.html', tree=make_tree(path))


@app.route('/files')
def read_file():
    s=""
    for i in os.listdir("/Users/apple/Documents/Coding/python"):
        s+=i
    return s

if __name__ == '__main__':
    app.run(debug=True)
