__author__ = 'zhang fu qiang'

source = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [3, 4, 5]]
print(source)
column_num = len(source[0])
target = []
for i in range(column_num):
    target.append([row[i] for row in source])

print(target)

