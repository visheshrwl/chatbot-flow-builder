from flask import jsonify

# Create new flow
def create_flow(request, db):
    data = request.json
    new_flow = Flow(name=data['name'], structure=data['structure'])
    db.session.add(new_flow)
    db.session.commit()
    return jsonify({'message': 'Flow created successfully'}), 201

# Retrieve all flows
def get_flows():
    flows = Flow.query.all()
    return jsonify([{'id': flow.id, 'name': flow.name, 'structure': flow.structure} for flow in flows])

# Simulate chatbot response based on flow
def simulate_chat(request):
    user_message = request.json.get('message')
    flow_id = request.json.get('flow_id')
    flow = Flow.query.get(flow_id)
    if not flow:
        return jsonify({'error': 'Flow not found'}), 404
    response = simulate_flow_logic(flow.structure, user_message)
    return jsonify({'response': response})

def simulate_flow_logic(flow_structure, user_message):
    # Basic logic: find matching intent based on user message
    intents = flow_structure.get('intents', [])
    for intent in intents:
        if user_message.lower() in intent['triggers']:
            return intent['response']
    return "Sorry, I don't understand that."
