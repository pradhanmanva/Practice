class MyError(RuntimeError):
    def __init__(self,arg):
        self.args=arg


try:
    raise MyError("Omg Help")
except MyError as e:
    print("It happens. ")