# A Voice Chatbot built with Google Gemini Pro and Python for RPi
# Tested and working on RP 4 model B. 
# By TechMakerAI on YouTube
# 
import google.generativeai as genai
import speech_recognition as sr
from datetime import date
from gtts import gTTS
from io import BytesIO
from pygame import mixer

mixer.init()
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# set the Google Gemini API key as an environment variable or here
# genai.configure(api_key= "GOOGLE_API_KEY")

today = str(date.today())

# model of Google Gemini API
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

# select to use OpenAI's text to speech API
openaitts = False     

def speak_text(text):
    
    mp3file = BytesIO()
    tts = gTTS(text, lang="en", tld = 'us') 
    tts.write_to_fp(mp3file)

    mp3file.seek(0)
    
    try:
        mixer.music.load(mp3file, "mp3")
        mixer.music.play()

        while mixer.music.get_busy():
            pass

    except KeyboardInterrupt:
        mixer.music.stop()
        mp3file.close()
    
    mp3file.close()	
    
# save conversation to a log file 
def append2log(text):
    global today
    fname = 'chatlog-' + today + '.txt'
    with open(fname, "a") as f:
        f.write(text + "\n")

# define default language to work with the AI model 
slang = "en-EN"

# Main function  
def main():
    global today, chat, model, slang
    
    rec = sr.Recognizer()
    mic = sr.Microphone()
    rec.dynamic_energy_threshold=False
    rec.energy_threshold = 400    
    
    sleeping = True 
    # while loop for conversation 
    while True:     
        
        with mic as source:            
            rec.adjust_for_ambient_noise(source, duration= 0.5)

            print("Listening ...")
            
            try: 
                audio = rec.listen(source, timeout = 20, phrase_time_limit = 30)
                text = rec.recognize_google(audio, language=slang)
                
                # AI is in sleeping mode
                if sleeping == True:
                    # User must start the conversation with the wake word "Jack"
                    # This word can be chagned by the user. 
                    if "jack" in text.lower():
                        request = text.lower().split("jack")[1]
                        
                        sleeping = False
                        # AI is awake now, 
                        # start a new conversation 
                        append2log(f"_"*40)                    
                        today = str(date.today())                         
                        chat = model.start_chat()
                        
                        # if the user's question is none or too short, skip 
                        if len(request) < 2:
 
                            speak_text("Hi, there, how can I help?")
                            append2log(f"AI: Hi, there, how can I help? \n")
                            continue                      

                    # if user did not say the wake word, nothing will happen 
                    else:
                        continue
                      
                # AI is awake         
                else: 
                    
                    request = text.lower()

                    if "that's all" in request:
                                               
                        append2log(f"You: {request}\n")
                        
                        speak_text("Bye now")
                        
                        append2log(f"AI: Bye now. \n")                        

                        print('Bye now')
                        
                        sleeping = True
                        # AI goes back to speeling mode
                        continue
                    
                    if "jack" in request:
                        request = request.split("jack")[1]                        
                
                # process user's request (question)
                append2log(f"You: {request}\n ")

                print(f"You: {request}\n AI: " )
               
                response = chat.send_message(request, stream=True,
                generation_config=genai.types.GenerationConfig(
                # Only one candidate for now.
                max_output_tokens=168 ) 
                )

                for chunk in response:
                    print(chunk.text, end='') #, flush=True)
                    speak_text(chunk.text.replace("*", ""))
                    
                #print(response.text)
                #speak_text(response.text.replace("*", ""))
                print('\n')
               
                append2log(f"AI: {response.text } \n")
 
            except Exception as e:
                continue 
 
if __name__ == "__main__":
    main()



