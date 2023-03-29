import speech_recognition as sr
import pyautogui as pg
import os
from time import *
import webbrowser as wb
import pyttsx3 as pt
import mysql.connector as sql
import datetime as dt


def speak(str):

    eg=pt.init()

    voice=eg.getProperty("voices")

    eg.setProperty("voice",voice[1].id)

    eg.setProperty("rate",160)

    eg.say(str)
    
    eg.runAndWait()

#######################################################################################################################################################################

#VOICE
  
def voice():
    pg.hotkey("winleft")
    sleep(1)
    pg.typewrite("voice\n",0.2)
    sleep(1)
            
    cord1=pg.locateCenterOnScreen("D://CS//BOARD//record.PNG")
    pg.click(cord1)
        
    


#######################################################################################################################################################################

#POWER
    
def shutdown():
    os.system("shutdown /s /t 1")
    speak("Shutting Down Computer")


#######################################################################################################################################################################

#WRITE

def write():
    notepad=sr.Recognizer()
    pg.hotkey("winleft")
    sleep(1)
    pg.typewrite("note\n",0.1)
    sleep(1)
    speak("what do u want me to take down?")
    with sr.Microphone() as source:
        notes=notepad.listen(source)
        words=notepad.recognize_google(notes)
        pg.typewrite(words,0.1)
    

#######################################################################################################################################################################

#GOOGLE
        
def google(query):

    goog=sr.Recognizer()

    soup=BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/'+query).text,"lxml")

    text=""
    textesh=""
    res="y"
    data=soup.find_all('p')
    for i in data:
        text+=" "+i.text
    
    if("may refer to" in text[0:20]):
        speak("there are many types of "+query+"'s "+"which i can provide you with, Its better if you chose, "+query+" webpage coming right up")
        url="https://www.google.com/search?q="
        wb.open_new(url+query)

    elif("Other reasons" in text[0:100]):
        url="https://www.google.com/search?q="
        wb.open_new(url+query)
        
    else:
        while res=="y":
            for j in text:
                if(j=="."):
                    res="n"
                    break
                else:
                    textesh+=j
            print(textesh)            
            speak(textesh)
            speak("do you still want me to open the page")
            with sr.Microphone() as source:
                yorn=goog.listen(source)
                yornesh=goog.recognize_google(yorn)
                if(yornesh.lower()=="yes"):
                    speak("webpage coming up right away")
                    url="https://www.google.com/search?q="
                    wb.open_new(url+query)
                else:
                    speak("ok you got it")
            

#######################################################################################################################################################################

#SONGS

def song(song_name):
    os.startfile("C://Users//NEW//AppData//Roaming//Spotify//Spotify.exe")
    sleep(5)
    pg.hotkey("ctrl","l")
    pg.typewrite(song_name,0.1)
    sleep(1)
    pg.press("Enter")
    pg.press("tab")
    pg.press("Enter")
    sleep(1)
    pg.press("Enter")

                    
#######################################################################################################################################################################

#OPENNING APP

def launch(open):
    pg.hotkey("winleft")
    sleep(1)
    pg.typewrite(open,0.1)
    pg.press("Enter")

def name():
    speak("Hey My name is Panda")

def hru():
    l_hru=["Im fine thanks!","How bad can a panda's life be?","Perfectly fine and ready to help you"]
    speak(r.choice(l_hru))

def remember():
    reminder=open("reminder.txt","a+")
    reminder.write(get1[19:]+"\n")
    reminder.close()
    speak("reminder has been set")

def ifremember():
    reminder=open("reminder.txt","a+")
    reminder.write(get1[18:]+"\n")
    reminder.close()
    speak("reminder has been set")

def read_remember():
    rem_read=open("reminder.txt","r")
    reminds=rem_read.readlines()
    if(len(reminds)==0):
        speak("Your Up to date!,you have no reminders")

    else:
        for i in reminds:
            speak(i)
            print(i)
            
    rem_read.close()

