# snowboyPI
snowboy setup on raspberry pi
Start with a fresh install of Raspbian (Lite or Regular, this guide assumes Lite)
1) Update
sudo apt update && sudo apt -y upgrade && sudo apt-get -y auto-remove && sudo reboot
2) Install dependencies:
sudo apt -y install python-pyaudio python3-pyaudio sox python3-pip python-pip libatlas-base-dev
3) Install PortAudio’s Python bindings:
python2:
sudo pip install pyaudio
python3:
sudo pip3 install pyaudio
4) Create ~/.asoundrc with correct hw settings. use aplay -l & arecord -l to find out hw cards. "card 0, device 0" is "hw:0,0"
In the attached sample, playback is through onboard jack & input is through usb mic
5) If using RESTful API Calls  via python script (per snowboy instructions) need to install "requests" module for python:
pip install requests
6) Download pre-packaged Snowboy binaries and their Python wrappers for Raspberry Pis:
https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/rpi-arm-raspbian-8.0-1.1.1.tar.bz2
7) Extract to Pi & rename directory to "snowboy"

Prepare Snowboy
1) copy training_service.py to the snowboy directory
2) log into https://snowboy.kitt.ai, click on “Profile settings”, and copy your API token
3) change the appropriate fields (token, hotword, etc.) in training_service.py
4) use "rec -r 16000 -c 1 -b 16 -e signed-integer FILENAME.wav" to record 3 wav files of your hotword to the same directory
5) run the following to generate a pmdl
python training_service.py 1.wav 2.wav 3.wav saved_model.pmdl
6) move saved_model.pmdl to ~/snowboy/resources/ (rename for easier recall later)
7) run the demo to make sure everything is working:
python demo.py ~/snowboy/resources/saved_model.pmdl

Customize Snowboy
1) copy snowboy.py to the snowboy directory
2) copy thinger.io curl request to ~/thingeriocurl.sh
