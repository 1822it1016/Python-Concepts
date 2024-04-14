import time


def print_name():
    print("Wait started")
    time.sleep(5)
    print("Wait is done")
    while(True):
        name = input("Enter name")
        print(f"name is {name}")
        yield(name)

name = print_name()
print(next(name))
print(next(name))
print(next(name))
print(next(name))