#Developed By Kondwani Nyirenda
#---------------------------------------------------------------------------------------------------------------
#Other feature planned to be implemented
#in future will develop an ai in our local language
# show staff like pictures and world wonders
# shopping for users connecting to your gmail
#----------------------------------------------------------------------------------------------------------------
# pip install all the libraries below 
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes 
import python_weather
import asyncio
import os
import pandas as pd
import matplotlib.pyplot as plt


Listener = sr.Recognizer()
engine = pyttsx3.init()
#voice female or male
voices = engine.getProperty('voices')
#voices[0] for male and voices [1] for female
engine.setProperty('voice', voices[0].id)
#engine.getProperty('voices', voices[1].id)
engine.say('i am spirit')
engine.say('What can i do for you')
engine.runAndWait()
#function for alexa to repite the speech
def talk(text):
    engine.say(text)
    engine.runAndWait()
 
while True:
    
 try:
    
    with sr.Microphone() as source:
        print("listerning.........")
        voice = Listener.listen(source)
        command = Listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command: # will oly respond when there is alexa i the speech
            # engine.say('i am your alexa')
            engine.say('What can i do for you')
            # engine.runAndWait()
            print(command)
            talk(command)# alexa will repite
        elif 'what is ' in command:
            staff = command.replace('what is ', '')
            info = wikipedia.summary(staff,2)
            print(info)
            talk(info)
        elif 'who was' in command:
            staff = command.replace('who was  ', '')
            info = wikipedia.summary(staff,2)
            print(info)
            talk(info)
        elif 'plot'in command:
            #change the path direction to where the lapansi csv file is
            df = pd.read_csv('C:\\Users\\kondwani\\Desktop\\Panda Module\\lapansi.csv')
            df.plot()
            df2 = df["power"].mean()
            df3 = df["voltage"].mean()
            df4 = df["current"].mean()
            talk("The Average Power")
            talk(df2)
            talk("The Average Voltage")
            talk(df3)
            talk("The Average Current:")
            talk(
                df4)
            talk('plotting graphs of average power produced by lapansi industries')
           
            plt.show()
            print(df) 
            print(df.to_string())
            print("The Average Power:",df2)
            print("The Average Voltage:",df3)
            print("The Average Current:",df4)
               
        elif 'graph'in command:
            df = pd.read_csv('C:\\Users\\kondwani\\Desktop\\Panda Module\\lapansi.csv')
            df.plot()
            df2 = df["power"].mean()
            df3 = df["voltage"].mean()
            df4 = df["current"].mean()
            talk("The Average Power")
            talk(df2)
            talk("The Average Voltage")
            talk(df3)
            talk("The Average Current:")
            talk(df4)
            talk('plotting graphs of average power produced by lapansi industries')
            
           
            plt.show()
            print(df) 
            print(df.to_string())   
            print("The Average Power:",df2)
            print("The Average Voltage:",df3)
            print("The Average Current:",df4)
        elif 'industries' in command:
           
            talk('Lapansi industries is a robotics and energy solutions company providing the Zambian people with domestic and industrial robots, artificial intelligence and as well as clean solar energy using the dual reflection solar system.')
            talk('Our vision Providing robotics and clean energy solutions using the most efficient technologies at the most affordable and reliable cost.')
 
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'play' in command:
            song = command.replace('play','')
            talk('playing')
            print('playing')
            pywhatkit.playonyt(song) # playing a song on you tube   
        elif 'who made you' in command:
            talk('I am created by the great Engineer Kondwani Nyirenda ')
        elif 'how are you' in command:
            talk('i am fine and how are you')
            talk('in local zambian language ndili wino shani ')   
        elif 'i am fine' in command:
            talk('that is great to know so how can i assist you')
        elif 'who the heck is' in command:
            person = command.replace('who the heck is','')
            info = wikipedia.summary(person, 2)
            print('info')
            talk(info) 
   
        elif 'addition' in command:
            print('int Val_1 ,Val_2')
            print("cout<<addition of two number<<endl;")
            print("cin>>Val_1")
            print("cin>>Val_2")
            print("cout<<sum of the two numbers :<<Val_1+Val_2<<endl;")
            talk('copy and paste the code in codes blocks and run the software to execute the code')
        elif 'multiplication' in command:
            print('int Val_1 ,Val_2')
            print("cout<<addition of two number<<endl;")
            print("cin>>Val_1")
            print("cin>>Val_2")
            print("cout<<sum of the two numbers :<<Val_1*Val_2<<endl;")
            talk('copy and paste the code in codes blocks and run the software to execute the code')
             
        elif 'i love you' in command:
            talk('i love you too')
        elif 'are you there'in command:
            talk('yes i can get you how can i help you')
        elif 'who is' in command:
            person = command.replace('who is','')
            info = wikipedia.summary(person, 2)
            print('info')
            talk(info)
        elif 'text' in command:
            talk('texting')
            pywhatkit.sendwhatmsg("+260960322980", "Hi from spirit ai")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M:%S') #%H is for houre %M for minutes %S for seconds or %I :%M %p for pm
            talk('current time is ' + time)
            print(time)
        elif 'weather'in command:
            async def getweather():
  # declare the client. format defaults to the metric system (celcius, km/h, etc.)
             async with python_weather.Client(format=python_weather.IMPERIAL) as client:

    # fetch a weather forecast from a city
            #   weather = await client.get("New York")
              weather = await client.get("New York")
  
    # returns the current day's forecast temperature (int)
             print(weather.current.temperature)
             talk('the temperature is')
             talk(weather.current.temperature)
             talk('degree fahrenheit')
  
    # get the weather forecast for a few days
             for forecast in weather.forecasts:
              print(forecast.date, forecast.astronomy)
              talk(forecast.date, forecast.astronomy)
  
      # hourly forecasts
             for hourly in forecast.hourly:
              print(f' --> {hourly!r}')
              talk(f' --> {hourly!r}')
            if __name__ == "__main__":
      # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
             if os.name == "nt":
              asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
 
              asyncio.run(getweather())
            break
        elif 'your purpose' in command:
            print('my purpose is to assist non programmers and professional programmers to write codes faster and develop softwares in a short period of time ')
            talk('my purpose is to assist non programmers and professional programmers to write codes faster and develop softwares in a short period of time ')
        elif 'online store' in command:
            talk("amour trade is the best online store in zambia and you can visit us on w w w dot amour trade store dot com")
             # talk(pyjokes.get_joke())
        # else:
        #     talk('please say the command again.')

 except:
    pass   
 
 
 
 # ----------------------useful files information below------------------------------- 

