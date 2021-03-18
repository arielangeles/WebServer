from flask import Flask, jsonify, request
from http import HTTPStatus
from validators import validate_key_parse

app = Flask(__name__)

messages = {
    1: 'Hola',
    2: 'Mundo'
}

@app.route('/messages/', methods=['GET'])
def get_messages():
    return jsonify(messages), HTTPStatus.OK

@app.route('/messages/', methods=['POST'])
def create_message():
    if request.is_json:
        data = validate_key_parse(request.json)

        if data:
            messages.update(data)
            return jsonify(data), HTTPStatus.OK

        return jsonify(
            {'Error': f'Key must be a valid numerical string'}
        ), HTTPStatus.BAD_REQUEST

    return jsonify(
        {'Bad request': 'Content-Type must be application/json'}
    ), HTTPStatus.BAD_REQUEST

@app.route('/messages/<int:message_id>', methods=['PUT'])
def edit_message(message_id):
    if message_id in messages:
        if request.is_json:
            data = validate_key_parse(request.json)

            if data and message_id in data.keys() and len(data) == 1:
                messages.update(data)
            else:
                return jsonify({'Error': 'Invalid data'})
        else:
            message = request.data.decode()
            messages[message_id] = message

        return jsonify(messages), HTTPStatus.OK

    return jsonify({'Error': 'Invalid Message Id'}), HTTPStatus.BAD_REQUEST

@app.route('/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    if message_id in messages:
        messages.pop(message_id)

        return jsonify(messages), HTTPStatus.OK

    return jsonify({'Error': 'Invalid Message Id'}), HTTPStatus.BAD_REQUEST


if __name__ == '__main__':
    app.run()