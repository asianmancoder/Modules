import socket 


def get_dns(sitename):
  return socket.gethostbyaddr(socket.gethostbyname(sitename))[0]
