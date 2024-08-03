
def fibonacci(numero):

	if numero == 0 or numero == 1:
		return numero

	else:
		return fibonacci(numero - 1) + fibonacci(numero - 2)

for i in range(10):
	print(fibonacci(i))