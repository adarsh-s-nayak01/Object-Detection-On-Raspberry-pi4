import os
import speech_recognition as sr 
import os
import time
import telepot
import cv2

r = sr.Recognizer()

def Capture():
    vs = cv2.VideoCapture(0)
    i = 0
    while True:
        ret, frame = vs.read()
        if not ret:
            break
        i += 1
        if i > 25:
            cv2.imwrite('frame.png', frame)
            break
        cv2.imshow('stream',  frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('frame.png', frame)
            break
    vs.release()
    cv2.destroyAllWindows()
    
def Send():
    bot = telepot.Bot('5505770046:AAHZ00lFDyhh9AL_r7XFrzKaqDT2LWp52V4')
    bot.sendMessage("1388858613", str("emergency http://maps.google.com/?q=77.434,12.35434"))
    bot.sendPhoto("1388858613", photo=open('frame.png', 'rb'))
    
print('say something')
while True :

    if(os.path.isfile('out1.wav')):
        os.system('arecord --format=S16_LE --rate=16000 --file-type=wav out1.wav -d 3')
        print('done')
        harvard = sr.AudioFile('out1.wav')
        with harvard as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio) 
            print ("you said: " + text )
            os.remove('out1.wav')
            if text == 'emergency':
                Capture()
                Send()
        except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio")
                print('Say again ')

        except sr.RequestError as e: 
                print("Could not request results from Googlespeech Recognition service; {0}".format(e))
                print('Say again ')
    else:
        print('say again')
        os.system('arecord --format=S16_LE --rate=16000 --file-type=wav out1.wav -d 3')
