list=[5,10,15,20,25,50,20]
def my_list(list):
    i = 0
    for i in range (len(list)):
        if list[i]==20:
            list[i]=200
    print(list)
my_list(list)