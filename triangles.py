import math
def hypotTri (a, b):
	hypot = math.sqrt(a**2 + b**2)
	print "The hypotenuse of your right triangle with side a\={0} and side b\={1} is {2}.".format (a, b, hypot)

def areaTri (b, h):
	area = (b*h)/2
	print "The area of your triangle a base of {0} and a height of {1} is {2}.".format (b, h, area)

def choice ():
	calculation = int (raw_input("Select a calculation: \n1. Calulate hypotenuse \n2. Calulate area of triangle"))

	if calculation == 1:
		a = raw_input ("Enter the length of side a of your triangle: \n")
		b = raw_input ("Enter the length of side b of your triangle: \n")
		try:
			hypotTri (float (a), float (b))
		except ValueError:
			print "Sorry, we only accept numbers."
			return choice()		
	elif calculation == 2:
		a = raw_input ("Enter the length of the base of your triangle: \n")
		b = raw_input ("Enter the height of your triangle \n")
		try:
			areaTri (float (a), float (b))
		except ValueError:
			print "Sorry, we only accept numbers."
			return choice()

	else:
		print "Please select a valid calculation."
		choice ()


if __name__ == '__main__':
	choice()
