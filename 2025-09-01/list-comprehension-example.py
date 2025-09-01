# 제곱수 예시 (for 문)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
# output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(x)
# output: 9

# 제곱수 예시 (리스트 컴프리헨션)

squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]



# 리스트 결합 예시 (for 문)

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

# 리스트 결합 예시 (리스트 컴프리헨션)

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(combs)
# output: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]




# 복잡한 함수와 표현식

from math import pi

pi_list = [str(round(pi, i)) for i in range(1, 6)]

print(pi_list)
# output: ['3.1', '3.14', '3.142', '3.1416', '3.14159']




# 중첩된 리스트 컴프리헨션 (Nested List Comprehension)
# 행렬 전치 (for)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

# 행렬 전치 (리스트 컴프리헨션)

transposed = [[row[i] for row in matrix] for i in range(4)]

# 내장함수(이 경우 zip)를 사용한 행렬 전치 구현

print(list(zip(*matrix)))
# output: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]