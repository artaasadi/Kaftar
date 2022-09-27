from asyncore import write
from operator import index
import random


if __name__ == "__main__":

    materials = ""
    materials_base = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/.>,<\'\";:]}[{|\\+=_-)(*&^%$#@?!`~•"
    for i in range(10):
        materials = materials_base + materials 

    materials = list(materials)
    random.shuffle(materials)
    materials = "".join(materials)

    f = open("recipe.txt", "w")
    f.write(materials)
    f.close()

