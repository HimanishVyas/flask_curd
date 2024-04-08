from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Curd


@app.route('/index')
def index():
    curds = Curd.query.all()
    return render_template('index.html', curds=curds)

@app.route('/add', methods=['GET', 'POST'])
def add_curd():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        curd = Curd(name=name, description=description)
        db.session.add(curd)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_curd(id):
    curd = Curd.query.get_or_404(id)
    if request.method == 'POST':
        curd.name = request.form['name']
        curd.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', curd=curd)

@app.route('/delete/<int:id>', methods=['GET'])
def delete_curd(id):
    curd = Curd.query.get_or_404(id)
    print(curd)
    db.session.delete(curd)
    db.session.commit()
    return redirect(url_for('index'))
