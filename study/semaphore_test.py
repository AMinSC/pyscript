import threading

# Create a semaphore that allows up to 5 threads at a time
semaphore = threading.Semaphore(5)

def my_task():
    # Acquire the semaphore
    with semaphore:
        # Only up to 5 threads can execute this section at a time
        ...

threads = [threading.Thread(target=my_task) for _ in range(100)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
