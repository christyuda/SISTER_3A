#Spawn a Process – Chapter 3: Process Based Parallelism
import multiprocessing

def myFunc(i):
    print ('Karryawan Mengerjakan tugas : %s' %i)
    for j in range (0,i):
        print('Tugas dikerjakan karyawan :%s' %j)
    return

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()