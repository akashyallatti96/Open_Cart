import random
import string


# def randon_string_generator(size=8,chars=string.ascii_lowercase+string.digits):
def randon_string_generator(size=8,chars=string.ascii_lowercase):
    return "".join(random.choice(chars) for char in range(size))