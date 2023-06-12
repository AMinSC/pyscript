import inspect

frame = None

def func():
    global frame
    x = 10
    y = 20
    print(x + y)
    frame = inspect.currentframe()

if __name__ == "__main__":
    func()
    print(frame.f_locals)
    print(frame.f_back)
    print(frame.f_lasti)
    print(frame.f_code)
