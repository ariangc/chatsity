from app import db
from models.utils import AddUpdateDelete

class BlacklistedToken(db.Model, AddUpdateDelete):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(1000))