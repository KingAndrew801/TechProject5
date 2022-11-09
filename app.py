from flask import render_template, url_for, redirect, request
from models import app, db, Project

@app.route("/")
def index():
    proj = Project.query.all()
    return render_template('index.html', proj = proj)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/new', methods =['GET', 'POST'])
def addproj():
    if request.form:
        proj = Project(id = request.form['id'],
                       title=request.form['title'],
                       date=request.form['date'],
                       desc=request.form['description'],
                       skills=request.form['skills-list'],
                       github=request.form['github'])
        db.session.add(proj)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')

@app.route('/edit/<id>', methods = ['POST'])
def editproj(id):
    proj = db.session.get(id)
    return render_template('editproj.html', proj = proj)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
