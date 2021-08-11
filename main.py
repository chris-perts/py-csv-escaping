import csv

evil_string = '''a'a\\'b"c>?>%}}%%>c<[[?${{%}}cake\\'''

def print_csv_file(filename):
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print(', '.join(row))

print("Non-evil csv file, with unicode, parsed:\n")

print_csv_file('eggs.csv')

print("\nCsv file with trailing backslash, parsed:\n")

print_csv_file('evil_eggs.csv')

print("\nCsv file with PERTS problematic value automatically encoded, then parsed:\n")

filename = 'perts_example_auto.csv'
with open(filename, 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(["🍔"] + ['Spam'] * 4 + ['Baked Beans'])
    spamwriter.writerow(['Spam', evil_string, 'Wonderful Spam'])
print_csv_file(filename)
