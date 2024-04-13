# Google-Gemini-Powered-Voice-Chatbot-on-Raspberry-Pi

Previously, I built a voice assistant (chatbot) with Raspberry Pi, Python, and OpenAI ChatGPT API. In this project, I changed it to use Google's Gemini API. This version has been tested on Raspberry Pi 4. 

Following the YouTube video here to learn more about this code:    

The no-LED version of the code (GVA4Pi1_NoLED.py) works on both Raspberry Pi and Windows. 

## Materials 

* Raspberry Pi    
* microSD card     
* Speaker   
* Microphone (https://www.microcenter.com/product/613575/adafruit-industries-mini-usb-microphone-black)   
* LEDs (optional)      
* 200Ω resistors (optional)      

## Set System Environment Variables 

GOOGLE_API_KEY=(API key from Google)   
PYGAME_HIDE_SUPPORT_PROMPT=hide

## Install Python and Packages 
You will need to install the following packages to run this code: 

```console
$ pip install -q -U google-generativeai
$ pip install speechrecognition gtts pygame gpiozero
```
