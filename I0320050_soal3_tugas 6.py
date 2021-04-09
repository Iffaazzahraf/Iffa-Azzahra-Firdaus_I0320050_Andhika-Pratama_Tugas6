#membuat program menentukan bilangan prima pada range(10,25)
for x in range(10,25):
     for i in range(2, x):
        if x % i == 0:
            print(x, "bukan prima")
            break
     else:
        print(x, "adalah bilangan prima")



