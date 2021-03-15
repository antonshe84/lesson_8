"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
 исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


# >>> a = calc_cube(5)
125
# >>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""
from functools import wraps


def val_checker(arg_f):
    def val_checker_0(func):
        @wraps(func)
        def wrapper(num):
            if arg_f(num):
                print(func(num))
            else:
                raise ValueError(f"wrong val {num}")

        return wrapper

    return val_checker_0


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    print(calc_cube.__name__)
    a = calc_cube(5)
    b = calc_cube(-6)
except ValueError as exc:
    print(f"Value Error: {exc}")
