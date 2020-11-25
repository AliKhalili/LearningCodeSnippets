import random
import string


def random_generator(max_length=20):
    valid_set = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(valid_set) for _ in range(max_length))
