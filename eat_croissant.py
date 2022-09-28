import random
import random
import paramiko
import os
import sys
folder_name = 'lighten-rx'
def eat(fileName) :
    hostname = "82.115.20.200"
    username = "root"
    password = "1QAZ2wsx"

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
    destLoc = "./received_croissants/"
    allData = ["/root/msgBroker/messages/"+folder_name+"/"+fileName+".txt"]
    for filetosend in allData:
        try:
            filename = os.path.basename(filetosend)
            destFile = os.path.join(destLoc,filename) #renaming the file
            print("receive : ", destFile)
            sftp_client.get(filetosend, destFile) #send datafile filetosend to destFile
            with open('RFidgetRunLogs.txt','a') as file:
                file.write(f"{filetosend}, {destFile}\n") #add the run logs
        except:
            print("File not found or something.")


    sftp_client.close()

    NAME = "User"

    f = open("recipe.txt", "r")
    recipe = list(f.read())

    f = open("./received_croissants/"+fileName+".txt", "r")
    pack = f.read().split(".")

    print("\n {} :".format(NAME))

    for croissant in pack:
        if (croissant == ""):
            print(" {}|  ".format( "".join([" " for i in range(len(NAME)+1)]) ) )
        else:
            yamyam = []
            for roll in croissant.split(":"):
                bite = ""
                for crust in roll.split(","):
                    bite = bite + str(len(crust))
                yamyam.append(recipe[int(bite)])

            print(" {}|  ".format( "".join([" " for i in range(len(NAME)+1)]) ) + "".join(yamyam))


