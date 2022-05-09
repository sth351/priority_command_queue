# priority_command_queue
Implemented a priority queue with min heap to pop out highest priority command that needs to be executed.

# Insert
insert type is a dictionary with two keys: command and priority where the priority is a value from 0 to 10 and we assume that 0 is the top priority.
for example: `{'command':'cmd1', 'priority':5}`

# Usage Example
```
cmdQueue = PriorityQueue()
cmdQueue.insert({'command':'c1', 'priority':10})
cmdQueue.insert({'command':'c2', 'priority':2})
cmdQueue.insert({'command':'c3', 'priority':5})
cmdQueue.insert({'command':'c4', 'priority':0})
cmdQueue.insert({'command':'c5', 'priority':1})
cmdQueue.insert({'command':'c6', 'priority':4})
cmdQueue.insert({'command':'c7', 'priority':2})
cmdQueue.insert({'command':'c8', 'priority':0})
for i in xrange(cmdQueue.get_size()):
    cmdQueue.popTopPriority()
```

# Time Complexity
O(log(n)) time complexity to insert and pop top priority element
