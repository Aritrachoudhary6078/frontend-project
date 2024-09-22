from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data')
        file_b64 = request.json.get('file_b64')

        numbers = [str(x) for x in data if str(x).isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        lowercase_alphabets = [x for x in alphabets if x.islower()]

        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

        file_valid = bool(file_b64)
        file_mime_type = "image/png"  # Example mime type
        file_size_kb = 400  # Example file size

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else [],
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
