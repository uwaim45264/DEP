from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))


user_parser = reqparse.RequestParser()
user_parser.add_argument('username', type=str, required=True, help='Username is required')
user_parser.add_argument('password', type=str, required=True, help='Password is required')

item_parser = reqparse.RequestParser()
item_parser.add_argument('name', type=str, required=True, help='Name is required')
item_parser.add_argument('description', type=str)


class UserRegister(Resource):
    def post(self):
        data = user_parser.parse_args()
        if User.query.filter_by(username=data['username']).first():
            return {'message': 'User already exists'}, 400

        user = User(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201


class UserLogin(Resource):
    def post(self):
        data = user_parser.parse_args()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401


class ItemResource(Resource):
    @jwt_required()
    def get(self, item_id):
        item = Item.query.get_or_404(item_id)
        return {'id': item.id, 'name': item.name, 'description': item.description}

    @jwt_required()
    def delete(self, item_id):
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {'message': 'Item deleted'}, 200


class ItemListResource(Resource):
    @jwt_required()
    def get(self):
        items = Item.query.all()
        return [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]

    @jwt_required()
    def post(self):
        data = item_parser.parse_args()
        item = Item(name=data['name'], description=data.get('description'))
        db.session.add(item)
        db.session.commit()
        return {'id': item.id, 'name': item.name, 'description': item.description}, 201


api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(ItemResource, '/item/<int:item_id>')
api.add_resource(ItemListResource, '/items')

if __name__ == '__main__':
    app.run(debug=True)
