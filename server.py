import socket
from random import randrange

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(('127.0.0.2', 2897))
server_count = 0
total_pl = 0

# receive player's answer for mode selection
mode, addressInfo = serverSock.recvfrom(100)

while True:

   print('Ready to receive')

   # if player chooses auto, automatically calculate and send seq, ack and pl numbers
   if mode.decode('utf-8') == 'auto':

       # code to receive data
       data, addressInfo = serverSock.recvfrom(100)
       server_count += 1
       print(data.decode('utf-8') + ' from ' + str(addressInfo))
       print(' Ready to send' + ' server score: ' + str(server_count))

       # split received data
       msg, seq, ack, pl = data.split()

       # calculate new seq, ack numbers
       # received ack number is now server side's seq number
       new_seq = str(int(ack))

       # add total pl, add 1 to it and make it the new ack number  (expected value from client side)
       old_seq = str(int(seq))
       old_ack = str(int(ack))
       old_pl = str(int(pl))


       total_pl = int(pl)
       seq = int(seq)
       new_ack = str(total_pl + seq)

       # packet length is random, between 0 and 100
       new_pl = str(randrange(100))



       # code to send calculated data
       #serverSock.sendto(bytes(new_seq + ' ' + new_ack + ' ' + new_pl, 'utf-8'), ('127.0.0.2', 3997))
       #################################################
       ack = str((int(old_seq)+int(old_pl)))
       if new_seq != old_ack or new_ack != ack:
           print("False")
           Negative_response = "Corrupted packet or duplicate packet"
           serverSock.sendto(bytes(Negative_response + ' ' + new_seq + ' ' + new_ack + ' ' + new_pl, 'utf-8'),
                             ('127.0.0.2', 3997))
       else:

           print("Correct")
           serverSock.sendto(bytes( new_seq + ' ' + new_ack + ' ' + new_pl, 'utf-8'), ('127.0.0.2', 3997))



   # if player chooses manual, let player 2 (server) calculate and type their own reply
   elif mode.decode('utf-8') == 'manual':
       # receive data
       data, addressInfo = serverSock.recvfrom(100)

       print(data.decode('utf-8') + ' from ' + str(addressInfo))
       print(' Ready to send' + ' server score: ' + str(server_count))

       i = 0


       list = []

       while i>=0 and i<10:
           print('Enter your reply')
           reply = input()
           print('Enter your calculated seq, ack, packet length numbers: ')
           seq1, ack1, pl1 = input().split()
           # split received data
           msg2, seq2, ack2, pl2 = data.split()
           # print(seq)
           # print(ack)
           # print(pl)
           # print('*')

           packet = seq1 + " " + ack1 + " " + pl1
           list.append(packet)


           if (seq1 == str(int(ack2))) and (str((int(pl2) + int(seq2))) == ack1):
               print('Ready to send data')

               serverSock.sendto(bytes(reply + ' ' + seq1 + ' ' + ack1 + ' ' + pl1, 'utf-8'),  # data to be sent

                                 ('127.0.0.2', 3997)  # details of destination

                                 )

               # code to receive data

               server_count += 1

               print('Ready to receive' + ' server score = ' + str(server_count))

               # data => received

               data, addressInfo = serverSock.recvfrom(100)

               print(data.decode('utf-8') + ' from ' + str(addressInfo))

               i += 1



           elif len(list)>1 and list[-1] == list[-2]:
               server_count -= 1
               i += 1
               print("server score = " + str(server_count))
               print("This is a duplicate packet!")

           else:

               server_count -= 1

               i += 1

               print("server score = " + str(server_count))

               msg1 = '!!Corrupted packet!! try again, please more careful!!'

               print(msg1)
