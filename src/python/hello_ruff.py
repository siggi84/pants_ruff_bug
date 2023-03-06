 # Fixable unused-import (F401)
import numpy

# Unfixable import-star-usage (F405)
from hello_user import * #

if __name__ == "__main__":
    print(hello_user("John Doe"))
