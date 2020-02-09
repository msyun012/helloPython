# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using
# the split() method. The program should build a list of words.
# For each word on each line check to see if the word is
# already in the list and if not append it to the list.
# When the program completes, sort and print the resulting
# words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt




fname = input("Enter file name: ")
if len(fname) < 1: fname = "romeo.txt"

fh = open(fname)
lst = list()
sen = ""

for line in fh:
    line = line.rstrip()
    sen = line.split()

    for ln in sen:
        if ln not in lst:
            lst.append(ln)

lst.sort()

print(lst)

# print(lst)
#    sen = sen + line
#    lst = sen.split()

# for line in lst:
