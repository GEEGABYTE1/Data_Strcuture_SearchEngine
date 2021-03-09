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



test = Script()

#print(test.Stack())


