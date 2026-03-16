def sumNum(*args):
    total = sum(args)
    return total

print(sumNum(1,2,3,4,5,1))


def save_user(**kwargs):
    user_data = {}
    for key in kwargs.items():
        user_data[key] = value
    return user_data

print(save_user(name = 'Pasha', age = 28, isSaw = True ))


