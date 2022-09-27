import random

if __name__ == "__main__":

    NAME = "RX"

    f = open("recipe.txt", "r")
    recipe = list(f.read())

    f = open("./received_croissants/croissant.txt", "r")
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
