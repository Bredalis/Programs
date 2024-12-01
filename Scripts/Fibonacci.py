
def fibonacci(numero):
	return numero if numero == 0 or numero == 1 else fibonacci(numero - 1) + fibonacci(numero - 2)