import snowboydecoder
import sys
import signal
#import this to call bash commands within python:
import os

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

#don't need this warning when calling pmdl programmatically:
#if len(sys.argv) == 1:
#    print("Error: need to specify model name")
#    print("Usage: python demo.py your.model")
#    sys.exit(-1)

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

#original line from kitt.ai/snowboy:
#model = sys.argv[1]
#Add custom voice models here:
models = ['/home/pi/snowboy/resources/saved_model.pmdl']

#original line from kitt.ai/snowboy:
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
#use this so you don't need to specify voice model when calling this script
detector = snowboydecoder.HotwordDetector(models, sensitivity=0.5)

#put what should happen when snowboy detects hotword here:
callbacks = [lambda: os.system("/home/pi/thingeriocurl.sh")]
#without "lambda", callback will run immediately on startup, 
#and then after each hotword detection:
#callbacks = [os.system("/home/pi/test.sh")]

print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
