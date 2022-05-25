from collections import deque

que = deque(maxlen=5)
que.append(1)
que.append(2)
que.append(3)
que.append(4)
que.append(5)
# note - element is overriddden when maxlen reached 
que.append(6)
print(que)
print(que.popleft())
print(que)
que.clear()
print(que)