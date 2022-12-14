import random
import random
import paramiko
import os
import sys


folder_name = ''


def eat(fileName) :
    
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
    
    
    #------------------------------------------------
    
    
    NAME = "User"

    f = open("recipe.txt", "r")
    recipe = list(f.read())

    f = open("./received_croissants/"+fileName+".txt", "r")
    pack = f.read().split(".")

    cover_date = []
    for croissant in pack[:2]:
        date = []
        for roll in croissant.split(":"):
            bite = ""
            for crust in roll.split(","):
                bite = bite + str(len(crust))
            date.append(recipe[int(bite)])
        cover_date.append("".join(date))
    print()
    print("------------------------------")
    print(" {} | {} ".format(cover_date[0],cover_date[1]))
    print("------------------------------")


    print(" {} :".format(NAME))
    for croissant in pack[2:]:
        if (croissant == ""):
            # read enter: [\n]
            print(" {}|  ".format( "".join([" " for i in range(len(NAME)+1)]) ) )
        else:
            yamyam = []
            for roll in croissant.split(":"):
                bite = ""
                for crust in roll.split(","):
                    bite = bite + str(len(crust))
                yamyam.append(recipe[int(bite)])

            print(" {}|  ".format( "".join([" " for i in range(len(NAME)+1)]) ) + "".join(yamyam))
    print("------------------------------")
    print()


