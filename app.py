from flask import Flask


app=Flask(__name__)


@app.route('/')
def index():
    return "<h1> Welcome <h1>"

@app.route('/greet')
def index():
    return "<h1> Hello <h1>"   

@app.route('/greet/<name>')
def index(name):
    return "<h1> Hello {}<h1>".format(name)     


if __name__=='__main__':
    app.run()    