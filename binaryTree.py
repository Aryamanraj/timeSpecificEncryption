import random
from collections import deque
import pickle

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
      def __init__(self):
        self.root = None

      def hashing(self,val,val2):
            val3 = int(val)*int(val2)
            val4 = str(val3)
            return hash(val4)%(10**8)

########
      def insert_bottom_up(self, numbers):
        if not numbers:
            return
        nodes = []
        for i in range(len(numbers)):
            nodes.append(Node(numbers[i]))
        for i in range(len(nodes)//2-1, -1, -1):
            if i*2+1 < len(nodes):
                nodes[i].left = nodes[i*2+1]
            if i*2+2 < len(nodes):
                nodes[i].right = nodes[i*2+2]
        self.root = nodes[0]
###############

      def print_tree(self):
        if not self.root:
            return

        queue = deque()
        queue.append(self.root)
        while queue:
            count = len(queue)
            level = []
            for i in range(count):
                curr = queue.popleft()
                level.append(curr.data)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            print(' '.join(map(str, level)))

      def search(self, num):
        curr = self.root
        num = str(num)  
        for i in range(len(num)):
            if num[i]=='0':
                curr = curr.left
            elif num[i]=='1':
                curr = curr.right
            if curr is None:
                return None
        return curr.data


      def generator(self):
            arr = []
            vector = []
            n = int(input("Enter no. between 1 to 23: "))+1
            n=1<<n
            for i in range(0,n):
                  vector.append(random.randint(1, 1000))
            vector2 = vector
            
            while(len(vector2)>1):
                  newArr = []
                  for j in range(0,len(vector2),2):
                        newArr.append(self.hashing(vector2[j],vector2[j+1]))
                  arr = arr+list(reversed(newArr))
                  vector2 = newArr
            return list(reversed(arr))
      def save_tree(self,file_name):
            with open(file_name, 'wb') as f:
                  pickle.dump(self, f)


