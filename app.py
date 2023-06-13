import os

import streamlit as st

from speech import recognize_from_microphone, synthetise_speech
from utils import generate_story, load_api_keys, language2code


language = 'Portuguese'
gender = 'male'
model_name = 'gpt-3.5-turbo'
temperature = 1

load_api_keys()
openai_api_kei = os.environ.get('OPENAI_API_KEY')


def main() -> None:
     
    st.set_page_config(page_title="talesGPT", page_icon=":heart:")
    st.subheader("Tell me a story")

    if "button1" not in st.session_state:
        st.session_state["button1"] = False        
    
    if "button2" not in st.session_state:
        st.session_state["button2"] = False

    if "button3" not in st.session_state:
        st.session_state["button3"] = False


    if st.button("Button1"):
        # toggle button1 session state  
        st.session_state["button1"] = not st.session_state["button1"]
        try:
            with st.spinner("Recording audio..."):
                # Trigger audio recording
                user_input = recognize_from_microphone(language2code(language))
                st.write(user_input)
    
        except Exception as e:
            st.exception(f"Exception: {e}")


    if st.session_state["button1"]:
        if st.button("Button2"):
            print(f"user_input: {user_input}")
            # toggle button2 session state
            st.session_state["button2"] = not st.session_state["button2"]
            
            #story = generate_story(user_input, language, model_name, temperature, openai_api_kei)
            story = 'hello world'
            print(f"story: {story}")
            st.text(story)


    if st.session_state["button1"] and st.session_state["button2"]:
        if st.button("Button3"):
            # toggle button3 session state
            st.session_state["button3"] = not st.session_state["button3"]
            synthetise_speech(story, language, gender)


    if st.session_state["button3"]:
        st.write("End")


    # Print the session state to make it easier to see what's happening
    st.write(
        f"""
        ## Session state:
        {st.session_state["button1"]=}

        {st.session_state["button2"]=}

        {st.session_state["button3"]=}
        """
    )


if __name__ == '__main__':
    main()