document.addEventListener('DOMContentLoaded', function () {
    const flowForm = document.getElementById('flow-form');
    const sendMessageButton = document.getElementById('send-message');
    const flowSelect = document.getElementById('flow-select');

    // Fetch existing flows and populate select dropdown
    fetch('/flows')
        .then(response => response.json())
        .then(data => {
            data.forEach(flow => {
                let option = document.createElement('option');
                option.value = flow.id;
                option.textContent = flow.name;
                flowSelect.appendChild(option);
            });
        });

    // Create new flow
    flowForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const flowName = document.getElementById('flow-name').value;
        const flowStructure = document.getElementById('flow-structure').value;

        fetch('/create-flow', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: flowName, structure: JSON.parse(flowStructure) })
        })
            .then(response => response.json())
            .then(data => alert(data.message));
    });

    // Simulate chatbot conversation
    sendMessageButton.addEventListener('click', function () {
        const message = document.getElementById('user-message').value;
        const flowId = flowSelect.value;

        fetch('/simulate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message, flow_id: flowId })
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById('chat-response').textContent = data.response;
            });
    });
});
