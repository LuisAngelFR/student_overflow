from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Question(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), nullable=False)
  content = db.Column(db.Text, nullable=False)

class Answer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text, nullable=False)
  question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
  timestamp = db.Column(db.DateTime, default=datetime.now)
  question = db.relationship('Question', backref=db.backref('answers', lazy=True))

  def __repr__(self):
    return f'<Answer {self.id}>'


@app.route('/')
def index():
  questions = Question.query.all()
  return render_template('index.html', questions=questions)

@app.route('/question/<int:id>', methods=['GET', 'POST'])
def question(id):
  question = Question.query.get_or_404(id)
  
  if request.method == 'POST':
    content = request.form['content']
    new_answer = Answer(content=content, question_id=id)
    db.session.add(new_answer)
    db.session.commit()
    return redirect(url_for('question', id=id))

  answers = Answer.query.filter_by(question_id=id).all()
  return render_template('question.html', question=question, answers=answers)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']
    new_question = Question(title=title, content=content)
    db.session.add(new_question)
    db.session.commit()
    return redirect(url_for('index'))
  return render_template('ask_question.html')

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)
