import socket

host = 'localhost'
port = 10000

# Se crea UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Se enlaza el socket con el puerto (no es necesario conexion con el server)
server_address = (host, port)
# Corriendo servidor
sock.bind(server_address)
print "Server running..."

while True:
    # Se recibe archivo desde el cliente
    data, address = sock.recvfrom(512)
    # Se abre el archivo recibido
    f = open("kk.txt",'wb')
    # Se muestra lo recibido (contenido del archivo)
    print repr(data)
    # Se muestra los bytes de lo recibido
    print "Received %d bytes from Client." % len(data) 
    break

# Archivo ya fue recibido 
print "Successfully get the file."
# Se cierra el socket
sock.close()


