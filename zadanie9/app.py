import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

class UserPrompt:
    def __init__(self, prompt):
        self.prompt = prompt

class ChatResponse:
    def __init__(self, response):
        self.response = response

def query_llama2(prompt: str) -> str:
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama2'],
            input=prompt.encode('utf-8'),
            capture_output=True,
            check=True
        )
        return result.stdout.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ollama error: {e}")

@app.route('/chat', methods=['POST'])
def post_prompt_to_llama():
    data = request.get_json()
    user_prompt = data.get('prompt')

    if not user_prompt:
        return jsonify({'error': 'No message provided'}), 400

    try:
        llama2_response = query_llama2(user_prompt)
        response = ChatResponse(response=llama2_response)
        return jsonify(response.__dict__)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
