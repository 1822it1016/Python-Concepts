import multiprocessing
import time


def increment_counter(counter, lock):
    for _ in range(5):
        lock.acquire()
        counter.value += 1  
        print(f"Counter: {counter.value}")
        lock.release()
        time.sleep(0.1)  # Simulate some work


if __name__ == "__main__":
    counter = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()

    processes = []
    for _ in range(3):
        p = multiprocessing.Process(target=increment_counter, args=(counter, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Final Counter Value:", counter.value)