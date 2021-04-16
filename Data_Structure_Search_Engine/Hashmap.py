from script import test



class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(self.array_size)]

    def hash(self, key, collisions=0):
        key_bytes = str(key).encode()
        hash_code = sum(key_bytes)
        return hash_code + collisions 

    def compressor(self, hash_code):
        return hash_code % self.array_size 

    def setter(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            self.array[array_index] = [key, value]
            return 

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return 

        number_collisions = 1
        while current_array_value[0] != key:
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]

            if new_array_value == None:
                self.array[new_array_index] = [key, value]
                return 

            if new_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return 

            number_collisions += 1
            return 

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value == None:
            return None
        
        if current_array_value[0] == key:
            return current_array_value[1]

        retrieve_collisions = 1
        while current_array_value[0] != key:
            new_hash_code = self.hash(key, retrieve_collisions)
            new_array_index = self.compressor(new_hash_code)
            new_array_value = self.array[new_array_index]

            if new_array_value == None:
                return None 

            if new_array_value[0] == key:
                return new_array_value[1]
            
            retrieve_collisions += 1
            return 



test1 = HashMap(13)
test1.setter("Node", test.Node())
test1.setter("LinkedList", test.LinkedList())
test1.setter("Stack", test.Stack())
test1.setter("Queue", test.Queue())
test1.setter("Binary Search Tree", test.TreeNode())
test1.setter("Hash Map", test.HashMap())
test1.setter("MaxHeap", test.MaxHeap())
test1.setter("MinHeap", test.MinHeap())
test1.setter("Complex_Graph", test.graph())
#print(test1.array)

class Prompt:

    def __init__(self, prompt=None):
        self.prompt = prompt
        lst = ["LinkedList", "Stack", "Queue", "Node", "Binary Search Tree", "Hash Map", "MaxHeap", "MinHeap", "Graph"]
        print("Please note that all data structures are written in Python3")
        #print(lst)
        print("-------------------------------------")
        for i in lst:
            print(i + "\t")
        print("-------------------------------------")
        print("Please type in a Linear Data Structure you would want to see: ")
        playing = True
        while playing:
            
            self.prompt = input()

            if self.prompt == "Node " or self.prompt == "Node":
                print(test1.retrieve("Node"))

            elif self.prompt == "Linked List" or self.prompt == "Linked List " or self.prompt == "LinkedList":
                print(test1.retrieve("LinkedList"))

            elif self.prompt == "Stack" or self.prompt == "Stack ":
                print(test1.retrieve("Stack"))

            elif self.prompt == "Queue" or self.prompt == "Queue ":
                print(test1.retrieve("Queue"))

            elif self.prompt == "Binary Search Tree" or self.prompt == "Tree":
                print(test1.retrieve("Binary Search Tree"))

            elif self.prompt == "Hash Map" or self.prompt == "HashMap":
                print(test1.retrieve("Hash Map"))
            
            elif self.prompt == "MaxHeap" or self.prompt == "MaxHeap ":
                print(test1.retrieve("MaxHeap"))
            
            elif self.prompt == "MinHeap" or self.prompt == "MinHeap ":
                print(test1.retrieve("MinHeap"))
            
            elif self.prompt == "Graph" or self.prompt == "Graph ":
                print(test1.retrieve('Complex_Graph'))

            elif self.prompt == "/quit" or self.prompt == "\quit ":
                break

            else:
                print("That data structure seems to be invalid")

player = Prompt()
#print(player)



        
