#################################
# Info on WeeVocavulary package #
# Author: Gaétan Lepage         #
# Creation Date: 2024-09-02     #
#################################
"""Metadata"""
__author__ = "Gaétan Lepage"
__version__ = "0.1.0"    # primary changes (not functional)
__modif__ = "2024-09-02"

"""Requirements"""
# Built-in packages
import os, sys, time, logging
# External packages
import pandas                         # Data manipulation (csv)
import genanki, tkinter, ttkbootstrap # Anki/GUI
import translate, gtts, lingua        # TRANSLATION/VOICE GENERATION/LANGUAGE DETECTION
# Internal packages
import utility

"""Hard files requirements"""
# Logging configuration
log_config_path = 'log_config.py'
os.path.isfile(log_config_path)
# Directories for data storage
data_path = 'data/'
os.path.isdir(data_path)
# File for settings 
settings_path = 'settings_weevoc.py'
