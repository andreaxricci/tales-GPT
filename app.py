import os

from speech import recognize_from_microphone, synthetise_speech

from utils import generate_story, load_api_keys, language2code

language = 'Italian'
gender = 'male'
model_name = 'gpt-3.5-turbo'
temperature = 0.8

load_api_keys()
openai_api_kei = os.environ.get('OPENAI_API_KEY')

user_input = recognize_from_microphone(language2code(language))

story = generate_story(user_input, language, model_name, temperature, openai_api_kei)

print(story)

synthetise_speech(story, language, gender)