from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/validar_mac')
def validar_mac():
    mac = {'valido': False, 'erro': 'MAC nao fornecido'}
    return jsonify(mac)
    
    # Regex para MAC Address (formato AA:BB:CC:DD:EE:FF)
    padrao = r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$'
    valido = {'valido': valido}
    return jsonify(valido)

if __name__ == '__main__':
    app.run(debug=True)