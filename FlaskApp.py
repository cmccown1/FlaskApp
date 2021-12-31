from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/kinzley')
def kinzley():
    return render_template('kinzley.html')

if __name__ == '__main__':
    app.run()
