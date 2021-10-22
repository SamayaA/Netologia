from datetime import datetime
import os
import sys
sys.path.append('c:\\Users\\Samaya\\Desktop\\Учеба\\Netology\\OOP\\Netologia\\pro python\\homework_1\\application')
from salary import calculate_salary

def timeit(log_path):
    def log(func):
        def wraper(*args, **kwargs):
            with open(log_path,'a') as f:
                f.write(f'{datetime.now()}\
                    \nfunction name = {func.__name__}\
                    \nargs = {args}\tkwargs = {kwargs}\n')
                result = func(*args, **kwargs)
                f.write(f'return value = {result}\n\n')
            return result
        return wraper
    return log


@timeit(os.getcwd() + '\\file.log')
def foo(*args, **kwargs):
    return sum(args)

if __name__ == "__main__":
    l = [i for i in range(5)]
    foo(*l)
    #task 3
    a = timeit(os.getcwd() + '\\file.log')(calculate_salary)()




