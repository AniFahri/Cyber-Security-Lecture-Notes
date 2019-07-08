import sys

import time



print("Sample program started...")



index = 0



while True:

    print("Looping at index:{}".format(index))

    sys.stdout.flush()

    time.sleep(1)

    index = index + 1



print("Sample program stopped...")