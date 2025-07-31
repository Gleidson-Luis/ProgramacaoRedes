from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/validar_mac', methods=['POST'])
def validar_mac():
    mac = request.json.get('mac')
    
    if not mac:
        return jsonify({'valido': False, 'erro': 'MAC não fornecido'})
    
    # Regex para MAC Address (formato AA:BB:CC:DD:EE:FF)
    padrao = r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
    valido = bool(re.match(padrao, mac))
    
    return jsonify({'valido': valido})

if __name__ == '__main__':
    app.run(debug=True)