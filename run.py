from app import app, db
from app.controllers import default



# apartir do sqlalchemy 3 é necessario este comando
#with app.app_context():
#    db.create_all()

db.create_all()


if __name__ == "__main__":
    app.run(debug=True,port=4987)