import os
import sys
import pygame
from PIL import Image
import cv2
import moviepy
from pydub import AudioSegment
import tkinter

def check_installation():
    # Suppress ALSA and Pygame messages temporarily
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')
    pygame.init()
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    # Check Pygame version
    print(f"✅ Pygame version: {pygame.version.ver}")

    # Check Pillow version
    print(f"✅ Pillow version: {Image.__version__}")

    # Check OpenCV version
    print(f"✅ OpenCV version: {cv2.__version__}")

    # Check MoviePy version using an alternative method
    print(f"✅ MoviePy version: {moviepy.__version__}")

    # Check Pydub version
    print(f"✅ Pydub version: {'ffmpeg' if AudioSegment.ffmpeg else 'no ffmpeg'}")

    # Check Tkinter
    try:
        _ = tkinter.Tcl()  # Only initialize, don't open a window
        print("✅ Tkinter is installed and working!")
    except Exception as e:
        print(f"❌ Terjadi kesalahan saat memeriksa Tkinter: {str(e)}")

check_installation()
