from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json
        user_id = f"{data['first_name']}_{data['last_name']}_{data['dob'].replace('-', '')}"

        numbers = []
        alphabets = []
        for item in data.get('data', []):
            if isinstance(item, int):
                numbers.append(item)
            elif isinstance(item, str) and item.isalpha():
                alphabets.append(item)
        
        highest_lowercase = max([char for char in alphabets if char.islower()], default=None)

        response = {
            "user_id": user_id,
            "is_success": True,
            "email_id": data.get('email_id', ''),
            "roll_number": data.get('roll_number', ''),
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase": highest_lowercase,
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
