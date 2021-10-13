import speech_recognition as sr
import queue, threading
import sounddevice as sd
import soundfile as sf
import os, time

def set():
    global q
    global recorder
    global recording
    global audio_path
    q= queue.Queue()
    recorder = False
    recording = False
    audio_path=r"C:\pythonworkspace\python macro\pythom_macro\record_file\temp.wav"

def complicated_record():
    with sf.SoundFile(audio_path, mode='w', samplerate=16000, subtype='PCM_16', channels=1) as file:
        with sd.InputStream(samplerate=16000, dtype='int16', channels=1, callback=complicated_save):
            while recording:
                file.write(q.get())

def complicated_save(indata, frames, time, status):
    q.put(indata.copy())

def start():
    global recorder
    global recording
    recording = True
    recorder = threading.Thread(target=complicated_record)
    print('start recording')
    recorder.start()

def stop():
    global recorder
    global recording
    recording = False
    recorder.join()
    print('stop recording')

def recognize_text(audio_path):
    r = sr.Recognizer()
    harvard = sr.AudioFile(audio_path)
    with harvard as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language='ko-KR')
    except:
        text="none"

    print(text)
    return text

def command(text):
    if "어쩌구1" in text:
        print("어쩌구1")
        if "명단" in text:
            path = os.path.realpath(r'C:\python_project\어쩌구2\명단.xlsx')
        else:
            path = os.path.realpath(r'C:\python_project\어쩌구2\명단.xlsx')
    elif "어쩌구2" in text:
        print("어쩌구2")
        if "명단" in text:
            path = os.path.realpath(r'C:\python_project\어쩌구2\명단.xlsx')
        else:
            path = os.path.realpath(r'C:\python_project\어쩌구2')
    elif "어쩌구3" in text:
        print("어쩌구3")
        if "명단" in text:
            path = os.path.realpath(r'C:\python_project\어쩌구3\명단.xlsx')
        else:
            path = os.path.realpath(r'C:\python_project\어쩌구3')
    else:
        path = os.path.realpath(r'C:\\')
    os.startfile(path)

# set()
# start()
# time.sleep(3)
# stop()
# command(recognize_text(audio_path))