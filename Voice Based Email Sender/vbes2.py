#importing the libraries r
from tkinter import *               #creates a gui
from PIL import ImageTk, Image      #used to include images to the python program
import speech_recognition as sr     #used to recognise what the user says for further action
import pyttsx3                      #used to convert text to speech
import smtplib                      #used to send email to the defined id
import time as t                    #used for delay betweens two sentence 


def speak(c):                       #this function is used to covert the text to speech
    e = pyttsx3.init()
    e.say(c)
    e.runAndWait()

r = sr.Recognizer()

def click():
    o = smtplib.SMTP("smtp.gmail.com", 587)
    o.starttls()
    o.login("visualspprt@gmail.com", "Help@123")
    speak("Welcome to the voice recognition mail service")
    t.sleep(1)
    speak("You can give me command to send mail")
    while(1):
        try:
            with sr.Microphone() as st:
                r.adjust_for_ambient_noise(st,duration=0.2)
                speak("hello,  how may i help you")
                a2 = r.listen(st)
                mt = r.recognize_google(a2)
                mt = mt.lower()
                #print(f"Did you said '{mt}'?")
                if "send" in mt:
                    speak("ok, what is the recipents id")
                    a2 = r.listen(st)
                    mt = r.recognize_google(a2)
                    re = mt.replace(" ","") + "@gmail.com"
                    recipent = [re]
                    speak("ok, got it, what should be the subject of your mail")
                    a2 = r.listen(st)
                    mt = r.recognize_google(a2)
                    subject = mt
                    speak("ok, what is the message you want to send")
                    a2 = r.listen(st)
                    mt = r.recognize_google(a2)
                    body = mt
                    message = f"Subject:{subject}\n\n{body}"
                    o.sendmail("Visual Suport", recipent, message)  
                    o.quit()
                    speak("email successfully sent")         
                if "exit" in mt:
                    speak("Thanks for using our service, hope you liked it Please provide your valuable feedback on our mail, visualspprt@gmail.com, have a great day ")
                    break
        except Exception as e:
            print(e)
            speak(f"Sorry, i was unable to hear you")
            t.sleep(0.4)
            speak("Could you please repeat yourself")
             
def main():
    root = Tk()
    root.title(" Voice based Email service for visually challenged people")
    root.geometry("1000x900+10+10")
    root.configure(bg="white")
    img = ImageTk.PhotoImage(Image.open("micro.png"))
    Button(root, image=img, border=0, command=click).place(relx=0.5, rely=0.5, anchor=CENTER)
    Button(root, text="Exit", command=root.quit).pack(side=BOTTOM)
    root.mainloop() 

if __name__ == "__main__":
    main()