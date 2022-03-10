def data(**args):
    print(args)

def arg(*args):
    print(args[0][1])

dict1={"name":"saikat","age":15}


# data(**dict1)

arg([1,3,5])