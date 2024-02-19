import os

# a strong 128 bit method for accessing flag
# this is still beta app, so even admin can't control the method for now.
def create_method():
    return [*str(os.urandom(128))]

strong_method = create_method()
