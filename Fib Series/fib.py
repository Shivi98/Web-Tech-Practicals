def fib(n=0):
    temp_list = []
    a, b = 0, 1
    for i in range(n):
        temp_list.append(a)
        temp = a
        a = b
        b += temp
    return temp_list


def main():
    n = int(input("Enter number of elements in series: "))
    fib_list = fib(n)
    print(fib_list)


main()
