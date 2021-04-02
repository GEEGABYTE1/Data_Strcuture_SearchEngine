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
                    new_node = Node(new_value)
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
    
    def MinHeap(self):
        string = """

        class MinHeap:
            def __init__(self):
                self.heap_list = [None]
                self.count = 0

            def add(self, element):
                self.count += 1
                self.heap_list.append(element)
                self.heapify_up()
            
            def parent_idx(self, idx):
                return idx // 2

            def left_child_idx(self, idx):
                return idx * 2

            def right_child_idx(self, idx):
                return (idx * 2) + 1

            def heapify_up(self):
                idx = self.count 
                while self.parent_idx(idx) > 0:
                    child = self.heap_list[idx]
                    parent = self.heap_list[self.parent_idx(idx)]

                    if parent > child:
                        print("Swapping {parent} with {child} ".format(parent=parent, child=child))
                        self.heap_list[idx] = parent 
                        self.heap_list[self.parent_idx(idx)] = child 
                    idx = self.parent_idx(idx)
                
                print("Heap Restored {}".format(self.heap_list))

            def retrieve_min(self):
                if self.count == 0:
                    print("The heap is empty! ")
                    return None 
                else:
                    minimum = self.heap_list[1]
                    print("Removing {min} from {heap} ".format(min=minimum, heap=self.heap_list))
                    self.heap_list[1] = self.heap_list[-1]
                    self.count -= 1
                    self.heap_list.pop()
                    self.heapify_down()
                    return minimum 
            
            def get_smaller_child_idx(self, idx):
                if self.right_child_idx(idx) > self.count:
                    print("Only the left child is available")
                    return self.left_child_idx(idx)
                else:
                    left_child = self.heap_list[self.left_child_idx(idx)]
                    right_child = self.heap_list[self.right_child_idx(idx)]

                    if left_child < right_child:
                        print("The left child is smaller than the right child")
                        return self.left_child_idx(idx)
                    else:
                        print("The right child is smaller than the left child")
                        return self.right_child_idx(idx)
            
            def child_present(self, idx):
                if self.left_child_idx(idx) <= self.count:
                    return True 

            def heapify_down(self):
                idx = 1 
                while self.child_present(idx):
                    smaller_child_idx = self.get_smaller_child_idx(idx)
                    child = self.heap_list[smaller_child_idx]
                    parent = self.heap_list[idx]

                    if parent > child:
                        self.heap_list[idx] = child
                        self.heap_list[smaller_child_idx] = parent 
                    
                    idx = smaller_child_idx 
                
                print("Heap Restored {}".format(self.heap_list))
                """
        return string

    def MaxHeap(self):
        string = """

        class MinHeap:
            def __init__(self):
                self.heap_list = [None]
                self.count = 0

            def add(self, element):
                self.count += 1
                self.heap_list.append(element)
                self.heapify_up()
            
            def parent_idx(self, idx):
                return idx // 2

            def left_child_idx(self, idx):
                return idx * 2

            def right_child_idx(self, idx):
                return (idx * 2) + 1

            def heapify_up(self):
                idx = self.count 
                while self.parent_idx(idx) > 0:
                    child = self.heap_list[idx]
                    parent = self.heap_list[self.parent_idx(idx)]

                    if parent < child:
                        print("Swapping {parent} with {child} ".format(parent=parent, child=child))
                        self.heap_list[idx] = parent 
                        self.heap_list[self.parent_idx(idx)] = child 
                    idx = self.parent_idx(idx)
                
                print("Heap Restored {}".format(self.heap_list))

            def retrieve_min(self):
                if self.count == 0:
                    print("The heap is empty! ")
                    return None 
                else:
                    minimum = self.heap_list[1]
                    print("Removing {min} from {heap} ".format(min=minimum, heap=self.heap_list))
                    self.heap_list[1] = self.heap_list[-1]
                    self.count -= 1
                    self.heap_list.pop()
                    self.heapify_down()
                    return minimum 
            
            def get_smaller_child_idx(self, idx):
                if self.right_child_idx(idx) > self.count:
                    print("Only the left child is available")
                    return self.left_child_idx(idx)
                else:
                    left_child = self.heap_list[self.left_child_idx(idx)]
                    right_child = self.heap_list[self.right_child_idx(idx)]

                    if left_child < right_child:
                        print("The left child is smaller than the right child")
                        return self.left_child_idx(idx)
                    else:
                        print("The right child is smaller than the left child")
                        return self.right_child_idx(idx)
            
            def child_present(self, idx):
                if self.left_child_idx(idx) <= self.count:
                    return True 

            def heapify_down(self):
                idx = 1 
                while self.child_present(idx):
                    smaller_child_idx = self.get_smaller_child_idx(idx)
                    child = self.heap_list[smaller_child_idx]
                    parent = self.heap_list[idx]

                    if parent < child:
                        self.heap_list[idx] = child
                        self.heap_list[smaller_child_idx] = parent 
                    
                    idx = smaller_child_idx 
                
                print("Heap Restored {}".format(self.heap_list))
                """
        return string
    
    def graph(self):
        string = """

        ------------------------------------------------------------------------
        This data structure is illustrated into two files vertex.py and graph.py
        ------------------------------------------------------------------------
        vertex.py : 

        Class Vertex:
            def __init__(self, value):
                self.value = value 
                self.edges = {}

            def add_edge(self, vertex, weight=0):
                self.edges[vertex] = weight 

            def get_edges(self):
                return list(self.edges.keys())
        -----------------------------------------------------------------------
        graph.py: 
        
        from vertex import Vertex 

        class Graph:
            def __init__(self, directed=False):
                self.directed = directed 
                self.graph_dict = {}

            def add_vertex(self, vertex):
                print("Adding {}".format(vertex.value))
                self.graph_dict[vertex.value] = vertex 
            
            def add_edge(self, from_vertex, to_vertex, weight=0):
                self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)

                if not self.directed:
                    self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

            def find_path(self, start_vertex, end_vertex):
                start = [start_vertex]
                seen = {}

                while len(start) > 0:
                    current_vertex = start.pop()
                    seen[current_vertex] = True 
                    print(current_vertex)

                    if current_vertex == end_vertex:
                        return True 
                    else:
                        vertex = self.graph_dict[current_vertex]
                        next_vertices = vertex.get_edges()
                        next_vertices = [i for i in next_vertices if i not in seen]

                        start.extend(next_vertices)
                
                return False 

                            """ 
        return string 

        




test = Script()

#print(test.TreeNode())


