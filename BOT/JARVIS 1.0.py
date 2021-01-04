# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:30:28 2019

@author: Caio
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    
    while True:
        audio = r.listen(s)
        
        speech = r.recognize_google(audio, lang='pt')
        
        print ('Você disse:', speech)
        
        