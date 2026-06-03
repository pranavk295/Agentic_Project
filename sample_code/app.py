# Fixed divide function to correctly perform division
# No bugs found in this code.

def add(x,y):
    return x + y
def divide(x,y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"