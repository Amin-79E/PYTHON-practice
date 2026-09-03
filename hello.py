def print_row(space,bricks):
    for i in range(space,0,-1):
        print(" ", end ="")

    for k in range(bricks):
        print("#" ,end="")

    print()

def get_height():
    n = (input("ENter the height: "))
    return n

def main():
    while True:
        m = get_height()
        if m<1 or m>8:
            break

    for i in range(m):
        print_row(m-1-i , m+i)
