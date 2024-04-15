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
    with open(file_path, "r", newline= "") as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csvfile)

        for header in headers:
            data[header] = []

        for row in csv_reader:
            for i, value in enumerate(row):
                data[headers[i]].append(float(value))

    return data

def selection_sort(seznam):
    size = len(seznam)
    for idx in range(size):
        min_idx = idx

        for i in range(idx + 1, size):
            if seznam[i] < seznam[min_idx]:
                min_idx = i
        (seznam[idx], seznam[min_idx]) = (seznam[min_idx], seznam[idx])

    return seznam



def main():
    file_name = "numbers.csv"
    data = read_data(file_name)
    seznam = [9, 2, 3, 4]
    selection = selection_sort(seznam)
    print(selection)



if __name__ == '__main__':
    main()
