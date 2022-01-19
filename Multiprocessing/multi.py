from multiprocessing import Process, Pipe
my_numbers = [3, 4, 5, 6, 7, 8]

def cube(x):
   for x in my_numbers:
       print('%s cube is %s' % (x, x**3))


def evenno(x):
   for x in my_numbers:
       if x % 2 == 0:
           print('%s is an even number ' % (x))

if __name__ == '__main__':
    my_process1 = Process(target=cube, args=('x',))
    my_process2 = Process(target=evenno, args=('x',))

    my_process1.start()
    my_process2.start()
    
    my_process1.join()
    my_process2.join()
print ("Done")
