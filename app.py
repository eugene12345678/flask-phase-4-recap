from flask import Flask, make_response
from flask_migrate import Migrate
from models import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///recap.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate=Migrate(app,db)
db.init_app(app)    


@app.route('/')
def index():
    return 'Hello World'

@app.route('/users', methods=['GET'])
def users():
    # users = Users.query.all()
    # print(users)
    response = [user.to_dict() for user in Users.query.all()]
    return make_response(response, 200)

@app.route('/posts', methods=['GET'])
def posts():
    response = [post.to_dict(only=['id', 'title', 'description']) for post in Post.query.all()]
    return make_response(response, 200)

if __name__ == '__main__':
    app.run(debug=True, port=5000)