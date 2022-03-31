from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
#from flask_security.utils import encrypt_password

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'please hire me'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    score = db.Column(db.Integer)
    previous_score = db.Column(db.Integer)
    high_score = db.Column(db.Integer)

    def __repr__(self) -> str:
        return '<User %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    this_score=roll()
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None:
            user = User(username=request.form['username'], score=this_score, previous_score=0, high_score=this_score)
            db.session.add(user)
            db.session.commit()
            users = User.query.order_by(User.high_score.desc()).all()
            
            return render_template('index.html', users=users, username=user.username, score=user.score, previous_score=user.previous_score, high_score=user.high_score)
        else:
            user.previous_score = user.score
            user.score = this_score
            user.high_score = decide_highest_score(current_high=user.high_score, new_potential_high=this_score)
            row_changed = User.query.filter_by(username=user.username).update(dict(previous_score=user.previous_score, score=user.score, high_score=user.high_score))
            db.session.commit()
            users = User.query.order_by(User.high_score.desc()).all()
            
            return render_template('index.html', users=users, username=user.username, score=user.score, previous_score=user.previous_score, high_score=user.high_score)
    else:
        user = User.query.first()
        users = User.query.order_by(User.high_score.desc()).all()
        return render_template('index.html', users=users, username=user.username, score=user.score, previous_score=user.previous_score, high_score=user.high_score)

def roll():
    score = random.randrange(1, 7, 1)
    return score

def decide_highest_score(current_high, new_potential_high) -> int:
    if current_high < new_potential_high:
        return new_potential_high
    return current_high

if __name__ == "__main__":
    app.run(debug=True)