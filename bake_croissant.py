import random
import paramiko
import os
import sys
folder_name = ''

def bake(fileName) :

    NAME = "User"

    print("==============================")
    print(" TO BAKE CROISSANT ENTER: ::: ")
    print("==============================")
    

    f = open("recipe.txt", "r")
    recipe = list(f.read())    
    paste = []
    chocolate = []

    materials = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/><\'\";]}[{|\\+=_-)(*&^%$#@!`~"
    
    print("\n {} :".format(NAME))


    while(True):
        chocol = input( " {}|  ".format("".join([" " for i in range(len(NAME)+1)])) )
        if(chocol == ':::'):
            break
        chocolate.append(list(chocol))


    # f = open("new_update.txt", "r")
    # file = f.read()

    # for line in file.split("\n"):
    #     chocol = line
    #     chocolate.append(list(chocol))


    for chocol in chocolate:
        p = []
        if (chocol != []):
            for c in chocol:
                indices = [i for i, x in enumerate(recipe) if x == c]
                if (len(indices)!=0):
                    random.shuffle(indices)
                    p.append(str(indices[0])) 
                else:
                    print("WARNING: NOT SUPPORTED [{}]".format(c))
        paste.append(p) 


    croissant = ""


    for layers in paste:
        if (layers == []):
            croissant = croissant + "."
        for layer in layers:
            roll = ""
            for crust in list(layer):
                roll = roll + ("".join([random.choice(list(materials)) for i in range(int(crust))])) + ","
            croissant = croissant + roll[:-1] + ":"
        croissant = croissant[:-1] + "."

    
    f = open("./sended_croissants/"+fileName+".txt", "w")
    f.write(croissant[:-1])
    f.close()

    hostname = "XX.XX.XX.XX"
    username = "USER"
    password = "PASS"

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
    destLoc = "/root/msgBroker/messages/"+folder_name
    allData = ["./sended_croissants/"+fileName+".txt"]
    for filetosend in allData:
        filename = os.path.basename(filetosend)
        destFile = os.path.join(destLoc,filename) #renaming the file
        print("file to send : ", filetosend)
        print("receive : ", destFile)
        sftp_client.put(filetosend, destFile) #send datafile filetosend to destFile
        with open('RFidgetRunLogs.txt','a') as file:
            file.write(f"{filetosend}, {destFile}\n") #add the run logs


    sftp_client.close()
