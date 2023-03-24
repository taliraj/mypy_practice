def simple_optionals1(arg):  # change only this line
    arg = 1
    arg = None
    print(arg)


def simple_optionals2(arg):  # change only this line
    arg = 1.0
    arg = "test"
    print(arg)


def simple_optionals3(arg):  # change only this line
    arg = True
    arg = "test"
    arg = None
    arg = 1
    return arg


def collections1(arg):  # change only this line
    arg = [1]
    print(arg)


def collections2(arg):  # change only this line
    arg = {1, 2, 3}
    arg = [1, 2, 3]
    return arg


def collections3(arg):  # change only this line
    arg = (1, "test", 1.0)
    print(arg)


def collections4(arg):  # change only this line
    arg = 1
    arg = (1, "test", 1.0)
    print(arg)

 
def collections5(arg):  # change only this line
    arg = ("name", "test", 1.0)
    arg = (1, "test", 1.0)
    return arg
