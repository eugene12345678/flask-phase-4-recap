from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin   
db = SQLAlchemy()

user_group = db.Table('user_group',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class Users(db.Model, SerializerMixin):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)    
    email = db.Column(db.String(50), nullable=False, unique=True)

    
    posts = db.relationship('Post', back_populates='user', lazy=True)
    groups = db.relationship('Group', secondary=user_group, back_populates='users', lazy=True)
    
    serialize_rules = ('-posts.user', '-groups.users')
    @validates('email')
    def validate_email(self, key, value):
        if '@' not in value:
            raise ValueError("Invalid Email")
        return value

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts' 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), nullable=False)
    description = db.Column(db.String(225), nullable=False)


    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    user = db.relationship('Users', back_populates='posts')
# serialize_rules = ('-user.groups')
class Group(db.Model):
    __tablename__ = 'groups' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
   
    users = db.relationship('Users', secondary=user_group, back_populates='groups', lazy=True)