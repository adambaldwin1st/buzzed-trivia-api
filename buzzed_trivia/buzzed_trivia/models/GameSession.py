from ..app import db
from sqlalchemy.dialects.postgresql import JSONB


class GameSession(db.Model):
    id = db.Column(db.String(4), primary_key=True)
    data = db.Column(JSONB)
