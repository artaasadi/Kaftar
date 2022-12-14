from fileinput import filename
import bake_croissant
import eat_croissant
import paramiko
import os
folder_name = ''
hostname = "XX.XX.XX.XX"
username = "USER"
password = "PASS"
if __name__ == "__main__" :
    print("==============================")
    print("          TYPE 'help'         ")
    print("==============================")
    while True:
        action = input("WHAT TO DO : ").split()
        if action[0] == "bake":
            if len(action) == 2 :
                bake_croissant.bake(action[1])
            else :
                print("you need to add topic for your message")
        elif action[0] == "eat":
            if len(action) == 2 :
                eat_croissant.eat(action[1])
            else :
                print("you need to add topic for the message you're going to read")
        elif action[0] == "list":
            # initialize the SSH client
            client = paramiko.SSHClient()
            # add to known hosts
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(hostname=hostname, username=username, password=password)
            except:
                print("[!] Cannot connect to the SSH Server")
                exit()
            sftp_client = client.open_sftp()
            filesList = sftp_client.listdir("/root/msgBroker/messages/"+folder_name)
            readedFiles = os.listdir("./received_croissants")
            for fileName in filesList :
                if not(fileName in readedFiles):
                    print("[UNREAD] ", fileName)
                else:
                    print("[READ] ", fileName)
        elif action[0] == "help":
            print("==============================")
            print("          THE ACTIONS         ")
            print("==============================")
            print("    |   To [write] a new message, type 'bake' and then the topic. Like 'bake sth'.")
            print("    |   To [read] a message, type 'eat' and then the topic. Like 'eat sth'. (without '.txt')")
            print("    |   To see the [list] of messages, type 'list'.")
            print("    |   To [exit], type exit.")
        elif action[0] == "exit":
            exit()
