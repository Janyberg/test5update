def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            if type(x)==int and float:
                print("don't do that again")
            else:
                print(x , " end of line")
        return function_wrapper
    return greeting_decorator

@greeting("")
def foo(x):
    print('')

foo('beginning of line...')