def clear():
    f=open("reminder.txt","w")
    f.write("")
    f.close()
    speak("all reminders have been cleared")

def joke():
    jokesh=["Im a big fan of whiteboards. I find them quite re-markable.","I asked my French friend if she likes to play video games. She said, vee","Don’t trust atoms, they make up everything.","eBay is so useless. I tried to look up lighters and it gave me 13,749 matches.","Trying to write with a broken pencil is pointless"]
    speak(r.choice(jokesh))

#FRONT END
print("####################################################################")
print("READ THE TEXT FILE TO CALRIFY ANY DOUBTS YOU HAVE IN THE COMMANDS")
print("####################################################################")


try:
    try:
        f=open("name.txt","r")
        namesh=f.readlines()
        speak("Hey "+namesh[0]+" just wake me up to start using me")
        f.close()
    except IndexError:
        speak("Hey im Panda!...What do you want me to call you?")
        name=input("Enter Your nickname")
        f=open("name.txt","w")
        f.write(name)
        speak("Done!...I will call you")
        speak(name)
        f.close()
            

except FileNotFoundError:
    speak("Hey im Panda!...What do you want me to call you?")
    name=input("Enter Your nickname")
    f=open("name.txt","w")
    f.write(name)
    speak("Done!...I will call you")
    speak(name)
    f.close()

r1=sr.Recognizer()
r2=sr.Recognizer()

res="y"

while res=="y":
    
    resesh="y"
    
    try:
        
        with sr.Microphone() as source:
            
            audio=r2.listen(source)
            callesh=r2.recognize_google(audio)
            call=callesh.lower()
            print(call)
            
            if("wake up panda" in call):
                speak("Hey how can i help")
                print("Hey how can i help")
                while resesh=="y":
        
                    
                    try:
                        
                        with sr.Microphone() as source1:
                            
                            audio1=r1.listen(source1)
                            get=r1.recognize_google(audio1)
                            get1=get.lower()
                            print(get1)
                            
                            if(get1.startswith("panda")):
                                
                                print(get1)
                                
                                if("record" and "voice" in get1):
                                    speak("Recording Voice")
                                    voice()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")

                                elif("google" in get1):
                                    speak("Just a moment")
                                    google(get1[13:])
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")

                                
                                elif("take down" in get1 or "take notes" in get1):
                                    speak("Opening Notepad")
                                    write()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")
                                
                                elif("play" and "game" in get1):
                                    speak("Starting Game")
                                    game()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")
                                    
                                elif("open" in get1):
                                    speak("launching"+get1[12:])
                                    launch(get1[11:])
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")

                                elif("close" in get1):
                                    speak("Closing"+get1[11:])
                                    close(get1[12:])
                                    print("\t\t\tpanda proccessing...")
                                    sleep(1)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")

                                elif("spotify" in get1):
                                    speak("playing" + get1[14:])
                                    song(get1[14:])
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")
                                    
                
                                elif("next" in get1 or "next song" in get1):
                                    next()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")
                                
                                elif("previous" in get1 or "previous song" in get1):
                                    previous()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")

                                elif("stop" in get1 or "stop song" in get1):
                                    pause()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")
                                    
                                elif("resume" in get1 or "resume song" in get1):
                                    play()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")
                                    
                                elif("+" in get1):
                                    add()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")

                                elif("-" in get1):
                                    sub()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")

                                elif("into" in get1):
                                    mult()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")

                                elif("divided by" in get1):
                                    div()
                                    print("\t\t\tpanda proccessing...")
                                    sleep(3)
                                    print("\t\t\tPANDA ready!")
                                    speak("panda ready")

                                else:
                                    print("dsdf")
                                    speak("i didnt quite catch that")
                                
                                
                                
                            else:
                                print("HEY")
                                speak("i didnt quite catch that!")

                    except ValueError:
                        continue
    except ValueError:
        continue
