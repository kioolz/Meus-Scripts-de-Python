parte do chatbot

from chatterbot.traners import ListTrainer
from chatterbot import ChatBot





#Reconhecimento de fala

import speech_recognition as sr



#Reconhecimento de síntese

import pyttsx3

bot = ChatBot('Logo') #Inicia o bot

chats = ['Hi', 'Hello', 'How are you?', 'I''m fine.', 'thanks.']

bot.set_trainer(ListTrainer) #define o metodo
bot.train(chats)  #Define a lista de conversas

r.sr.Recognizer()


    r.adjust_for_ambient_noise(s) #Se adaptar ao ruído

    while True:
        audio = r.listen(s) #Escutar
        speech = r.recognize_google(audio) #Falar
        print(bot.get_response(request))

while True:
    request = input('Enter a text: ')
    print(bot.get_response(request))
    
