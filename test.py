# -*- coding: UTF-8 -*-
import requests
import threading
import time
import sys

class Test(threading.Thread):
    def __init__(self, req_num=10):
        super(Test, self).__init__()
        self.req_num = req_num
    
    def echo(self, txt):
        sys.stdout.buffer.write(txt)
        sys.stdout.buffer.flush()
        print("\n")

    def timeapi(self):
        x = requests.get('http://127.0.0.1:8080/timeapi')
        self.echo(x.text.encode("UTF-8"))

    def count(self):
        x = requests.get('http://127.0.0.1:8080/count')
        self.echo(x.text.encode("UTF-8"))
    
    def run(self):
        st = time.time()
        for i in range(self.req_num):
            self.timeapi()
            self.count()
        en = time.time()
        print("END, taking %f sec to perform %d query(time, count)"%(en-st, self.req_num))

thread_num = 100
epoches = 10

for ep in range(epoches):
    thds = [ Test() for _ in range(thread_num) ]
    for i in range(thread_num):
        thds[i].start()
    for i in range(thread_num):
        thds[i].join()
    print("Next Epoch")

print("END Test")