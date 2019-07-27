import socket
import time
import os

host = "localhost"  
port = 50000

# Se crea TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se conecta el socket con el puerto al cual esta el servidor
client.connect((host, port))
# Se crea el archivo con caracteres random
filename = os.system("dd if=/dev/urandom of=/home/nicole/Escritorio/ClientTCP/kk.txt bs=512 count=64")
# Se abre el archivo para enviar
fileToSend = open("kk.txt",'rb')
# Se lee el archivo
l = fileToSend.read(512)

# Empieza a contar el tiempo de envio
start_time = time.time()

while (l):
	client.send(l)
	print "Sent %d bytes." % len(l)
	# Se muestra lo que se va enviando
	print repr(l)
	l = fileToSend.read(512)

# Ya termino
print "Done sending."
# Se muestran los segundos que se demoro en enviar el archivo
print "The file was sent in %s seconds." % (time.time()-start_time)
# Se cierra el archivo
fileToSend.close()
# Cerrando socket 
client.close()

#The file was sent in 0.0589370727539 secondss




