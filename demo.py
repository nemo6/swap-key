import keyboard
import math
import time
import threading
boolean = False
mouse_block = None
count = 0
count_thread = 0

# Return the truncated integer parts of different numbers
import win32api

def periodic_function():
	global count
	global mouse_block
	global count_thread
	count_thread += 1

	while mouse_block:
		print(count)
		count+=1
		win32api.SetCursorPos( (50, 50) )
		time.sleep(0.1)

	print("while exit")
	count_thread -= 1

# Start thread

# win32api.SetCursorPos((math.trunc(1920/2), math.trunc(1080/2)))

z = None
s = None
d = None
q = None

somestring = ["tab","ctrl","c","esc"]

def my_custom_a_function():
	print("my_custom_a_function")
	global boolean
	boolean = False
	my_custom_tab_function()

def my_custom_tab_function():

	global boolean
	global z
	global s
	global d
	global q
	global mouse_block
	global count
	global count_thread
	boolean = not boolean
	if( boolean ):

		print("TAB is active")

		# periodic_function()
		if( count_thread == 0 ):
			mouse_block=True
			thread = threading.Thread( target=periodic_function )
			thread.start()
		else:
			print("thread already running")

		z = keyboard.add_hotkey( "z", lambda: keyboard.press_and_release("up"), suppress=True )
		s = keyboard.add_hotkey( "s", lambda: keyboard.press_and_release("down"), suppress=True )
		d = keyboard.add_hotkey( "d", lambda: keyboard.press_and_release("right"), suppress=True )
		q = keyboard.add_hotkey( "q", lambda: keyboard.press_and_release("left"), suppress=True )

	else:

		print("TAB is not active")

		mouse_block=False
		count=0

		keyboard.unhook_all_hotkeys()
		init()

	keyboard.press_and_release("esc")

def my_custom_escape_function():
	# print("my_custom_escape_function")
	my_custom_tab_function()

def my_custom_ctrl_function():
	global boolean
	boolean = True
	my_custom_tab_function()

def on_key_event(event):

	if event.name not in somestring: 
		print(f"Key pressed: {event.name}")
	# if keyboard.is_pressed("ctrl") and event.name == "c":
	# 	exit()

def swap_keys():

	init()
	keyboard.on_press(on_key_event)
	keyboard.wait()

def init():

	tab = keyboard.add_hotkey( "tab" , lambda: my_custom_tab_function() , suppress=True )
	keyboard.add_hotkey( "esc" , lambda: my_custom_escape_function() )
	# keyboard.add_hotkey( "a", lambda: my_custom_a_function() )
	keyboard.add_hotkey( "ctrl" , lambda: my_custom_ctrl_function() )

try:
	swap_keys()
except:
	print( f"exit")
