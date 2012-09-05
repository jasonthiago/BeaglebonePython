#Python GPIO test script for the Beaglebone
#developed by Bryan - August, 2012

#General Python Imports, like system, time, etc.
import time

#Beaglebone bone.py API
from bone import *

led_on(USR2)
time.sleep(1)
led_off(USR2)

print "Script done."
