def language2voice(language,gender):
    """
    Given in input a language and a gender, this function returns the corresponding 
    voice in the Azure text-to-speech service.
    In case no mapping is found, the voice is set to 'en-US-JennyNeural'.
    """
    if language == 'it-IT' and gender == 'male':
        voice = 'it-IT-BenignoNeural'
    elif language == 'it-IT' and gender == 'female':
        voice = 'it-IT-ElsaNeural'
    elif language == 'de-CH' and gender == 'male':
        voice = 'de-CH-JanNeural'
    elif language == 'de-CH' and gender == 'female':
        voice = 'de-CH-LeniNeural'
    elif language == 'pt-PT' and gender == 'male':
        voice = 'pt-PT-DuarteNeural'
    elif language == 'pt-PT' and gender == 'female':
        voice = 'pt-PT-FernandaNeural'
    else:
        voice = 'en-US-JennyNeural'

    return voice