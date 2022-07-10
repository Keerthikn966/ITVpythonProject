import datetime
import os
import json
import csv
values = []

print("The file content are: ")
l1 = ['2022-05-09 00:00:01', '2022-05-30 00:00:31']
l2 = ['2022-05-11 00:01:01', '2022-05-31 00:02:01']
l3 = ['2022-05-11 00:01:01', '2022-05-31 00:02:01']
lst = []

lst.append(l1)
lst.append(l2)
lst.append(l3)
jsonString = json.dumps(lst)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
absolutepath = os.path.abspath('data.json')
with open(absolutepath) as f:
   data = json.load(f)

print(data)
print("Data:::::")
header = ['StartDateandTime', 'EndDateAndTime']
datas = [['2022-05-09 00:00:01', '2022-05-30 00:00:31'],
        ['2022-05-11 00:01:01', '2022-05-31 00:02:01'],
        ['2022-05-11 00:01:01', '2022-05-31 00:02:01'],
        ['2022-05-31 00:02:01', '2022-05-31 00:06:03'],
        ['2022-05-31 00:03:01', '2022-05-31 00:04:01'],
        ['2022-05-31 00:04:01', '2022-05-31 00:34:01']]

with open('DataList.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(datas)
'''with open("C:/Users/My PC/PycharmProjects/ITVpythonProject/DataInput.json") as fic:
    for line in fic:
        line = line.rstrip(",\r\n")
        row = list(map(string, line.split(",")))
        values.append(row)'''

'''txt_file = open("C:/Users/My PC/PycharmProjects/ITVpythonProject/DataInput.json", "r")
file_content = txt_file.read()
print("The file content are: ", file_content)

content_list = file_content.split('\n')
txt_file.close()
'''
print("The list is: ")
