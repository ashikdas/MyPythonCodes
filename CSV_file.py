import csv
"""
file = open('example.csv')
file_reader = csv.reader(file)

# data = list(file_reader)
# print(data)
# print(data[1][2])

for row in file_reader:
    print('Row no = '+str(file_reader.line_num)+' '+str(row))
"""
output_file = open('out.csv', 'a', newline='')
output_writer = csv.writer(output_file, delimiter='.')
output_writer.writerow(['1', '2', '3', '4'])
output_writer.writerow(['11', '12', '13', '14'])
output_file.close()