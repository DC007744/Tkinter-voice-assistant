import pyttsx3
import speech_recognition as sr
from datetime import date, time, datetime
import wikipedia
import webbrowser
from time import sleep
from tkinter import Label, Button, Grid, mainloop, Pack, Tk, PhotoImage, INSERT, Message
from tkinter import font as tkFont
from threading import Thread


#MODULE VARIABLES
root = Tk()                                 #tkinter
root.geometry("700x350+560+150")
root.resizable(width=False, height=False)
root.title('Voice Assistant')

engine = pyttsx3.init()                     #pyttsx3
r = sr.Recognizer()                         #SpeechRecognition



#IMAGE VARIABLES
background_image = PhotoImage(file = r"C:\Users\Dipesh\OneDrive\Desktop\Visual Studio Code\ai\bg1.png")
background_label = Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.pack()

btnbrd = PhotoImage(file = r"C:\Users\Dipesh\OneDrive\Desktop\Visual Studio Code\ai\bored_btn_bg2.png")
shopPic = PhotoImage(file = r"C:\Users\Dipesh\OneDrive\Desktop\Visual Studio Code\ai\shop1.png")
photo = PhotoImage(file = r"C:\Users\Dipesh\OneDrive\Desktop\Visual Studio Code\ai\micro2.png")



#GLOBAL VARIABLES
query = ''
usrQ = ''



#FONT VARIABLES
helv = tkFont.Font(family='Franklin Gothic Book', weight='bold')
chat_font = tkFont.Font(family='Courier New', size=12)
button_font = tkFont.Font(family='Cambria Math', size=10)



#PREDEFINED LABELS
l2 = Message(root, text='', width=226)
l2.pack()

l3 = Message(root, text='', width=226)
l3.pack()

l4 = Label(root, text='', font=chat_font)
l4.pack()



