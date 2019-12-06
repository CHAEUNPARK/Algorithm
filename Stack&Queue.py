def solution(height):
    answer = []
    return answer

# stack
stack = [3, 4, 5]

stack.append(6)
stack.append(7)

stack.pop() #7
print(stack) # [3, 4, 5, 6]
stack.pop() #6
print(stack) # [3, 4, 5]

"""
list를 큐로 사용하는 것도 가능한데, 처음으로 넣은 요소가 처음으로 꺼내지는 요소이다. 하지만, 리스트는
이 목적에는 효율적이지 않습니다. 리스트의 끝에 덧붙이거나, 끝에서 꺼내는 것은 빠르지만, 리스트의 머리에
덧붙이거나 머리에서 꺼내는 것은 느리다.
큐를 구현하려면, 양끝에서의 덧붙이깅와 꺼내기가 모두 빠르도록 설계된 collections.deque를 사용해시오
"""

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft() #Eric
queue.popleft() #John