class PriorityQueue(object):
    """
    A priority queue implemented by min_heap data structure.
    """
    def __init__(self):
        """
        initialization with empty list
        """
        self.cmd_queue = []
    
    def get_size(self):
        """
        return cmd_queue size
        """
        return len(self.cmd_queue)

    def min_heapify(self, index):
        """
        heapify the list by comparing the priority at index node with its left and right node
        and swap if needed to make sure the root node has the minimum priority value.
        """
        size = self.get_size()
        minimum = index
        left_index = 2*index+1
        right_index = 2*index+2
        if left_index < size and left_index >= 0:
            if self.cmd_queue[left_index]['priority'] < self.cmd_queue[minimum]['priority']:
                minimum = left_index
        if right_index < size and right_index >= 0:
            if self.cmd_queue[right_index]['priority'] < self.cmd_queue[minimum]['priority']:
                minimum = right_index
        if minimum != index:
            self.cmd_queue[index], self.cmd_queue[minimum] = self.cmd_queue[minimum], self.cmd_queue[index]
            self.min_heapify(minimum)

    def insert(self, cmd):
        """
        simply insert the node if the list is empty, or heapify after insert it. The insertion
        format is a dictionary which contains two keys: 'command' and 'priority'.
        """
        size = self.get_size()
        if size == 0:
            self.cmd_queue.append(cmd)
        else:
            self.cmd_queue.append(cmd)
            size += 1
            for i in range((size//2)-1, -1 , -1):
                self.min_heapify(i)

    def popTopPriority(self):
        """
        pop the root(first) node which is the minimum(highest priority), and print it out,
        and heapify after remove the root node.
        """
        size = self.get_size()
        topPriority_cmd = self.cmd_queue[0]['command']
        print topPriority_cmd # according to what the command is for, we can execute it instead of printing 
        self.cmd_queue[0] = self.cmd_queue[size-1]
        self.cmd_queue.pop(size-1)
        self.min_heapify(0)

### Uncomment the following to run a simple test ###
# cmdQueue = PriorityQueue()
# cmdQueue.insert({'command':'c1', 'priority':10})
# cmdQueue.insert({'command':'c2', 'priority':2})
# cmdQueue.insert({'command':'c3', 'priority':5})
# cmdQueue.insert({'command':'c4', 'priority':0})
# cmdQueue.insert({'command':'c5', 'priority':1})
# cmdQueue.insert({'command':'c6', 'priority':4})
# cmdQueue.insert({'command':'c7', 'priority':2})
# cmdQueue.insert({'command':'c8', 'priority':0})
# for i in xrange(cmdQueue.get_size()):
#     cmdQueue.popTopPriority()