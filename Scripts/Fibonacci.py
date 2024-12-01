
def fibonacci(numero):
<<<<<<< HEAD
	return numero if numero == 0 or numero == 1 else fibonacci(numero - 1) + fibonacci(numero - 2)
=======

	if numero == 0 or numero == 1:
		return numero

	else:
		return fibonacci(numero - 1) + fibonacci(numero - 2)
>>>>>>> 0ef5f1e9e18af325cc084fe05193bb4d49bdf2da