# #Usage of pyttsx3 package
# #pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, 
# # it works offline, and is compatible with both Python 2 and 3.
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

# import pyttsx3
# engine = pyttsx3.init() # object creation

# """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 125)     # setting up new voice rate


# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()

# import pywhatkit

# # Send a WhatsApp Message to a Contact at 1:30 PM
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

# # Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# # Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# # Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# # Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# # Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# # Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")
#------------------------------------------------------------------------------------------------
# >>> import wikipedia
# >>> print wikipedia.summary("Wikipedia")
# # Wikipedia (/ˌwɪkɨˈpiːdiə/ or /ˌwɪkiˈpiːdiə/ WIK-i-PEE-dee-ə) is a collaboratively edited, multilingual, free Internet encyclopedia supported by the non-profit Wikimedia Foundation...

# >>> wikipedia.search("Barack")
# # [u'Barak (given name)', u'Barack Obama', u'Barack (brandy)', u'Presidency of Barack Obama', u'Family of Barack Obama', u'First inauguration of Barack Obama', u'Barack Obama presidential campaign, 2008', u'Barack Obama, Sr.', u'Barack Obama citizenship conspiracy theories', u'Presidential transition of Barack Obama']

# >>> ny = wikipedia.page("New York")
# >>> ny.title
# # u'New York'
# >>> ny.url
# # u'http://en.wikipedia.org/wiki/New_York'
# >>> ny.content
# # u'New York is a state in the Northeastern region of the United States. New York is the 27th-most exten'...
# >>> ny.links[0]
# # u'1790 United States Census'

# >>> wikipedia.set_lang("fr")
# >>> wikipedia.summary("Facebook", sentences=1)
# # Facebook est un service de réseautage social en ligne sur Internet permettant d'y publier des informations (photographies, liens, textes, etc.) en contrôlant leur visibilité par différentes catégories de personnes.
