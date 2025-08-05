class SampleFlask:
    def __init__(self):
        pass
    def route(selfself, func):
        def wrapper():
            print(func.__name__,)
            func()
            print(func.__name__,)
        return wrapper
app = SampleFlask(__name__)

@app.route
def hello():
    print("hello")
if __name__ == '__main__':
    hello():