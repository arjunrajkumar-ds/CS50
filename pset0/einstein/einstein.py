# Program that takes an input for mass & calculates the Energy output
# E = mc^2, 
# E = Joules
# m = mass
# c = constant 300000000

def main():
    mass = int(input("m: "))
    c = 300000000
    energy = mass * c * c
    print("E:", energy)

main()