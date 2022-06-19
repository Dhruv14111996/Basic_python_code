# Here i am creating decorator to check perfoermance

from time import time


def performance(fun):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fun(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} sec')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i*5


long_time()

print('--------------------------------------------------------------------')

user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
