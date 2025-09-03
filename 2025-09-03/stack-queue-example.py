# Stack Example

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


# Queue Example

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