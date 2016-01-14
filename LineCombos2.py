import csv
import pandas as pd

file = open("Test.csv", newline="")
i_file = csv.reader(file, quotechar='|')

for row in i_file:
    print(row)