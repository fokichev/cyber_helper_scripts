import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help="Filename of file to be ammended")
parser.add_argument("-d", "--data", help="Data to be added at every interval")
parser.add_argument("-i", "--interval", help="Interval at which data is to be added")

args = parser.parse_args()

file = args.file if args.file else input("Please enter the filepath of file to be ammended: ")
data = args.data if args.data else input("Please enter data to be added at intervals: ")
interval = int(args.interval if args.interval else input("Please enter interval at which data is to be added: "))

# open and read file into array
f = open(file, "r")
file_arr = list(filter(None, f.read().split("\n")))
f.close()

# at intervals insert data
i = 0
while i < len(file_arr):
    file_arr.insert(i, data)
    i = i + interval

# save as "filename_data_every_interval.ext"
new_file_path = file.rsplit(".", 1)[0] + "_" + data + "_every_" + str(interval) + "." + file.rsplit(".", 1)[1]

with open(new_file_path, "w") as f:
    for i in range(len(file_arr)):
        if i < len(file_arr): f.write(file_arr[i] + "\n")
        else: f.write(file_arr[i])
f.close()

print("Success! Entries are now: ")
print(file_arr)