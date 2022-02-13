from flask import Flask, render_template
app = Flask(__name__)

#double routes:
@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')