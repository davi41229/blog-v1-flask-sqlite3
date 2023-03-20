from app import db

class Blogger(db.Model):
    __tablename__ = 'blogger'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        
        
   
