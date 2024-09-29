from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot_flows.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Import Models and Controllers
from models import Flow, Intent
import flow_controller

# Route for Homepage (Load Frontend)
@app.route('/')
def index():
    return render_template('index.html')

# Route for creating a new flow
@app.route('/create-flow', methods=['POST'])
def create_flow():
    return flow_controller.create_flow(request, db)

# Route for retrieving all flows
@app.route('/flows', methods=['GET'])
def get_flows():
    return flow_controller.get_flows()

# Route for simulating chatbot responses
@app.route('/simulate', methods=['POST'])
def simulate_chat():
    return flow_controller.simulate_chat(request)

# Run the app
if __name__ == '__main__':
    db.create_all()  # Create database and tables if not existing
    app.run(debug=True)
