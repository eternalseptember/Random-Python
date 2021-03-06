import turtle
import time

def show_poly():
	try:
		win = turtle.Screen()	# Grab/create a resource, e.g. a window
		squirtle = turtle.Turtle()

		# This dialog could be cancelled,
		#   or the conversation to int might fail, or n might be zero.
		n = int(input("How many sides do you want in your polygon?"))
		angle = 360 / n
		for i in range(n):	# Draw the polygon
			squirtle.forward(10)
			squirtle.left(angle)
		time.sleep(3)		# Make program wait a few seconds
	finally:
		win.bye()			# Close the turtle's window


show_poly()
show_poly()
show_poly()