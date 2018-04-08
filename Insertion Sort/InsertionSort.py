def main():
    elements = input("Enter a list of numbers (Like a b c d ...): ").strip()
    elements = elements.split(" ")
    elements = [int(element) for element in elements]
    if elements:
        insertionSort(elements)
        print("Sorted List: ", elements)
    else:
        print("Enter a valid list of elements")


def insertionSort(elements):
    for i in range(1, len(elements)):
        j = i
        temp = elements[j]
        while j > 0 and temp < elements[j - 1]:
            elements[j] = elements[j - 1]
            j = j - 1
        elements[j] = temp


main()
