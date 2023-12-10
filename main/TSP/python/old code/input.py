def seed_input(): #The name said it all
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

def distance_input(n): #In case there is no distance, we input it
    distance = [0] * n
    for i in range(n):
        distance[i] = [0]*n
        for j in range(i+1,n):
            distance[i][j] = int(input("Distance of city "+i+" and city "+j+" is: "))
    return distance
