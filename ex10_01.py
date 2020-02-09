# 10.2 Write a program to read through the mbox-short.txt and
# figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding
# the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

times = dict()

for line in handle:

    line = line.strip()

    if not line.startswith("From "): continue
    words = line.split()
    time = words[5]
    time2 = time[0:2]
    times[time2] = times.get(time2,0) + 1

times2 = list()
for key, val in times.items():
    newtup = (key, val)
    times2.append(newtup)

times2 = sorted(times2)

for key, val in times2:

    print(key, val)


#    for words in line:

#    print(line)
#    print(words)
#    print(time)
#    print(time2)
# print(times)
# print(times2)
# print("")


#    time
