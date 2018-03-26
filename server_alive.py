import socket

servers = [{
   "address":"www.google.com",
   "port":80
   },{
   "address":"www.facebook.com",
   "port":80
   }
]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for server in servers:
   result = sock.connect_ex((server['address'], server['port']))
   if result == 0:
      print(server['address']+": Port is open")
   else:
      print(server['address']+":Port is not open")