import requests
import string
import random
from random import randint
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

for i in range(1000000):
    print("===================================")
    print(i)

    randn = randint(8, 24)
    randn1 = randint(5, 15)

    user=id_generator(randn1)
    passw = id_generator(randn)

    files = {
    'email': (None, '{}@gmail.com'.format(user)),
    'password': (None, passw),
     }
    print("email:{}\npassword:{}".format('{}@gmail.com'.format(user), passw))

    response = requests.post('https://www.google.com', files=files)
    # print(response.text)
