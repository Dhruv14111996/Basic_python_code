import csv

with open('new.csv', 'r') as csv_file:
    re = csv.reader(csv_file)

    for line in csv_file:
        print(line)

with open('new.csv', 'a') as csv_file:
    text = csv_file.write(
        '\nMy fav topic is nature...')

    print(text)

# with write comand we can creat new file but for that we need to mention that new file name and 'write'
# function.

with open('game.csv', 'r') as csv_file:
    re = csv.reader(csv_file)

    for line in csv_file:
        print(line)


with open('game.csv', 'a') as csv_file:
    text = csv_file.write(
        '\nI am making game like PUBG...')

    print(text)
