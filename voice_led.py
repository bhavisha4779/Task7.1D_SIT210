import RPi.GPIO as GPIO
import speech_recognition as sr
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 11
GPIO.setup(LED_PIN, GPIO.OUT)

r = sr.Recognizer()
mic = sr.Microphone(device_index=2)

print("Say 'TURN ON' to switch LED ON, 'TURN OFF' to switch LED OFF.")
print("Press Ctrl+C to stop.")

try:
    while True:
        with mic as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=4)

        try:
            command = r.recognize_google(audio)
            command = command.lower().strip()
            print("You said:", command)

            if "turn on" in command:
                GPIO.output(LED_PIN, GPIO.HIGH)
                print("[MATCHED: TURN ON] → LED turned ON")
            elif "turn off" in command:
                GPIO.output(LED_PIN, GPIO.LOW)
                print("[MATCHED: TURN OFF] → LED turned OFF")
            else:
                print("[NO MATCH] Command not recognized.")

        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results;", e)

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program...")
finally:
    GPIO.cleanup()
