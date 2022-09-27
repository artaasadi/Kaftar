import socket
from sys import argv
import threading
import time

PORT = 1373 # Port to listen on
MESSAGE_LENGTH_SIZE = 64 # Need MESSAGE_LENGTH_SIZE to get message length to know how much to recieve
ENCODING = 'ascii' # Ascii encoding for messages
SERVER = "82.115.20.200"
subscribers = {} # A global dictionary is needed

def send_msg(server : socket.socket, message) :
    msg = message.encode(ENCODING)
    msg_length = str(len(msg)).encode(ENCODING)
    msg_length += b' ' * (MESSAGE_LENGTH_SIZE - len(msg_length))

    server.send(msg_length)
    server.send(msg)


def add_subscriber(conn : socket.socket, topics) :
    for topic in topics :
        if topic in subscribers.keys() :
            if conn not in subscribers[topic]:
                subscribers[topic].append(conn)
        else :
            subscribers[topic] = [conn]
    msg = "subscribing on :"
    for topic in subscribers.keys() :
        if conn in subscribers[topic] :
            msg += " " + topic
    send_msg(conn, msg)


def publish_msg(topic, msg) :
    message = "[MESSAGE] [{}]".format(topic)
    for m in msg :
        message += " " + m
    for t in subscribers.keys() :
        if t == topic :
            for conn in subscribers[t] :
                send_msg(conn, message)
            break

def client_listener(conn : socket.socket, address, close_connection, ping_answer) :
    while True :
        try :
            received = conn.recv(MESSAGE_LENGTH_SIZE).decode(ENCODING)
            msg_length = int(received)
            msg = conn.recv(msg_length).decode(ENCODING)
        except :
            print("connection {} interrupted".format(address))
            break
        print("[MESSAGE RECEIVED] [{}] {}".format(address, msg))
        msg = msg.split()
        if msg[0] == "subscribe" :
            try :
                add_subscriber(conn, msg[1:])
                send_msg(conn, "you subscribed successfully".format(msg[1:]))
            except :
                send_msg(conn, "subscribing failed")
        elif msg[0] == "publish" :
            try :
                publish_msg(msg[1], msg[2:])
                send_msg(conn, "your message published successfully")
            except :
                send_msg(conn, "your message publishing failed")
        elif msg[0] == "Pong" :
            del ping_answer[:]
        elif msg[0] == "quit" :
            close_connection.append(1)
            break


def connection_handler(conn : socket.socket, address):
    with conn:
        print("[NEW CONNECTION] {}".format(address))
        last_ping = time.time()
        close_connection = []
        pings = []
        t = threading.Thread(target=client_listener, args=(conn, address, close_connection, pings))
        t.start()
        while True :
            if (time.time() - last_ping) >= 10.0 :
                if len(pings) != 0 :
                    print("[PING NOT ANSWERED] {} time(s): {}".format(len(pings), address))
                if len(pings) == 3 :
                    break
                last_ping = time.time()
                send_msg(conn, "Ping")
                pings.append(1)
            if len(close_connection) > 0 : 
                break
        for subscriber in subscribers.keys() :
            if conn in subscribers[subscriber] :
                subscribers[subscriber].remove(conn)
        send_msg(conn, "closed")
            
    print("[CONNECTION CLOSED] {}".format(address))

def start_server(server : socket.socket, info) :
    print("[SERVER ON] {}".format(info))
    server.listen()
    while True :
        conn, address = server.accept()
        threading.Thread(target= connection_handler, args= (conn, address)).start()


def main() :
    address = SERVER #socket.gethostname() #socket.gethostbyname(socket.gethostname()) # Get Address automatically
    HOST_INFORMATION = (address, PORT)
    # Initialize server socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server :
        server.bind(HOST_INFORMATION)
        start_server(server, HOST_INFORMATION)


if __name__ == '__main__' :
    main()