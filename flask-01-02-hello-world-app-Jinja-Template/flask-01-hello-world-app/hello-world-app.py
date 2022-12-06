from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/second')
def seconds():
    return "This is the second)"

@app.route('/third/subthird')
def third():
    return "This is the subpage of third page"

@app.route('/fourth/<string:id>')
def forth(id):
    return f"The id of this page is {id}"

if __name__=='__main__':
    app.run(debug=True)



