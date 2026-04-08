from flask import Flask, request, jsonify
from config import DATABASE_URL, SECRET_KEY
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY
db.init_app(app)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

if __name__ == '__main__':
    app.run(debug=True)