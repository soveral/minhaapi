from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_user_info(CPF):
    conn = sqlite3.connect('bundle.db')
    cursor = conn.cursor()
    cursor.execute("SELECT CPF, NOME, PESSOA, DDD, FONE, INST FROM bundle WHERE CPF = ?", (CPF,))
    result = cursor.fetchone()
    conn.close()
    return result

@app.route('/')
def index():
    return render_template('index.html')

# New GET endpoint to retrieve user data as JSON
@app.route('/get_user_info/<CPF>', methods=['GET'])
def get_user_info_get(CPF):
    user_info = get_user_info(CPF)
    if user_info:
        user_data = {
            "CPF": user_info[0],
            "NOME": user_info[1],
            "PESSOA": user_info[2],
            "DDD": user_info[3],
            "FONE": user_info[4],
            "INST": user_info[5]
        }
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

# Existing POST endpoint
@app.route('/get_user_info', methods=['POST'])
def get_user_info_route():
    CPF = request.form.get('CPF')
    user_info = get_user_info(CPF)
    if user_info:
        user_data = {
            "CPF": user_info[0],
            "NOME": user_info[1],
            "PESSOA": user_info[2],
            "DDD": user_info[3],
            "FONE": user_info[4],
            "INST": user_info[5]
        }
        return jsonify(user_data)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
