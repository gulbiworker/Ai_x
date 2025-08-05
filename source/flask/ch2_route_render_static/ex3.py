def check(func):
    def wrapper():
        print(func.__name__,)
        func()
        print(func.__name__,)
    return wrapper

@check
def hello():
    print("hello")
@check
def world() : 2개의 사용위치
    print('world')

if __name__=="main"__:
   hello()
   world()