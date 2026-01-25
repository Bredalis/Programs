
# Enviar mensajes automáticos

import pywhatkit
from datetime import datatime
import time

segundos = time.time() + 60
date = datatime.fromtimestamp(segundos)

def enviar_mensaje(telefono, texto):
	pywhatkit.sendwhatmsg(
		telefono,
		texto,
		date.hour,
		date.minute
	)

	time.sleep(5)