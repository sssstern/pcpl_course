import random

def gen_random(amount,begin,end):
    result = []
    for i in range(amount):
        result.append(random.randint(begin,end))
    return result

if __name__ == "__main__":
    print(list(gen_random(5, 1, 3)))