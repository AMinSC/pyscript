def producer(coroutine):
    print('Starting producer')
    for i in range(1, 5):
        print(f'Producing data {i}')
        coroutine.send(i)
    print('Producer done')
    coroutine.close()

def consumer():
    print('Starting consumer')
    while True:
        i = (yield)  # Receive a 'i' value from the producer
        print(f'Consuming data {i}')

c = consumer()
next(c)  # Start consumer coroutine
producer(c)
