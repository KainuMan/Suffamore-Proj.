def seed_input():
    asking = input("Import your seed? (y/n) ")
    if (asking == "y" or asking == "Y"):
        seed = int(input("Seed: "))
    else:
        seed = None
        if (asking == "n" or asking == "N"):
            print("Well, you choose randomized then")
        else:
            print ("GO TO HELL!")
    return seed

def number_input(entites):
    n = int(input("Number of "+entites+": "))
    return n