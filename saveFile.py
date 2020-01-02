import csv

# Initialize csv file
fileName = input('Please enter a file name: ')
with open(fileName, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while True:
        filewriter.writerow([timePassed, voltage])
        time.sleep(0.1)
        timePassed = timePassed + 0.1
