import csv
import os
print("Current working directory:", os.getcwd())


def read_csv(filename):
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print("The file does not exist.")


filename = input("Enter the CSV file name to read: ")
read_csv(filename)










# /Users/samarthdevadiga/Desktop/Suprise Assignment 01/3. Advanced (61–90-100)/85data.csv