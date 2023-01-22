import pickle
from timeFromFirstDay import timeFromFirstDay
from findCommonSubstring import find_common_substring
from binaryTree import BinaryTree, Node
def load_tree(file_name):
      with open(file_name, 'rb') as f:
            return pickle.load(f)