
import socket
from numpy import random

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.bind(('127.0.0.2', 3997))


def send_msg():
    print('Do you want to play in auto mode or manual mode?')
    mode_selection = input()

    if mode_selection == 'auto':
        # score count declaration
        client_count = 0

        i = 0

        clientSock.sendto(bytes(mode_selection, 'utf-8'), ('127.0.0.2', 2897))

        list = []

        while i == 0:

            print('Enter your message')
            msg = input()
            print('Enter your sequence, acknowledgement and packet length values:')
            seq, ack, pl = input().split()
            print('Ready to send data')

            clientSock.sendto(bytes(msg + ' ' + seq + ' ' + ack + ' ' + pl, 'utf-8'),  # data to be sent
                              ('127.0.0.2', 2897)  # details of destination
                              )

            # code to receive data
            client_count += 1


            print('Ready to receive' + ' client score = ' + str(client_count))

            # data => received
            data, addressInfo = clientSock.recvfrom(100)
            print(data.decode('utf-8') + ' from ' + str(addressInfo))
            i += 1

            packet = seq + " " + ack + " " + pl
            list.append(packet)


        while i>=1 and i< 10:

            print('Enter your message')
            msg = input()
            print('Enter your sequence, acknowledgement and packet length values:')
            seq, ack, pl = input().split()


            seqS, ackS, plS = data.split()


            packet = seq + " " + ack + " " + pl
            list.append(packet)


            if (seq == str(int(ackS))) and (str((int(plS)+int(seqS))) == ack):
                print('Ready to send data')

                clientSock.sendto(bytes(msg + ' ' + seq + ' ' + ack + ' ' + pl, 'utf-8'),  # data to be sent
                                  ('127.0.0.2', 2897)  # details of destination
                                  )

                # code to receive data
                client_count += 1

                print('Ready to receive' + ' client score = ' + str(client_count))

                # data => received
                data, addressInfo = clientSock.recvfrom(100)
                print(data.decode('utf-8') + ' from ' + str(addressInfo))
                i += 1

            elif list[-1] == list[-2]:
                client_count -= 1
                i += 1
                print("client score = " + str(client_count))
                print("This is a duplicate packet!")

            else:
                client_count -= 1
                i += 1
                print("client score = " + str(client_count))
                msg1 = '!!Corrupted packet!! try again, please more careful!!'
                print(msg1)
        #print("server score:   "+UDPServer.server_count)





    if mode_selection == 'manual':

        # score count declaration

        client_count = 0

        i = 0

        clientSock.sendto(bytes(mode_selection, 'utf-8'), ('127.0.0.2', 2897))

        list = []

        while i == 0:
            print('Enter your message')

            msg = input()

            print('Enter your sequence, acknowledgement and packet length values:')

            seq, ack, pl = input().split()

            print('Ready to send data')

            clientSock.sendto(bytes(msg + ' ' + seq + ' ' + ack + ' ' + pl, 'utf-8'),  # data to be sent

                              ('127.0.0.2', 2897)  # details of destination

                              )

            # code to receive data

            client_count += 1

            print('Ready to receive' + ' client score = ' + str(client_count))

            # data => received

            data, addressInfo = clientSock.recvfrom(100)

            print(data.decode('utf-8') + ' from ' + str(addressInfo))

            i += 1

            packet = seq + " " + ack + " " + pl
            list.append(packet)

        while i >= 1 and i < 10:

            print('Enter your message')

            msg = input()

            print('Enter your sequence, acknowledgement and packet length values:')

            seq, ack, pl = input().split()

            reply, seqS, ackS, plS = data.split()

            packet = seq + " " + ack + " " + pl
            list.append(packet)

            if (seq == str(int(ackS))) and (str((int(plS) + int(seqS))) == ack):

                print('Ready to send data')

                clientSock.sendto(bytes(msg + ' ' + seq + ' ' + ack + ' ' + pl, 'utf-8'),  # data to be sent

                                  ('127.0.0.2', 2897)  # details of destination

                                  )

                # code to receive data

                client_count += 1

                print('Ready to receive' + ' client score = ' + str(client_count))

                # data => received

                data, addressInfo = clientSock.recvfrom(100)

                print(data.decode('utf-8') + ' from ' + str(addressInfo))

                i += 1

            elif list[-1] == list[-2]:
                client_count -= 1
                i += 1
                print("client score = " + str(client_count))
                print("This is a duplicate packet!")

            else:

                client_count -= 1

                i += 1

                print("client score = " + str(client_count))

                msg1 = '!!Corrupted packet!! try again, please more careful!!'

                print(msg1)
        #print("server score:   "+UDPServer.server_count)
    else:
        print('Invalid answer. Try again')


send_msg()
