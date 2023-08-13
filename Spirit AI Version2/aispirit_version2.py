#***************************************Developed By Eng: Kondwani Nyirenda*************************************
#---------------------------------------------------------------------------------------------------------------
#Version 2 of spirit Ai it can now do more task than before face recognition ,hand detection ,light bulds and so on
#Last Upated : 13th August ,2023
#-----------------------------------------------------------------------------------------------------------------
#------------------------------------Other feature planned to be implemented--------------------------------------
#in future will develop an ai in our local language
# image generation using Dalle ,show staff like pictures and world wonders
# shopping for users connecting to your gmail
# Controlling robots ,self driving ,energy consumption turn gerysers and lights off
# How security and facial recognition capabilitues 
# Intergration with chat gpt model  
#----------------------------------------------------------------------------------------------------------------
# pip install all the libraries below 
import speech_recognition as sr
import serial
import time
import pyttsx3
import cv2
import mediapipe as mp
import pywhatkit as kit
import wikipedia
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import threading
import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'
#----------------------------------------------the code starts here----------------------------------------------
arduino_port = 'COM3'  # Change this to your Arduino port
arduino = serial.Serial(arduino_port, 9600)
time.sleep(2)  # Wait for Arduino to initialize

def generate_code(code_text):
    # You can replace this with more complex code generation logic
    code = f'print("{code_text}")'
    return code

def control_lights(action):
    if action == "on":
        arduino.write(b'1')
    elif action == "off":
        arduino.write(b'0')
#----------------------------------------------face detection----------------------------------------------
def detect_faces(image):
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = image.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(image, bbox, (0, 255, 0), 2)

    return image
def detect_hands(image):
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    with mp_hands.Hands(min_detection_confidence=0.5) as hands:
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return image

#----------------------------------------------fruit detection----------------------------------------------
# Define class names
class_names = ['apple', 'banana']  # List of class names
# Load your trained fruit classification model
fruit_classification_model = tf.keras.models.load_model('fruit_classification_model.h5')

def detect_and_visualize_fruit(model):
    cap = cv2.VideoCapture(0)

    def close_camera():
        time.sleep(15)
        cap.release()
        cv2.destroyAllWindows()

    threading.Thread(target=close_camera).start()

    while True:
        # Initialize the camera
        # cap = cv2.VideoCapture(0)  # 0 for default camera
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess the frame for classification
        resized_frame = cv2.resize(frame, (224, 224))
        input_frame = np.expand_dims(resized_frame, axis=0)
        input_frame = input_frame / 255.0

        # Predict the fruit type
        prediction = fruit_classification_model.predict(input_frame)
        predicted_class_index = int(np.round(prediction[0][0]))
        predicted_class = class_names[predicted_class_index]

        # Draw bounding box and label on the frame
        label = f'{predicted_class} ({prediction[0][0]:.2f})'
        color = (0, 255, 0) if predicted_class == 'apple' else (0, 0, 255)
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        # Display the frame
        cv2.imshow('Fruit Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#----------------------------------------------using chat gpt----------------------------------------------
def chat_with_gpt():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("You chose to use ChatGPT. You can choose between text or voice input.")
    while True:
        print("Would you like to use text or voice? (Type 'text' or 'voice', or 'exit' to quit)")
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input == "text":
            chat_with_gpt_text()
        elif user_input == "voice":
            chat_with_gpt_voice()
        else:
            print("Invalid input. Please choose 'text', 'voice', or 'exit'.")

def chat_with_gpt_text():
    print("You chose text input. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input,
            max_tokens=50
        )
        print("ChatGPT:", response.choices[0].text.strip())

def chat_with_gpt_voice():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("You chose voice input. Speak now. Say 'exit' to quit.")
    with microphone as source:
        while True:
            print("Listening...")
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)

            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            response = openai.Completion.create(
                engine="davinci",
                prompt=user_input,
                max_tokens=50
            )
            print("ChatGPT:", response.choices[0].text.strip())

#----------------------------------------------main program----------------------------------------------
def talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #voices[0] for male and voices [1] for female
    engine.setProperty('voice', voices[0].id)
    
    engine.setProperty('rate', 130)  # Adjust the rate value as needed
    #voice female or male
    engine.say(text)
    engine.runAndWait()  

