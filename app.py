from speech import recognize_from_microphone, synthetise_speech

language = 'pt-PT'
gender = 'female'
text = recognize_from_microphone(language)
synthetise_speech(text, language, gender)