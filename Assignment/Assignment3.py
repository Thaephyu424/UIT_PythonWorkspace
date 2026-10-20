# Assignment3 No1

numbers = list(range(1, 11))
print(numbers)

# Assignment3 No2
number=list(range(2,101,2))
print("Even Numbers: ",number)

# Assignment3 No3
number=list(range(2,51,2))
print("Even Numbers: ",number)

number=list(range(51,100,2))
print("Odd Numbers: ",number)

# Assignment3 No4
factorials = []
current = 1

for i in range(1, 11):
    current *= i
    factorials.append(current)

print(factorials)


# Assignment3 No5
primes = []

for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(primes)

# Assignment3 No6
names = ["alice", "bob", "Anna", "alex", "david", "Amanda", "charlie"]

result = [name.upper() for name in names if name[0].lower() == 'a']

print(result)

#Assignment3 No7
result_dict = {i: ('even' if i % 2 == 0 else 'odd') for i in range(1, 11)}

print(result_dict)

# Assignment3 No8
names = ["abc", "mno", "pqr", "xyz"]
marks = [90, 55, 78, 66]

# Dictionary comprehension with zip
result = {k: v for k, v in zip(names, marks)}
print(result)

# Using dict() and zip()
result = dict(zip(names, marks))
print(result)


# Using map, zip, and dict
result = dict(map(lambda item: (item[0], item[1]), zip(names, marks)))
print(result)

# Assignment3 No.9
original_dict = {'a': 1, 'b': 2, 'c': 9}


inverted_dict = {v: k for k, v in original_dict.items()}

print(inverted_dict)


# Assignment3 No10
primes = []

for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

squares = [p ** 2 for p in primes]

print(squares)

# Assignment3 No11
s = "aa12bb4c3d56"

result = [int(char) for char in s if char.isdigit()]

print(result)
