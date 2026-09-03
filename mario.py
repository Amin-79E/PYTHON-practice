def print_row(space,bricks):
    for i in range(space,0,-1):
        print(" ", end ="")

    for k in range(bricks):
        print("#" ,end="")

    print()

def get_height():
     while True:
         try:
            n = int(input("Enter the height: "))
            return n
         except ValueError:
                  continue


def main():
    while True:
        m = get_height()
        if  1<=m<=8:
            break

    for i in range(m):
        print_row(m-1-i , 1+i)

if __name__ == "__main__":
    main()