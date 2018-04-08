def main():
    elements = input("Enter list of elements: ").strip()
    elements = elements.split(" ")
    element = input("Enter an element to search: ")
    result, index = linearSearch(elements, element)
    if result:
        print("Element found at index: ", index + 1)
    else:
        print("Element not found")


def linearSearch(elements, element):
    for i in range(0, len(elements)):
        if element == elements[i]:
            return True, i
    return False, 0


main()