class Win1:

    def speak(self, text):
        l1.configure(text='Status: Active')
        l4.place(x=5, y=45)
        l4.configure(text='[MyAssistant]:')
        l2.place(x=5, y=70)
        l2.configure(text= text, font=chat_font) 
        engine.say(text)
        engine.runAndWait()


    def greet_me(self):

        self.hour = int(datetime.now().hour)
        self.greeting = ''

        if self.hour>=0 and self.hour<12 :
            self.greeting = 'Good morning!'
        elif self.hour>=12 and self.hour<18:
            self.greeting = 'Good afternoon!'
        else:
            self.greeting = 'Good evening!'

        self.speak(f'{self.greeting} I am Jarvis. How may I help you today?')


    def listen_to_me(self):
        l1.configure(text='Status: Listening...', bg='yellow')
        with sr.Microphone() as source:
            
            self.audio = r.listen(source)

            l1.configure(text='Status: Processing...', bg='yellow')
            global query
            try:
                query = r.recognize_google(self.audio, language='en-in')
                l3.place(x=5, y=140)
                l3.configure(text=f"[Me]: {query}", font=chat_font)
            except:
                if query == '':
                    self.speak("Sorry didn't quite catch that. Please repeat.")
                    self.listen_to_me()

        global usrQ
        usrQ = query
        usrQ = usrQ.lower()
        return usrQ


    def reply(self):
        self.query = self.listen_to_me()

        # Logic for executing tasks based on query
        if 'wikipedia' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            self.speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("for", "")
            results = wikipedia.summary(query, sentences=1)
            self.speak(f'According to Wikipedia, {results}')

        elif 'open youtube' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            self.speak('Opening Youtube...')
            webbrowser.open("https://youtube.com")

        elif 'open google' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            self.speak('Opening Google...')
            webbrowser.open("https://google.com")

        elif 'open stack overflow' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            self.speak('Opening StackOverflow...')
            webbrowser.open("https://stackoverflow.com")

        elif 'what' and 'time' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            self.speak(f"Sir, The time is {strTime}")

        elif 'what' and 'date' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            today = date.today()
            d2 = today.strftime("%B %d, %Y")    
            self.speak(f"Sir, The date is {d2}")

        elif 'what is the meaning of' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            
            address = "https://www.google.com/search?q="
            search_results = address + self.query

            self.query = self.query.replace('search google for', '')
            self.query = self.query.replace('google', '')
            self.query = self.query.replace('look up', '')
            self.query = self.query.replace('search the web for', '')

            self.speak("One moment...")
            sleep(1)
            self.speak("Here's what I found on the web for " + '"' + query + '"') 

            webbrowser.open(search_results)

        elif 'search the web for' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            
            address = "https://www.google.com/search?q="
            search_results = address + self.query

            self.query = self.query.replace('search google for', '')
            self.query = self.query.replace('google', '')

            self.speak("One moment...")
            sleep(1)
            self.speak("Here's what I found on the web for " + '"' + query + '"') 

            webbrowser.open(search_results)

        elif 'my name' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            self.speak('Sir, your name is Dipesh chandiramani and I am here to serve you.')
        
        elif 'how are you' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            self.speak('I am doing jolly good, sir.')
        
        elif 'what can you do' in self.query:
            l1.configure(text='Status: Displaying results', bg='yellow')
            self.speak('I can look up for definitions on wikipedia, open sites like YouTube,Google, or StackOverflow, and of course, tell the time... So what do you want me to do?')

        else:
            l1.configure(text='Status: Displaying results', bg='yellow')
            self.speak("I don't understand " + '"' + self.query + '". Do you want me to do a google search?')
            self.listen_to_me()
            if 'no' or 'nope' in self.query:
                l1.configure(text='Status:', bg='yellow')
                self.speak("Ok, Sir. I'm sorry I'm not smart enough yet but I'm learning...")

            elif 'yes' or 'yeah' or 'ok' or 'sure' in self.query:
                l1.configure(text='Status: Displaying results', bg='yellow')
                self.speak("One moment...")
                sleep(1)
                address = "https://www.google.com/search?q="
                search_results = address + self.query

                self.speak("Here's what I found on the web for " + '"' + self.query + '"') 
                webbrowser.open(search_results)


    def main_function(self):
        self.greet_me()
        self.reply()

    def start_t1(self):
        self.thread1 = Thread(target=self.main_function)
        self.thread1.start()

mainObj = Win1()


class Win2:
    def __init__(self):
        self.btnbrd = PhotoImage(file = r"C:\Users\Dipesh\OneDrive\Desktop\Visual Studio Code\ai\bored_btn_bg2.png")

    def Trigger_bored_features(self):
        import myAssistantBoredFEATURE
        myAssistantBoredFEATURE.bored()

obj2 = Win2()
thrWin2 = Thread(root, target=obj2.Trigger_bored_features)


class Win3:
    def __init__(self):
        self.shopPic = PhotoImage(file = r"C:\Users\Dipesh\OneDrive\Desktop\Visual Studio Code\ai\shop1.png")

    def Trigger_shop_features(self):
        import myAssistantShoppingFEATURE
        myAssistantShoppingFEATURE.shopping()

obj3 = Win3()
thrWin3 = Thread(root, target=obj3.Trigger_shop_features)



#WIDGETS
l1 = Label(root, text='Status: Inactive', bg='yellow')
l1.pack()
l1.place(x=5, y=5)

b1 = Button(root, text='Start', font=helv, command=mainObj.start_t1, height=58, width=42, image=photo)
b1.pack()
b1.place(x=315,y=220)

b2 = Button(root, image=btnbrd, command=thrWin2.start)
b2.image = btnbrd
b2.pack()
b2.place(x=591, y=3)

shop_button = Button(root, image=shopPic, command=thrWin3.start)
shop_button.image = shopPic
shop_button.pack()
shop_button.place(x=591, y=150)

root.mainloop()