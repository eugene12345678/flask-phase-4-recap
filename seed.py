from app import app
from models import db, Users, Post, Group

with app.app_context():
    
    Users.query.delete()
    Post.query.delete()
    Group.query.delete()

    
    u1 = Users(name='John', email='john@example.com')
    u2 = Users(name='Jane', email='jane@example.com')
    u3 = Users(name='Jack', email='jack@example.com')
    u4 = Users(name='Jill', email='jill@example.com')
    u5 = Users(name='Joe', email='joe@example.com')

    db.session.add_all([u1, u2, u3, u4, u5])
    db.session.commit()

    # Add posts for the users
    p1 = Post(title='First Post', description='First Post Description', user=u1)
    p2 = Post(title='Second Post', description='Second Post Description', user=u1)
    p3 = Post(title='Third Post', description='Third Post Description', user=u1)
    p4 = Post(title='Fourth Post', description='Fourth Post Description', user=u4)
    p5 = Post(title='Fifth Post', description='Fifth Post Description', user=u5)
    p6 = Post(title='Sixth Post', description='Sixth Post Description', user=u1)
    p7 = Post(title='Seventh Post', description='Seventh Post Description', user=u1)
    p8 = Post(title='Eighth Post', description='Eighth Post Description', user=u3)
    p9 = Post(title='Ninth Post', description='Ninth Post Description', user=u4)
    p10 = Post(title='Tenth Post', description='Tenth Post Description', user=u1)

    db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
    db.session.commit()

    
    g1 = Group(name='Group 1')
    g2 = Group(name='Group 2')
    g3 = Group(name='Group 3')
    g4 = Group(name='Group 4')
    g5 = Group(name='Group 5')

    db.session.add_all([g1, g2, g3, g4, g5])
    db.session.commit()

    # Associate users with groups
    u1.groups.append(g5)
    u1.groups.append(g2)
    
    g5.users.append(u2)
    g2.users.append(u5)
    g4.users.append(u3)
    g4.users.append(u1)

    # Commit changes to the database
    db.session.commit()
