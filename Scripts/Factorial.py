
def factorial(numero):

	if numero == 0:
		return 1

	else:
		return numero * factorial(numero - 1)
		
for i in range(5):
	print(factorial(i))