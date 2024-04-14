import time 
import threading 



answer_square = []
answer_cube= []
def calculate_square(n: list):
    for i in n:
        time.sleep(0.5)
        print(f"Square of i is {i*i}")
        answer_square.append(i*i)

def calculate_cube(n: list):
    for i in n:
        time.sleep(0.5)
        print(f"Cube of i is {i*i*i}")
        answer_cube.append(i*i*i)        


if __name__ == "__main__":
    li = [2,4,5,6]
    thread1 = threading.Thread(target=calculate_square, args=(li,))
    thread2 = threading.Thread(target=calculate_cube, args=(li,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(answer_square)
    print(answer_cube)




