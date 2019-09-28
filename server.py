# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:03:27 2019

@author: cbshnrh
"""
from socket import *


def deal_with_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        fh = open(filename[1:])
        output_data = fh.read()
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent_Length: %d\n\n' % (len(output_data))
        connectionSocket.send(header.encode())
        for i in range(len(output_data)):
            connectionSocket.send(output_data[i].encode())
        print("Succeeded!")
        connectionSocket.close()
    except IOError:
        print("Failed!")
        header = 'HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())
        connectionSocket.close()

 
def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 19999))
    serverSocket.listen(1)
    try:
        while true:
            connectionSocket, addr = serverSocket.accept()
            print("客户端：", addr, "已连接。")
            deal_with_client(connectionSocket, addr)      
    finally:      
        serverSocket.close()

   
if __name__ == '__main__':
    main()  
