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
4) Create ~/.asoundrc with correct hw settings. use aplay -l & arecord -l to find out hw cards.
in this sample, playback is through onboard jack & input is through usb mic

pcm.!default {
  type asym
   playback.pcm {
     type plug
     slave.pcm "hw:0,0"
   }
   capture.pcm {
     type plug
     slave.pcm "hw:1,0"
   }
}
5) If using RESTful API Calls  via python script (per snowboy instructions) need to install "requests" module for python:
pip install requests
6) Download pre-packaged Snowboy binaries and their Python wrappers for Raspberry Pis:
https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/rpi-arm-raspbian-8.0-1.1.1.tar.bz2
7) extract to Pi & rename directory to "snowboy"
