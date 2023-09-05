

'''
chatbot 
question:: answer
'''
import time 
now=time.ctime()
qna={
     "Hi":"Hey",
     "How are You":"I am fine",
     "What is your name":"My name is Vasu",
     "How old are you?":"I am 21 years old",
     "What is the time now" :now
     }

while True:
    qs=input()
    
    if(qs=="quit"):
        break
    else:
        print(qna[qs])
    