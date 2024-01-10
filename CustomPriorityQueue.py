
class CustomPriorityQueue:
    def __init__(self):
        self.queue = {}
        self.length = 0

    def empty(self):
        return self.length == 0
    
    def put(self):
        pass

    def get(self):
        pass

    def qsize(self):
        return self.length
    
    def print_queue(self):
        print(self.queue)
