#!/usr/bin/env python

# 24 Hour Light Cycle for Current Sattelite Plus using
# Raspberry Pi, Raspbian Stretch, LIRC, and Python
#
# Creator: FAD-DIYIT
# Date: 10/21/2018

# Loading in modules
import os
import time
import schedule

#
# Define Light Functions
#

# KEY_PROG4 is a programmable memory function set to 0% Red, 0% Green, 5% Blue, 0% White
def night_light():
	os.system("irsend SEND_ONCE SATELLITE_PLUS  KEY_PROG4")
	print("IR-SENT KEY_PROG4 - Blue Night-Light")

# KEY_PROG1 is a programmable memory function set to 50% Red, 30% Green, 0% Blue, 10% White
def pre_sunrise():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_PROG1")
	print("IR-SENT KEY_PROG1 - Pre-sunrise")

# KEY_F4 is the Sunrise/Sunset dynamic Fade feature
def dynamic_sunrise():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_F4")
	print("IR-SENT KEY_F4 - Sunrise Dynamic Fade")

# KEY_PROG2 is a programmable memory function set to 75% Red, 65% Green, 0% Blue, 20% White
def low_light_orange():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_PROG2")
	print("IR-SENT KEY_PROG2 - Orange Low Light")

# BTN_7 increases the White LEDs by ~5%, sent multiple times for a gradual 35% fade
def fade_up_white():
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_7")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_7")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_7")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_7")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_7")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_7")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_7")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_7")
	time.sleep(1)
	print("IR-SENT BTN_7 8x - Increase White")

# KEY_1 is a predefined color orange, 100% Red, 100% Green, %Blue, 100% White
def full_orange():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_1")
	print("IR-SENT KEY_1 - Full Color Orange")

# KEY_5 is a predefined full spectrum, 100% Red, 100% Green, 100% Blue, 100% White
def full_spectrum():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_5")
	print("IR-SENT KEY_5 - Full Spectrum")

# KEY_F3 is the Cloudy Moonlight dynamic fade feature
def cloudy_moon():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_F3")
	print("IR_SENT KEY_F3 - Cloudy Moon")

# KEY_2 is a predefined color Blue, 0% Red, 0% Green, 100% Blue, 100% White
def full_blue():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_2")
	print("IR-SENT KEY_2 - Full Color Blue")

# BTN_8 decreases the White LEDs by ~5%, sent multiple times for a gradual 35% fade
def fade_down_white():
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_8")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_8")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_8")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_8")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_8")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_8")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_8")
	time.sleep(1)
	os.system("irsend SEND_ONCE SATELLITE_PLUS BTN_8")
	time.sleep(1)
	print("IR-SENT BTN_8 8x - Deacrease White")

# KEY_F1 is the Bright Moonlight dynamic fade feature
def bright_moon():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_F1")
	print("IR-SENT KEY_F1 - Bright Moonlight")
	
# KEY_F2 is the Dim Moonlight dynamic fade feature
def dim_moon():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_F2")
	print("IR-SENT KEY_F2 - Dim Moonlight")

# KEY_F8 is the Afternoon Clouds dynamic fade feature
def afternoon_clouds():
	os.system("irsend SEND_ONCE SATELLITE_PLUS KEY_F8")
	print("IR-SENT KEY_F8 - Afternoon Clouds")

#
# Define start times for phases of the day, when lighting changes occur
#
phase0start = "23:00"  #Night Light
phase1start = "7:00"   #Pre-Sunrise
phase2start = "8:00"   #Sunrise
phase3start = "9:00"   #Early Morning
phase4start = "9:30"   #Increase Light 1
phase5start = "10:00"  #Increase Light 2
phase6start = "10:30"  #Late Morning
phase7start = "11:00"  #Noon
phase8start = "13:00"  #Afternoon Light Break
phase9start = "15:00" #Afternoon
phase10start = "17:00" #Late Afternoon
phase11start = "18:00" #Decrease Light 1
phase12start = "18:20" #Decrease Light 2
phase13start = "19:00" #Sunset
phase14start = "21:00" #Bright Moonlight
phase15start = "21:30" #Dim Moonlight

#
# Schedule light functions at phase start times
#
schedule.every().day.at(phase0start).do(night_light)
schedule.every().day.at(phase1start).do(pre_sunrise)
schedule.every().day.at(phase2start).do(dynamic_sunrise)
schedule.every().day.at(phase3start).do(low_light_orange)
schedule.every().day.at(phase4start).do(fade_up_white)
schedule.every().day.at(phase5start).do(fade_up_white)
schedule.every().day.at(phase6start).do(full_orange)
schedule.every().day.at(phase7start).do(full_spectrum)
schedule.every().day.at(phase8start).do(afternoon_clouds)
schedule.every().day.at(phase9start).do(full_spectrum)
schedule.every().day.at(phase10start).do(full_blue)
schedule.every().day.at(phase11start).do(fade_down_white)
schedule.every().day.at(phase12start).do(fade_down_white)
schedule.every().day.at(phase13start).do(dynamic_sunrise)
schedule.every().day.at(phase14start).do(bright_moon)
schedule.every().day.at(phase15start).do(dim_moon)

#
# loop checks schedule, then sleeps for 30 seconds
# run loop until shutdown or interrupt
#
while True:
	schedule.run_pending()
	time.sleep(30)
