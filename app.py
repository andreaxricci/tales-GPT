import os

from flask import Flask, request, render_template

from speech import recognize_from_microphone, synthetise_speech
from utils import generate_story, load_api_keys, language2code


#language = 'Portuguese'
#gender = 'male'
#model_name = 'gpt-3.5-turbo'
temperature = 1

load_api_keys()
openai_api_kei = os.environ.get('OPENAI_API_KEY')

#user_input = recognize_from_microphone(language2code(language))

#story = generate_story(user_input, language, model_name, temperature, openai_api_kei)

#print(story)

#synthetise_speech(story, language, gender)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    #user_input = request.form['text']
    language = request.form['language']
    gender = request.form['gender']
    model_name = request.form['model_name']

    # The user speaks into the microphone, triggering function recognize_from_microphone and passing the language code
    user_input = recognize_from_microphone(language2code(language))

    # Extract text
    story = generate_story(user_input, language, model_name, temperature, openai_api_kei)
    synthetise_speech(story, language, gender)

    # Call render template
    return render_template(
        'results.html',
        original_text=user_input,
        story=story
    )

