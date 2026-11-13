# Print your name and age, then read a number and print it doubled

def solve():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Name: {name}")
    print(f"Age: {age}")

    number = int(input("Enter a number: "))
    print(f"Doubled number: {number * 2}")


solve()