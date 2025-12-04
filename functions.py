# def greeeting():
#     print("hello hey")

# greeeting()

# def sum ():
#     a = 10
#     b = 20
#     c = 30
#     total = a + b + c
#     print (f"the total is, {total} and values are {a}, {b} and {c}")

# sum()

#using arguments
# def total (x,y,z):
#     total = x + y + z
#     return (f"the total is, {total} and values are {x}, {y} and {z}")


# print(total(2,6,4))     

x = int(input("enter ur 1st: "))
y= int(input("enter ur 2nd: "))
z= int(input("enter ur 3rd: "))

def total (x,y,z):
    total = x + y + z
    return (f"the total is, {total} and values are {x}, {y} and {z}")


print(total(x,y,z))