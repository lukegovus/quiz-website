from app import db

#initial version of database will store passwords. Store hashes later?
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(64))
    admin = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String(128), unique = True)
    category = db.Column(db.String(32), unique = True)
    num_pres = db.Column(db.Integer)

    def __repr__(self):
        return '<Question {}>'.format(self.question)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    answer = db.Column(db.String(32), unique = True)

    def __repr__(self):
        return '<Answer {}>'.format(self.answer)


#when assigning answers to questions make sure correct answers are specified
    #potential to cause error of no correct answers
class QuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))
    correct = db.Column(db.Boolean, default = False)
    num_picked = db.Column(db.Integer)
    
    #unsure if this will work with id
    def __repr__(self):
        return '<QuestionAnswer {}>'.format(self.id)



    



       