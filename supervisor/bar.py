import random
import time

while True:
    with open('test.out', 'a') as f:
        f.write("hello python!\n")

    time.sleep(random.randint(1, 10))

