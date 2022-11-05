# ChatBotTask
# This is Basic Chatbot which works for basic addition,subraction,division,mul
from random import randint
def greet_random():
    greetings=['hi','hello','vannakam','howdy']
    return greetings[randint(0,len(greetings)-1)]

greetings = greet_random()
q = ['quit','bye','exit']
print(greetings,"I'm Thanush, what is your query? if you want to quit ,type quit")
while True:
    msg = input()
    if msg in q:
        break
    elif "add" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        y = float(split_msg[2])
        print(x+y)
    elif "mul" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        y = float(split_msg[2])
        print(x*y)
    elif "sub" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        y = float(split_msg[2])
        print(x-y)
    elif "div" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        y = float(split_msg[2])
        print(x/y)
    elif "square" in msg:
        print(msg)
        split_msg= msg.split()
        print(split_msg)
        x = float(split_msg[1])
        print(x**2)
