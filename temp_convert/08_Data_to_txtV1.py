# Source: https://www.guru99.com/reading-and-writing-files-in-python.html

# Data to be outputted
data = ['First', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# get filename, cant be blank / invalid
# assume valid data for now
filename = input("Enter a Filename (leave off the extension): ")

# add .txt suffix!
filename += ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at the end of each item
for item in data:
    f.write(item + "\n")

# colse file
f.close()