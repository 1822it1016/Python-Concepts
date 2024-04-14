import time
import multiprocessing


def calculate_square(n: list, queue):
    for i in n:
        time.sleep(0.5)
        print(f"Square of {i} is {i*i}")
        queue.append(i*i)


def calculate_cube(n: list, queue):
    for i in n:
        time.sleep(0.5)
        print(f"Cube of {i} is {i*i*i}")
        queue.append(i*i*i)


if __name__ == "__main__":
    li = [2, 4, 5, 6]
    manager = multiprocessing.Manager()
    queue_square = manager.list()
    queue_cube = manager.list()
    lock = multiprocessing.Lock()

    process1 = multiprocessing.Process(target=calculate_square, args=(li, queue_square))
    process2 = multiprocessing.Process(target=calculate_cube, args=(li, queue_cube))
    process1.start()
    process2.start()
    process1.join()
    process2.join()

    print("Answer square:", queue_square)
    print("Answer cube:", queue_cube)
