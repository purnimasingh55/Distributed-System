'''

We need not to write main thread in python

run is only function which run as default in threading in python
'''

import time
from threading import *
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            time.sleep(1)
class Byee(Thread):
    def run(self):
        for i in range(5):
            print("byee")
            time.sleep(1)
t1 = Hi()
t2 = Byee()
t1.start()
t2.start()