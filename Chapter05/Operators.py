__author__ = 'zhangfuqiang'

x = 1
y = 2
z = 3
w = x if y else z
print('x if y else z: ', w)

w = x or y
print('x or y: ', w)

w = x and y
print('x and y: ', w)

# object identity test
v = x
print('v is x: ', v is x)

w = x | y
print('x | y: ', w)

w = x ^ y
print('x ^ y: ', w)

w = x | y
print('x & y: ', w)

w = x // y
print('x // y: ', w)

w = ~x
print('~x: ', w)

# 1011
# 0100
# 1011
