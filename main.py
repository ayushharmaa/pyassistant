import speech_recognition as sr
import openai 
import pyttsx3

openai.api_key='sk-api-key'

listener=sr.Recognizer()

#initializing text to speech
engine=pyttsx3.init()
engine.say('Hey I am Jarvis,How can i help you?')
engine.runAndWait()

def openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the engine (e.g., "davinci" or "curie")
        prompt=prompt,  # Input prompt
        # max_tokens=00,  # Maximum number of tokens to generate in the response
        # temperature=0.5,
    )
    return response['choices'][0]['text']

def speak_reply(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print('Jarvis Listening...')
        with sr.Microphone() as source:
            voice=listener.listen(source)
            global command
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'jarvis' in command:
                command=command.replace('Jarvis','')
                print(command)
                response=openai_response(command)
                print('gpt response: ',response)
                speak_reply(response)

if __name__ == '__main__':
    main()


            
