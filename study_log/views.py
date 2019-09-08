from flask import render_template, request, redirect, url_for
from study_log import app, db
from study_log.models import Log
from study_log.forms import LogForm


@app.route('/')
def index():
  logs = Log.query.order_by(Log.created_at.desc()).all()
  return render_template('index.html', logs=logs)

@app.route('/register', methods=['GET','POST'])
def register():
  form = LogForm()
  if request.method == "POST":
      if form.validate_on_submit():
          log = Log(date=form.date.data, time=form.time.data, memo=form.memo.data, todo=form.todo.data)
          db.session.add(log)
          db.session.commit()
          db.session.close()
          return redirect(url_for('index'))
      else:
        error = "エラーです"
        return render_template('edit.html', form=form, error=error)
  else:
      return render_template('edit.html', form=form)

@app.route('/detail/<int:id>')
def detail(id):
    log = Log.query.get(id)
    form = LogForm()
    return render_template('detail.html', log=log, form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    log = Log.query.get(id)
    form = LogForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            log.date = form.date.data
            log.time = form.time.data
            log.memo = form.memo.data
            log.todo = form.todo.data
            db.session.commit()

            return redirect(url_for('index'))
    else:
        form.date.data = log.date
        form.time.data = log.time
        form.memo.data = log.memo
        form.todo.data = log.todo
        return render_template('edit.html', form=form, id=id)

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
        log = Log.query.get(id)
        db.session.delete(log)
        db.session.commit()
        return redirect(url_for('index'))