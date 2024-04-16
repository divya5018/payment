from flask import Flask


app=Flask(__name__)


@app.route('/')
def index():
    return "<h1> Welcome <h1>"

@app.route('/greet')
def index():
    return "<h1> Hello <h1>"    


if __name__=='__main__':
    app.run()    