def main():
    print("Welcome to AI Spirit Version 2!")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #voices[0] for male and voices [1] for female
    engine.setProperty('voice', voices[0].id)
    
    engine.setProperty('rate', 130)  # Adjust the rate value as needed
    #voice female or male
   
    engine.say("How are you, am spirit AI here  to assist you ,how can i help you?")
    engine.runAndWait()
    model = tf.keras.models.load_model('fruit_classification_model.h5')



   

    while True:
        try:
            print("Say something...")
            talk('say something ')
           
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
            # with sr.Microphone(device_index=0) as source:
                audio = recognizer.listen(source, timeout=10)
            input_text = recognizer.recognize_google(audio)
            print(input_text)

            if "play a song" in input_text.lower():
                engine.say("Sure, playing a song on YouTube.")
                engine.runAndWait()
                query = input_text.lower().replace("play song", "").strip()
                kit.search(query)  # Opens a YouTube search page for the query

            elif "generate programming code" in input_text.lower():
                print("What code text would you like to generate?")
                engine.say("What code text would you like to generate?")
                engine.runAndWait()
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=5)
                code_text = recognizer.recognize_google(audio)
                generated_code = generate_code(code_text)
                print("Generated Code:", generated_code)
                engine.say("Code generated successfully!")
                engine.runAndWait()

            elif "turn on light" in input_text.lower():
                control_lights("on")
                print("Lights turned on.")
                engine.say("Lights turned on.")
                engine.runAndWait()

            elif "turn on light" in input_text.lower():
                control_lights("on")
                print("Lights turned on.")
                engine.say("Lights turned on.")
                engine.runAndWait()

            elif "turn off lights" in input_text.lower():
                control_lights("off")
                print("Lights turned off.")
                engine.say("Lights turned off.")
                engine.runAndWait()
            
            elif "using chat gpt" in input_text.lower():
                print("Lights turned off.")
                talk('you are now using Chat gpt')
                chat_with_gpt()

            elif "detect faces" in input_text.lower():
                cap = cv2.VideoCapture(0)
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        continue
                    frame = detect_faces(frame)
                    cv2.imshow('Face Detection', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "detect faces" in input_text.lower():
                cap = cv2.VideoCapture(0)
                start_time = time.time()
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        continue
                    frame = detect_faces(frame)
                    cv2.imshow('Face Detection', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q') or time.time() - start_time > 20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                engine.say("Face detection completed.")
                engine.runAndWait()
            elif " hand" in input_text.lower():
                cap = cv2.VideoCapture(0)
                start_time = time.time()
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        continue
                    frame = detect_hands(frame)
                    cv2.imshow('Hand Detection', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q') or time.time() - start_time > 30:
                        break
                cap.release()
                cv2.destroyAllWindows()
                engine.say("Hand detection completed.")
                engine.runAndWait()

            elif "face" in input_text.lower():
                cap = cv2.VideoCapture(0)
                start_time = time.time()
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        continue
                    frame = detect_faces(frame)
                    cv2.imshow('Face Detection', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q') or time.time() - start_time > 20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                engine.say("Face detection completed.")
                engine.runAndWait()
            elif 'what is ' in input_text.lower():
                staff = input_text.replace('what is ', '')
                info = wikipedia.summary(staff,2)
                print(info)
                engine.say(info)
                engine.runAndWait()
            elif 'who was' in input_text.lower():
                staff = input_text.replace('who was  ', '')
                info = wikipedia.summary(staff,2)
                print(info)
                engine.say(info)
                engine.runAndWait()

            elif 'plot'in input_text.lower():
                df = pd.read_csv('lapansi.csv')
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
               
            elif 'graph'in input_text.lower():
                df = pd.read_csv('lapansi.csv')
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
            elif 'power generated'in input_text.lower():
                df = pd.read_csv('lapansi.csv')
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

            elif 'power consumption'in input_text.lower():
                df = pd.read_csv('lapansi.csv')
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

            elif "detect fruit" in input_text.lower():
                engine.say("Opening camera for fruit detection...")
                engine.runAndWait()
                detect_and_visualize_fruit(model)
            elif "fruit" in input_text.lower():
                engine.say("Opening camera for fruit detection...")
                engine.runAndWait()
                detect_and_visualize_fruit(model)
            elif "food" in input_text.lower():
                engine.say("Opening camera for fruit detection...")
                engine.runAndWait()
                detect_and_visualize_fruit(model)

            elif 'industries' in input_text.lower():
                talk('Lapansi industries is a robotics and energy solutions company providing the Zambian people with domestic and industrial robots, artificial intelligence and as well as clean solar energy using the dual reflection solar system.')
                talk('Our vision Providing robotics and clean energy solutions using the most efficient technologies at the most affordable and reliable cost.')
 

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand you.")
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")

if __name__ == "__main__":
    main()
