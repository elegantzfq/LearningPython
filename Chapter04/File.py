

f = open('file_test.txt', 'r')
lines = f.read().split()
print(lines)

ff = open(file='file_test.txt', mode='r', encoding='utf-8')
print(ff.read())
