## 리스트 컴프리헨션(List Comprehension)

리스트 컴프리헨션은 리스트를 만드는 간결한 방법을 제공합니다. 흔한 용도는, 각 요소가 다른 시퀀스나 이터러블의 멤버들에 어떤 연산을 적용한 결과인 리스트를 만들거나, 어떤 조건을 만족하는 요소들로 구성된 서브 시퀀스를 만드는 것입니다.

예를 들면 제곱수의 리스트를 만들고자 할 때 아래와 같이 만들 수 있습니다.
```python
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
# output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(x)
# output: 9
```

이는 x라는 이름의 변수를 만들고 (또는 덮어쓰고) 루프가 종료된 후에도 남아있게 된다는 것을 유의해야 합니다.

아래의 방법을 사용한다면 어떠한 부작용 없이 리스트를 만들어낼 수 있습니다.

```python
squares = list(map(lambda x: x**2, range(10)))
```

또는 이렇게 할 수 있습니다.

```python
squares = [x**2 for x in range(10)]
```

리스트 컴프리헨션은 괄호 안에 표현식을 포함하고, 그 뒤에 for 절이 오며, 그 다음에 0개 이상의 for 또는 if 절이 오는 구조로 이루어집니다. 결과는 뒤따르는 for 및 if 절의 맥락에서 표현식을 평가하여 생성된 새로운 리스트가 됩니다.

아래 예시는 두 리스트의 요소가 서로 같지 않을 경우 해당 요소를 결합합니다.

```python
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```

그리고 이는 아래와 같습니다.

```python
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

print(combs)
# output: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

두 코드에서 for와 if의 순서가 같다는 것을 볼 수 있습니다.

리스트 컴프리헨션은 복잡한 표현식과 중첩된 함수들을 포함할 수 있습니다.

```python
from math import pi

pi_list = [str(round(pi, i)) for i in range(1, 6)]

print(pi_list)
# output: ['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### 중첩된 리스트 컴프리헨션 (Nested List Comprehension)

리스트 컴프리헨션의 첫 표현식으로 임의의 표현식이 올 수 있는데, 다른 리스트 컴프리헨션도 가능합니다.

아래는 길이가 4인 리스트 3개의 리스트로 구현된 3x4 행렬입니다.

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
```

다음 리스트 컴프리헨션은 행과 열을 전치 시킵니다.

```python
[[row[i] for row in matrix] for i in range(4)]
```

내부 리스트 컴프리헨션은 뒤따르는 for의 문맥에서 값이 구해집니다. 그래서 이 예시는 아래와 같습니다.

```python
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
# output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

내부 리스트 컴프리헨션을 전개하면 아래와 같습니다.

```python
transposed = []
for i in range(4):
    # 다음 3줄은 중첩된 리스트 컴프리헨션을 구현합니다
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
# output: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

실제 문제상황에서는 내장함수를 선호해야 합니다. 이 경우에는 zip() 함수가 제 역할을 할 수 있습니다.

```python
print(list(zip(*matrix)))
# output: [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```