from flask import Flask, request

from helper_functions.openai_api import chat_completion, create_image, transcript_audio
from helper_functions.twilio_api import send_twilio_message, send_twilio_photo

app = Flask(__name__)

@app.route('/')
def handle_home():
    return 'OK', 200

@app.route('/twilio', methods=['POST'])
def handle_twilio():
    data = request.form.to_dict()
    sender_id = data['From']
    if 'MediaUrl0' in data.keys():
        query = transcript_audio(data['MediaUrl0'])
        response = chat_completion(query)
        send_twilio_message(response, sender_id)
    else:
        query = data['Body']
        words = query.split(' ')
        if words[0] == '/ask':
            query = ' '.join(words[1:])
            response = chat_completion(query)
            send_twilio_message(response, sender_id)
        elif words[0] == '/img':
            query = ' '.join(words[1:])
            response = create_image(query)
            send_twilio_photo('Here is your generated image.', sender_id, response)
    return 'OK', 200
