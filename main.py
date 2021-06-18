import time

def prime(num):
    for i in range (1,num+1):
        for j in range(2,i):
            if i%j==0:
                print(i , "is not a prime number")
                time.sleep(5)
                break

            else:
                print(i , "is a prime number")
                time.sleep(5)
                break





prime(10)

