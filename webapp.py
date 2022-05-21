from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route1')
def route1():
    return '<h1>This is route1 page</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')