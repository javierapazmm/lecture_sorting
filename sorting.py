#[]><
import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    data = {}
    with open(file_path, "r", ) as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csvfile)

        for header in headers:
            data[header] = []

        for row in csv_reader:
            for i, value in enumerate(row):
                data[headers[i]].append(float(value))

    return data

def selection_sort(seznam, direction):
    size = len(seznam)

    if direction == "v":
        for idx in range(size):
            min_idx = idx

            for i in range(idx + 1, size):
                if seznam[i] < seznam[min_idx]:
                    min_idx = i
            (seznam[idx], seznam[min_idx]) = (seznam[min_idx], seznam[idx])

    elif direction == "s":
        for idx in range(size):
            max_idx = idx

            for i in range(idx + 1, size):
                if seznam[i] > seznam[max_idx]:
                    max_idx = i
            (seznam[idx], seznam[max_idx]) = (seznam[max_idx], seznam[idx])

    else:
        seznam

    return seznam

def insertion_sort(seznam):
    size = len(seznam)
    for i in range(1, size):
        key = seznam[i]
        j = i - 1
        while j >= 0 and key < seznam[j]:
            seznam[j+1] = seznam[j]
            j -= 1
        key = seznam[j + 1]

    return seznam

def bubble_sort(seznam):
    size = len(seznam)
    for i in range(size):
        for j in range(0, size - i -1):
            if seznam[j] > seznam[j+1]:
                (seznam[j],seznam[j+1]) = (seznam[j+1], seznam[j])


    return seznam


def main():
    file_name = "numbers.csv"
    data = read_data(file_name)
    seznam = [9, 2, 3, 4, 7, 5, 9, 12]
    selection = selection_sort(seznam, "s")
    bubble = bubble_sort(seznam)
    insertion = insertion_sort(seznam)


    print(insertion)



if __name__ == '__main__':
    main()
