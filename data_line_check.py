import re

file = open("/Users/gmnine/Pycharm_Projects/pythonProject/review_extraction.csv","r",encoding="utf-8")

# for line in file:
#
#     # a = line.count
#     # print(len(a))
#     if line == "\n":
#         print('yes',line)

data_lines = []
no_data_lines = []
comma_data_lines = []

# r = re.compile('^,')
# a = r.search()
# print(a)

for line in file:
    if line != "\n":
        data_lines.append(line)
    if line == "\n":
        no_data_lines.append(line)

    if re.search("^,",line):
        comma_data_lines.append(line)


data_lines_count = len(data_lines)
no_data_lines_count = len(no_data_lines)

full_lines_count = data_lines_count + no_data_lines_count

comma_data_lines_count = len(comma_data_lines)




print("data_lines_count =",data_lines_count)
print("no_data_lines_count =",no_data_lines_count)
print("full_lines_count =",full_lines_count)

print("comma_data_lines_count =",comma_data_lines_count)

file.close()