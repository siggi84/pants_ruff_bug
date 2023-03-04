import numpy
from scipy.special import cbrt
from hello_user import hello_user

if __name__ == "__main__":
    print(hello_user("John Doe"))

    cb = cbrt([27, 64])
    print(cb)
