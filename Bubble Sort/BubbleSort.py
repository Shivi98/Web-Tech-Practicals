def main():
    elements = input("Enter a list of numbers (Like a b c d ...): ").strip()
    elements = elements.split(" ")
    elements = [int(element) for element in elements]
    if elements:
        bubble(elements)
        print("Sorted List: ", elements)
    else:
        print("Enter a valid list of elements")


def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i + 1]:
                sorted = False
                bad_list[i], bad_list[i + 1] = bad_list[i + 1], bad_list[i]
