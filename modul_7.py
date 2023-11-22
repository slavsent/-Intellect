from time import time


def timing(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            func(*args, **kwargs)
            end_time = time()
            execution_time = end_time - start_time
            print(f"Время выполнение функции: {execution_time} секунд")
            if execution_time > n:
                print(f"Время выполнения: {execution_time} больше установленного {n}")

        return wrapper
    return decorator


if __name__ == '__main__':
    pass
