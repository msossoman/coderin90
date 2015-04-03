def factorial(n):
	while n > 0:
		return n * factorial(n-1)
	return 1

print factorial(4)

'''def user():
	n = (raw_input("What number would you like to use?"))
	try:
		factorial(int(n))
	except ValueError:
		print "You must choose a number. Please try again."
		return user()


if __name__ == '__main__':
	user()'''
