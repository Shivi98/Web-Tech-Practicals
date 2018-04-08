def main():
    elements = input("Enter list of elements: ").strip()
    elements = elements.split(" ")
    elements = [int(i) for i in elements]
    elements.sort()
    print(elements)
    element = int(input("Enter an element to search: "))
    result, index = binarySearch(elements, element)
    if result:
        print("Element found at index: ", index + 1)
    else:
        print("Element not found")


def binarySearch(elements, element):
    lo, hi = 0, len(elements) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if elements[mid] < element:
            lo = mid + 1
        elif element < elements[mid]:
            hi = mid - 1
        else:
            return True, mid
    return False, 0


main()
