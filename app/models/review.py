from .db import db
from .solved import Solved
from .review_problem import Review_Problem


class Review(db.Model):
    __tablename__ = 'reviews'

    # id, users_id, problems_id
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    problems_id = db.Column(db.Integer, db.ForeignKey(
        "problems.id"), nullable=False)

    user = db.relationship(
        "User", secondary=Review_Problem, back_populates="reviews")
    problem = db.relationship(
        "Problem", secondary=Solved, back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "users_id": self.users_id,
            "problems_id": self.problems_id,
        }
