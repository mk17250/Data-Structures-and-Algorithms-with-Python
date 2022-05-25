# Queue using python Queue module 

import queue as q

que = q.Queue(maxsize=5)
print(que.qsize())
que.put(1)
que.put(2)
que.put(3)
que.put(4)
print(que.get())
print(que.empty())
print(que.get())
print(que.qsize())

# How do we print out the Queue?