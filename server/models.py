from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name')
    def validate_name(self, key, name_entry):
        if name_entry and not Author.query.filter_by(name = name_entry).first():
            return name_entry
        raise ValueError #constructs class with no args
            
    @validates('phone_number')
    def validate_phone_number(self, key, number):
        print (f'len: {len(number)}')
        if len(number) == 10 and number.isdigit():
            return number
        print('fail')
        raise ValueError('asdf')

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('title')
    def validate_title(self, key, title):
        buzzwords = ["Won't Believe",
                    "Secret",
                    "Top",
                    "Guess"]
        for word in buzzwords:
            if word in title:
                return title
        # [return title for word in buzzwords if word in title]
        raise ValueError

    @validates('content')
    def validate_content(self, key, content):
        if len(content) >= 250:
            return content
        raise ValueError

    @validates('category')
    def validate_category(self, key, category):
        if category == "Fiction" or category == "Non-Fiction":
            return category
        raise ValueError
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) <= 250:
            return summary
        raise ValueError

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
