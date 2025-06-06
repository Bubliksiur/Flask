from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='HomePage')

@app.route('/hello')
def hello():
    return render_template('hello.html', title='HelloPage')

if __name__== "__main__":
    app.run(debug=True)