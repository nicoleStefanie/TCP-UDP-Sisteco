import socket                   

host = "localhost"
port = 50000

# Se crea TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enlazando con el puerto
server.bind((host, port))       
# Esperando la conexion con el cliente    
server.listen(5)                     
print 'Server running....'

while True:
    # Se establece la conexion con el cliente
    conn, addr = server.accept()
    with open('kk.txt', 'wb') as f:
        # Se abre el archivo recibido
        print 'File opened.'
        while True:
            # Se recibe contenido del archivo
            print "Receiving data from Client..."
            data = conn.recv(512)
            # Si hay mas datos que mostras
            if data:
                # Se muestran los datos
                print repr(data)
            # Si no hay mas datos que mostrar
            if not data:
                # Se acaba
                print "No more data."
                break
            # Se escribe el contenido recibido en un archivo
            f.write(data)
        break

# Archivo ya fue recibido 
print "Successfully get the file."
# Se cierra la conexion
conn.close()
print('Connection closed.')
# Cerrando socket
server.close()


