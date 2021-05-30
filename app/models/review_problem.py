from .db import db
from .solved import Solved


class Review_Problem(db.Model):
    __tablename__ = 'review_problem'

    id = db.Column(db.Integer, primary_key=True)
    review_problems = db.Column(db.Boolean, nullable=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    problems_id = db.Column(db.Integer, db.ForeignKey(
        "problems.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "review_problems": self.review_problems,
            "users_id": self.users_id,
            "problems_id": self.problems_id
        }
