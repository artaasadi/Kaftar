import random

if __name__ == "__main__":

    NAME = "LIGHTA"

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

    
    f = open("./sended_croissants/croissant.txt", "w")
    f.write(croissant[:-1])
    f.close()

