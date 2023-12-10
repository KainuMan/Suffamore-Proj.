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

def number_input(entites="what ever you have"):
    n = int(input("Number of "+entites+": "))
    return n

def distance_input(n):
    distance = []
    l = []
    for i in range(n):
        for j in range(i+1,n):
            a = int(input("Distance of city "+str(i)+" and city "+str(j)+" is: "))
            l.append(a)
        distance.append(l)
    return distance

def not_input(n,d,x,time):
    print("Distance of the cities:")
    for i in range(n):
        print(d[i])
    print("\n")
    print("Shortest way is:",x[1],"with the distance of:",x[0])
    print(f"Calculation time: {time} seconds.")