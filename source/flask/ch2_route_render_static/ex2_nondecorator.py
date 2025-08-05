def check(func):
    def wrapper():
        print(func.__name__,)
        func()
        print(func.__name__,)
    return wrapper


def hello():
    print(hello.__name__,'함수 전처리 작업 함')
    print("hello")
    print(hello.__name__, ' 함수 후처리 작업 함')

def world() : 2개의 사용위치
    print(world.__name__,)
    print('world')
    print(hello.__name__,)

if __name__=="main"__:
    trace_hello() = check(hello)
    trace_hello()
    trace_world() = check(world)
    trace_world()