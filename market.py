from flask import Flask
app = Flask(__name__)

@app.route('/')
def hollo_world():
  return '<h1> Hello, Wolrd!! Changed</h1>'

#Dynamic routing
@app.route('/about/<username>')
def about_page(username):
  return f'<h1> This is the about page of {username} </h1>'