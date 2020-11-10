# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
import random
import string


def random_generator(max_length=20):
    valid_set = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(valid_set) for _ in range(max_length))


if __name__ == '__main__':
    for i in range(10):
        print(random_generator())
