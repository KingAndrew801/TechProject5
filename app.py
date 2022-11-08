from flask import render_template, url_for, redirect, request
from models import app, db

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/new')
def addproj():
    if request.form:
        pass
    return render_template('projectform.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
