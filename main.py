import time


# Python Decorators
def delay_decorator(function):
    def wrapper_function():
        print("Wait 3 seconds as this function is being decorated :D")
        time.sleep(3)
        function()
        print("Thanks for waiting!\n")
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


@delay_decorator
def say_greeting():
    print("How are you?")


if __name__ == "__main__":
    say_hello()
    say_bye()
    say_greeting()
