from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from makedb import create_my_database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=False)
    dealer = db.Column(db.Integer)
    rating = db.Column(db.String(200))
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

    def __repr__(self):
        return '<Feedback %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or dealer == '':
            return render_template('index.html', message='Пожалуйста, заполните обязательные поля')

        data = Feedback(customer, dealer, rating, comments)
        db.session.add(data)
        db.session.commit()
        return render_template('success.html')


if __name__ == '__main__':
    create_my_database()
    app.debug = True
    app.run()
