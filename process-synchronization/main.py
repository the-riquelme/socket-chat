from threading import *
from time import sleep

count = 0


class Process(Thread):
    def __init__(self, position, semaphore):
        Thread.__init__(self)
        self.position = position
        self.semaphore = semaphore

    def run(self):
        global count
        while True:
            semaphore.acquire()
            print("Processo: {0} entrou na regiao critica, contador: {1}".format(
                self.position, count))
            count = count + 1
            print("Processo: {0} saiu da regiao critica, contador: {1}".format(
                self.position, count))
            semaphore.release()
            sleep(1)


semaphore = Semaphore(1)
for i in range(10):
    process = Process(i, semaphore)
    process.start()
