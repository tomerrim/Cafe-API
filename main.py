from flask import Flask, jsonify, render_template, request
from database import db, Cafe

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/all')
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

if __name__ == '__main__':
    app.run(debug=True)