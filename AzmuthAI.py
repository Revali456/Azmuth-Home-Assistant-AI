
import openai
import pyttsx3
import speech_recognition as sr

# Set up OpenAI API key
openai.api_key = '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'

# Set up Text-to-Speech engine
engine = pyttsx3.init()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def speak(response):
    engine.say(response)
    engine.runAndWait()

def ask_openai(query):
    response = openai.completions.create(
        model="text-davinci-003",
        prompt=query,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

def main():
    print("Hello, I am Azmuth. How can I assist you today?")
    
    while True:
        user_query = listen()
        
        if user_query:
            if user_query.lower() == 'exit':
                print("Goodbye!")
                break
            
            chatgpt_response = ask_openai(user_query)
            print(f"Azmuth: {chatgpt_response}")
            speak(chatgpt_response)

if __name__ == "__main__":
    main()
