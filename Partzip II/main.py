import json
import threading
score=0
x=0
def show_verb(verb):
    global score
    #print("Czasownik po polsku: ", verb["czasownik"])
    while True:
        answer=input("Prasens: ")
        if answer==verb["a"]:
            score+=1
            print("Dobrze")
            break
        else:
            print("Prasens: ",verb["a"])
    while True:
        answer = input("Imperfekt: ")
        if answer == verb["b"]:
            score += 1
            print("Dobrze")
            break
        else:
            print("Imperfekt: ", verb["b"])

    while True:
        answer = input("Partzip II: ")
        if answer == verb["c"]:
            score += 1
            print("Dobrze")
            break
        else:
            print("Partzip II: ", verb["c"])
def showed_verb(verb):
    print("Czasownik po polsku: ", verb["czasownik"])
    #a=input()
    #if a=="":
        #print("Prasens: ",verb["a"])
    #a = input()
    #if a =="":
        #print("Imperfekt: ",verb["b"])
    #a = input()
    #if a =="":
        #print("Partzip II: ",verb["c"])

with open("part.json") as json_file:
    verbs=json.load(json_file)
while True:
    for i in range(0, len(verbs)):
        showed_verb(verbs[i])
        show_verb(verbs[i])
    print("Wynik: ",score)
    end=input("Chcesz zakończyć? Y/N: ")
    if end=="y":
        break
    else:
        continue


