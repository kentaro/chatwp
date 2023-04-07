import chatwp

index = chatwp.load_index()

import os
import yaml

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

PORT = 3333
CORS(app, origins=[f"http://localhost:{PORT}", "https://chat.openai.com"])

@app.route('/.well-known/ai-plugin.json')
def serve_manifest():
    return send_from_directory(os.path.dirname(__file__), 'ai-plugin.json')

@app.route('/openapi.yaml')
def serve_openapi_yaml():
    with open(os.path.join(os.path.dirname(__file__), 'openapi.yaml'), 'r') as f:
        yaml_data = f.read()
    yaml_data = yaml.load(yaml_data, Loader=yaml.FullLoader)
    return jsonify(yaml_data)

@app.route('/logo.png')
def serve_logo():
    return send_from_directory(os.path.dirname(__file__), 'logo.png')

@app.route('/query', methods=['POST'])
def query():
  data = request.get_json()
  output = chatwp.execute_query(index, data['query'], 5)
  return jsonify({"output": output.response})

if __name__ == '__main__':
    app.run(port=PORT)
