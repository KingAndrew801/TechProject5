from flask import render_template, url_for, redirect, request
from models import app, db, Project
from datetime import datetime

@app.route("/")
def index():
    jects = Project.query.all()
    return render_template('index.html', jects=jects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/new', methods =['GET', 'POST'])
def addproj():
    if request.form:
        proj = Project(title=request.form['title'],
                       date=datetime.strptime(request.form['date'] + '-01','%Y-%m-%d'),
                       desc=request.form['desc'],
                       skills=request.form['skills'],
                       github=request.form['github'])
        db.session.add(proj)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def editproj(id):
    proj = Project.query.get(id)
    if request.form:
        proj.title = request.form['title']
        proj.date = datetime.strptime(request.form['date'] + '-01', '%Y-%m-%d')
        proj.desc = request.form['desc']
        proj.skills = request.form['skills']
        proj.github = request.form['github']
        db.session.commit()
        return redirect( url_for('index'))
    jects = Project.query.all()
    return render_template('editproj.html', proj = proj, jects=jects)

@app.route('/detail/<id>')
def detail(id):
    proj = Project.query.get_or_404(id)
    jects = Project.query.all()
    return render_template('detail.html', proj = proj, jects=jects)

@app.route('/delete/<id>')
def delete(id):
    proj = Project.query.get_or_404(id)
    db.session.delete(proj)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/skills')
def skills():
    jects = Project.query.all()

    def skillets():
        for p in jects:
            for skill in p.skills.split(', '):
                yield skill

    return render_template('skills.html',skillets=skillets(), jects=jects)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
