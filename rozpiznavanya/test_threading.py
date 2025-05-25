import threading
import time


def print_cube(num):
    print("Cube: {}" .format(num * num * num))
    time.sleep(3)
    


def print_square(num):
    print("Square: {}" .format(num * num))
    time.sleep(3)

def print_perimeter(num):
    print(f"Perimetr {num*4}")
    time.sleep(3)



def print_cube2(num):
    print("Cube: {}" .format(num * num * num))
    time.sleep(3)
    
def print_square2(num):
    print("Square: {}" .format(num * num))
    time.sleep(3)

def print_perimeter2(num):
    print(f"Perimetr {num*4}")
    time.sleep(3)




if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    t3 = threading.Thread(target=print_perimeter, args=(10,))
    t4 = threading.Thread(target=print_square2, args=(10,))
    t5 = threading.Thread(target=print_cube2, args=(10,))
    t6 = threading.Thread(target=print_perimeter2, args=(10,))

    start_1 = time.time()

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    print(f"Time: {time.time()-start_1}")
    print("Done!")