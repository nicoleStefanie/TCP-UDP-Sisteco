import socket	
import time
import os

host = 'localhost'
port = 10000

# Se crea UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Se enlaza el socket con el puerto (no es necesario conexion con el servidor)
server_address = (host, port)
# Se crea el archivo con caracteres random
filename = os.system("dd if=/dev/urandom of=/home/nicole/Escritorio/ClientUDP/kk.txt bs=512 count=64")
# Se abre el archivo para enviar
fileToSend = open("kk.txt", 'rb') 
# Se lee el archivo
l = fileToSend.read(512)

try:
	# Empieza a contar el tiempo de envio
	start_time = time.time()
	print "Sending File"
	sent = sock.sendto(l,server_address)
	# Se muestra el contenido del archivo
	print repr(l)
	# Archivo enviado
	print "File sent."
	# Se cierra el archivo enviado
	fileToSend.close()
	# Se muestran los segundos que se demoro en enviar el archivo
	print "The file was sent in %s seconds" %(time.time()-start_time)

finally:
    print "Closing socket"
    # Se cierra el socket
    sock.close()

#The file was sent in 0.000808954238892 seconds