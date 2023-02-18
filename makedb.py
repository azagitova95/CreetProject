def create_my_database():
    from app import db, app
    with app.app_context():
        db.drop_all()
        db.create_all()


# create_my_database()