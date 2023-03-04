from hello_user import hello_user
from scipy.special import cbrt

if __name__ == "__main__":
    print(hello_user("John Doe"))

    cb = cbrt([27, 64])
    print(cb)
