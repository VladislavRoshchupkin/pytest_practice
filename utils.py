def is_even(n: int) -> bool:
    return n % 2 == 0

def divide(a, b):
    return a / b

def get_user_age(users, name):
    return users[name]

def safe_divide(a,b):
    if b == 0:
        return "Делить на ноль нельзя"
    return a/b