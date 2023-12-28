import random


Hello = ("hello","hi","hey","heya")
reply_hello=("Hello sir!!","hi sir","hello how are you doing sir")

gd_mrng = ("morning")
mrng_reply=("A very good morning sir ","good morning sir","morning sir hope you have a nice day")

gd_eve = ("evening")
eve_reply = ("A very good evening sir","Hope you had ur evening tea sir","Good evening sir")

gd_aft = ("afternoon")
aft_reply = ("A very good afternoon sir","Good afternoon sir")

que = ("how are you jarvis","are you ok jarvis","are you ok","how are you","how are you feeling jarvis")
que_reply =("for you always at my best sir","absolutely in working condition sir","waiting for ur orders sir")

gd_nig=("night")
nig_reply=("Good night sir","night sir hope you sleep well.")

sorry_reply = ("sorry sir but could u please repeat","recognition problem...","please try to reduce noise in the background")

functions = ("what","tell")
functions_reply = ("I am currently under development process and my schedule says i am being designed to make this system totally voice automated","ill try to do my best to work according to your orders given under certain defined boundaries..")


def chatterbox(text):
    text = str(text)
    for word in text.split():
        if word in Hello:
            reply = random.choice(reply_hello)
            return reply

        elif word in gd_mrng:
            reply = random.choice(mrng_reply)    
            return reply

        elif word in gd_eve:
            reply = random.choice(eve_reply)    
            return reply
        
        elif word in gd_aft:
            reply = random.choice(aft_reply)    
            return reply

        elif text in que:
            reply = random.choice(que_reply)    
            return reply

        elif word in gd_nig:
            reply = random.choice(nig_reply)  
            return reply  

        elif word in functions:
            reply = random.choice(functions_reply)    
            return reply

        else :
            reply = random.choice(sorry_reply)    
            return reply
        

value = chatterbox('what')
print(value)
