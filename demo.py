import keyboard
boolean = False

d = None
q = None

def my_custom_a_function():

	global boolean
	if( boolean ):
		boolean = not boolean
		print("TAB is not active")
		keyboard.remove_hotkey(d)
		keyboard.remove_hotkey(q)

def my_custom_tab_function():

	global boolean
	global d
	global q
	boolean = not boolean
	if( boolean ):
		print("TAB is active")
		d = keyboard.add_hotkey( "d", lambda: keyboard.press_and_release("right"), suppress=True )
		q = keyboard.add_hotkey( "q", lambda: keyboard.press_and_release("left"), suppress=True )
	else:
		print("TAB is not active")
		keyboard.remove_hotkey(d)
		keyboard.remove_hotkey(q)
		# keyboard.unhook_all_hotkeys()
		# init()

	keyboard.press_and_release("esc")

def my_custom_escape_function():
	# print("my_custom_escape_function")
	my_custom_tab_function()

def my_custom_CTRL_function():
	# print("my_custom_CTRL_function")
	my_custom_tab_function()

def on_key_event(event):
	if( event.name != "tab" ):
		print(f"Key pressed: {event.name}")
	# if keyboard.is_pressed("ctrl") and event.name == "c":
	#	exit()

def swap_keys():

	init()
	keyboard.on_press(on_key_event)
	keyboard.wait()

def init():

	tab = keyboard.add_hotkey( "tab" , lambda: my_custom_tab_function() , suppress=True )
	a   = keyboard.add_hotkey( "a"   , lambda: my_custom_a_function() )

	keyboard.add_hotkey( "ctrl" , lambda: my_custom_CTRL_function() )
	keyboard.add_hotkey( "esc"  , lambda: my_custom_escape_function() )

try:
	swap_keys()
except:
	print( f"exit")
