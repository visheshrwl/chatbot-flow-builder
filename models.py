from app import db

class Flow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    structure = db.Column(db.JSON, nullable=False)  # Store flow in JSON format

class Intent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flow_id = db.Column(db.Integer, db.ForeignKey('flow.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    response = db.Column(db.String(500), nullable=False)
    triggers = db.Column(db.JSON, nullable=False)  # List of triggers for this intent
