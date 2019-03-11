'''
Iterator Design Pattern
- any code that you write using iterators is decoupled from the data structure
that the code is manipulating
- access the elements of a collection(class) in sequential manner without
understanding the underlying layer design
'''

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

f = fib()
print(type(f))
for i in range(20):
    print(next(f), end=' ')
print()

def count_to(count):
    nums = ['one', 'two', 'three', 'four', 'five']
    for num in nums[:count]:
        yield num

count_to_two = count_to(2)
count_to_five = count_to(5)

for count in [count_to_two, count_to_five]:
    for number in count:
        print(number, end=" ")
    print()
    
    
