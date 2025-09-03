## 리스트로 스택과 큐 사용하기

### 리스트를 스택으로 사용하기

기초적인 자료구조 스택(Stack)과 큐(Queue)를 파이썬의 리스트를 사용하면 어떻게 구현할 수 있는지 알아봅시다. 스택은 스택의 끝에서 요소의 `push`와 `pop`이 일어나는 LIFO(Last-In, First-Out) 구조를 하고 있습니다.

파이썬의 리스트 메서드들은 리스트를 스택으로 사용하기 쉽게 만드는데, 다음 두 메서드를 사용하여 리스트를 스택으로 사용할 수 있습니다.

`append()`: 스택의 `top`에 새로운 요소를 넣기 위해 사용합니다. (`push`연산)

`pop()`: 스택의 `top`에 있는 요소를 꺼낼 때 사용합니다. (`pop`연산)

아래는 리스트를 스택으로 사용하는 예시입니다.
```python
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
# output: [3, 4, 5, 6, 7]

stack.pop()
# output: 7

stack.pop()
# output: 6

stack.pop()
# output: 5

print(stack)
# output: [3, 4]
```

### 리스트를 큐로 사용하기

리스트를 큐로 사용하는 것도 가능한데, 큐는 처음으로 넣어진 요소가 처음으로 꺼내지는 FIFO(First-In, First-Out) 구조를 하고 있습니다.

사실 리스트는 큐로 사용하기에는 적합하지 않습니다. 리스트의 끝에서 요소를 덧붙이거나 꺼내는 것은 빠르지만, 리스트의 머리에서 요소를 덧붙이거나 꺼내려면 다른 요소들도 이동시켜야 하기 때문에 속도가 느립니다.

큐를 구현하려면 양 끝에서 덧붙이기와 꺼내기가 모두 빠르게 설계된 `collections.deque`를 사용하면 됩니다.

`collections.deque`의 두 메서드는 큐의 `push`와 `pop`을 수행합니다.

`append()`: 큐의 `rear`에 새로운 요소를 추가할 때 사용합니다. (`push` 연산)

`popleft()`: 큐의 `front`에 있는 요소를 꺼낼 때 사용합니다. (`pop` 연산)


아래는 `collections.deque`를 사용하여 구현한 큐입니다.

```python
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue.popleft())
# output: 'Eric'

print(queue.popleft())
# output: 'John'

print(queue)
# output: deque(['Michael', 'Terry', 'Graham'])
```
