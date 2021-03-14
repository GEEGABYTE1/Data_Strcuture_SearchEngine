class Script:
    
    def Node(self):
        string = """ 
        class Node:
            def __init__(self, value, link=None):
                self.value = value 
                self.link = link 

            def get_value(self):
                return self.value 

            def get_link(self):
                return self.link 

            def set_link(self, new_link):
                self.link = new_link 
                 """

        return string


    def LinkedList(self):
        string = """ 
        class LinkedList:
            def __init__(self, value=None):
                self.head_node = Node(value)

            def get_head_node(self):
                return self.head_node

            def insert_node(self, new_value):
                new_node = Node(new_value)
                new_node.set_link(self.head_node)
                self.head_node = new_node 

            def stringify_list(self):
                current_node = self.get_head_node()
                while curret_node:
                    if current_node.get_value() != None:
                        print(current_node.get_value())
                    current_node = current_node.get_link()

            def remove_node(self, value):
                current_node = self.get_head_node()
                if current_node.get_value() == value:
                    self.head_node = current_node.get_link()
                else:
                    while current_node:
                        next_node = current_node.get_link()
                        if next_node.get_value() == value:
                            current_node.set_link(next_node.get_link())
                            current_node = None 
                        else:
                            current_node = next_node 
                """
        return string
    
    def Stack(self):
        string = """
        class Stack:
            def __init__(self, top_item=None):
                self.top_item = top_item 
                self.size = 0
                self.limit = 1000 

            def is_empty(self):
                if self.size == 0:
                    return True 

            def has_space(self):
                if self.limit > self.size:
                    return True 

            def peek(self):
                if not self.is_empty():
                    return self.top_item.get_value()
                else:
                    print(\"The Stack is Empty\")

            def push(self, new_value):
                if self.has_space():
                    new_node = Node(new_value)
                    new_node.set_link(self.top_item)
                    self.top_item = new_node 
                    self.size += 1
                else:
                    print(\"The Stack is Full\")

            def pop(self):
                if not self.is_empty():
                    item_to_remove = self.top_item
                    self.top_item = item_to_remove.get_link()
                    self.size -= 1
                    return item_to_remove.get_value()
                else:
                    print(\"The Stack is Empty\")
                """
        return string

    def Queue(self):
        string = """
        class Queue:
            def __init__(self, limit=None):
                self.limit = limit 
                self.size = 0
                self.head_node = None 
                self.tail_node = None 

            def is_empty(self):
                if self.size == 0:
                    return True 

            def has_space(self):
                if self.limit == None:
                    return True 
                else:
                    if self.limit > self.size:
                        return True 

            def peek(self):
                if not self.is_empty():
                    return self.head_node.get_value()
                else:
                    print(\"The Queue Is Empty\")
            
            def enqueue(self, new_value):
                if self.has_space():
                    new_node = new_value
                    if self.size == 0:
                        self.head_node = new_node 
                        self.tail_node = new_node 
                    else:
                        self.tail_node.set_link(new_node)
                        self.tail_node = new_node 
                    self.size += 1
                else:
                    print(\"The Queue Is Full\")

            def dequeue(self):
                if not self.is_empty():
                    item_to_remove = self.head_node
                    if self.size == 1:
                        self.head_node = None 
                        self.tail_node = None 
                    else:
                        self.head_node = item_to_remove.get_link()
                    self.size -= 1
                    return item_to_remove.get_value()
                else:
                    print(\"The Queue Is Empty\")
            """
        return string

    def TreeNode(self):
        string = """
        class TreeNode:
            def __init__(self, value):
                self.value = value 
                self.children = []

            def add_child(self, child_node):
                self.children.append(child_node)

            def remove_child(self, child_node):
                self.children = [i for i in self.children if i != child_node]

            def traverse(self):
                level = 0
                node = self
                number = input("Please enter a number: ")

                while len(node.children) > 0:
                    level += 1
                    try:
                        if int(number) <= node.value:

                            if int(number) == node.children[0].value:
                                print(level)
                                print(node.children[0].value)
                                break
                            else:
                                print(level)
                                print(node.children[0].value)
                                node.value = node.children[0].value
                                node.children = node.children[0].children 
                        
                        elif int(number) >= node.value:

                            if int(number) == node.children[-1].value:
                                print(level)
                                print(node.children[-1].value)
                                break
                            else:
                                print(level)
                                print(node.children[-1].value)
                                node.value = node.children[-1].value
                                node.children = node.children[-1].children 
                    except IndexError:
                        return "This value is not valid"
                
                *********************************************************************
                The .traverse() function changes if you want to only interate a tree 

                def traverse(self):
                    node = [self]
                    while len(node) > 0:
                        current_node = node.pop()
                        print(current_node.value)
                        node += current_node.children
                        
                        """
        return string
    
    def HashMap(self):
        string = """
        *** Needs LinkedList class ***
        *** View LinkedList to see functions if needed ***

        class HashMap:
            def __init__(self, array_size):
                self.array_size = array_size
                self.array = [LinkedList() for i in range(self.array_size)]

            def hash(self, key, collisions=0):
                key_bytes = str(key).encode()
                hash_code = sum(key_bytes)
                return hash_code + collisions 

            def compressor(self, hash_code):
                return hash_code % self.array_size 

            def setter(self, key, value):
                array_index = self.compressor(self.hash(key))
                current_array_value = self.array[array_index]
                current_ll_value = current_array_value.get_head_node()

                if current_ll_value.get_value() == None:
                    self.array[array_index] = LinkedList([key, value])
                    return 

                if current_ll_value.get_value()[0] == key:
                    current_array_value.insert_node([key, value])
                    return 

                number_collisions = 1
                while current_ll_value.get_value()[0] != key:
                    new_hash_code = self.hash(key, number_collisions)
                    new_array_index = self.compressor(new_hash_code)
                    new_array_value = self.array[new_array_index]
                    new_ll_value = new_array_value.get_head_node()

                    if new_ll_value.get_value() == None:
                        self.array[new_array_index] = LinkedList([key, value])
                        return 

                    if new_ll_value.get_value()[0] == key:
                        new_array_value.insert_node([key, value])
                        return 
                    
                    number_collisions += 1
                    return 
            
            def retrieve(self, key):
                array_index = self.compressor(self.hash(key))
                current_array_value = self.array[array_index]
                current_ll_value = current_array_value.get_head_node()

                if current_ll_value.get_value() == None:
                    return None 

                if current_ll_value.get_value()[0] == key:
                    current_node = current_ll_value
                    while current_node:
                        if current_node.get_value() != None:
                            print(current_node.get_value())
                        current_node = current_node.get_link()

                retrieve_collisions = 1
                while current_ll_value.get_value()[0] != key:
                    new_hash_code = self.hash(key, retrieve_collisions)
                    new_array_index = self.compressor(new_hash_code)
                    new_array_value = self.array[new_array_index]
                    new_ll_value = new_array_value.get_head_node()

                    if new_ll_value.get_value() == None:
                        return None 

                    if new_ll_value.get_value()[0] == key:
                        current_node = new_ll_value
                        while current_node:
                            if current_node.get_value() != None:
                                print(current_node.get_value())
                            current_node = current_node.get_link()
                    
                    retrieve_collisions += 1
                    return
            
            def delete(self, key):
                array_index = self.compressor(self.hash(key))
                current_array_value = self.array[array_index]
                current_ll_value = current_array_value.get_head_node()

                if current_ll_value.get_value() == None:
                    pass

                if current_ll_value.get_value()[0] == key:
                    self.array[array_index] = LinkedList()
                    
                delete_collisions = 1
                while current_ll_value.get_value()[0] != key:
                    new_hash_code = self.hash(key, delete_collisions)
                    new_array_index = self.compressor(new_hash_code)
                    new_array_value = self.array[new_array_index]
                    new_ll_value = new_array_value.get_head_node()

                    if new_ll_value.get_value() == None:
                        pass

                    if new_ll_value.get_value()[0] == key:
                        self.array[new_array_index] = LinkedList()
                    
                    retrieve_collisions += 1
                    return 
                    """
        return string




test = Script()

#print(test.TreeNode())


