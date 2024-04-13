# Google Gemini Powered-Voice Chatbot on Raspberry Pi

Previously, I built a voice assistant (chatbot) with Raspberry Pi, Python, and OpenAI ChatGPT API. In this project, I changed it to use Google's Gemini API. This version has been tested on Raspberry Pi 4 model B. The no-LED version of the code (GVA4Pi1_NoLED.py) works on both Raspberry Pi and Windows. 

Following the YouTube video below to learn more about this code:     
https://youtu.be/BQuYTOirVy4

## Materials 

1. Raspberry Pi (https://amzn.to/4bmstJa)
2. microSD card (https://amzn.to/4ay0HbY)
2. Audio amplifier (https://amzn.to/3JjPWy9)
3. USB Microphone (https://amzn.to/3HGGSCA) 
4. Mini speaker (https://amzn.to/3TB9Pp3)    
5. (optional) LEDs and resistors (https://amzn.to/3Jg4Yoz)     

## Set System Environment Variables 

GOOGLE_API_KEY=(API key from Google)   
PYGAME_HIDE_SUPPORT_PROMPT=hide

## Install Python and Packages 
You will need to install the following packages to run this code: 

```console
pip install -q -U google-generativeai
pip install speechrecognition gtts pygame gpiozero
```
   
If you have Python 3.12 or newer, also install the "setuptools" package,       

```console
pip install setuptools
```    

You may need to create a Python virtual environment first.        

\* As a participant in the Amazon Associate Program, we earn from qualifying purchases.  
