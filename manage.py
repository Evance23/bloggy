from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')


@app.route('/about')
def about():
    render_template ('about.html')

@app.route('post')
def post():
    render_template('post.html')

@app.route('/contact')
def contact():
    render_template('contact.html')












if __name__ == '__main__:'

app.run(debug=True)
