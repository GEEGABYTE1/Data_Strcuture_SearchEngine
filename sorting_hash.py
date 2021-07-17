from sorting_algs import initialize 

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
        retrieve_collisions += 1
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

test2 = HashMap(22)
test2.setter("Bubble Sort", initialize.bubble_sort())
test2.setter("Merge Sort", initialize.merge_sort())
test2.setter('Quicksort', initialize.quicksort())
test2.setter('Radix_Sort', initialize.radix_sort())
test2.setter('Linear*Search', initialize.linear_search())
test2.setter("Naive_Pattern_Search", initialize.naive_pattern_search())
test2.setter("Bfs", initialize.bfs())
test2.setter("DFS_", initialize.dfs())
test2.setter("Bin_Search", initialize.binary_search())
test2.setter("heapsort", initialize.heapsort())


class Menu:
    def __init__(self, prompt=None):
        self.prompt = prompt 
        lst = ["Bubble Sort", "Merge Sort", 'Quicksort', 'Radix Sort', 'Linear Search', 'Naive Pattern Search', 'Breadth-First Search', 'Depth-First Search', 'Binary Search', 'Heapsort']
        print("Please note that all sort algorithms are written in Python3")
        print("-------------------------------------")
        for i in lst:
            print(i + "\t")
        print("-------------------------------------")
        print("Please type in an Algorithm you would want to see")
        playing = True
        while playing:
            print("\n")
            self.prompt = input(':')
            if self.prompt == "Bubble Sort" or self.prompt == "Bubble sort":
                print(test2.retrieve("Bubble Sort"))
            
            elif self.prompt == "Merge Sort" or self.prompt == "Merge sort":
                print(test2.retrieve("Merge Sort"))
            
            elif self.prompt == "QuickSort" or self.prompt == "Quicksort":
                print(test2.retrieve('Quicksort'))
            
            elif self.prompt == "Radix Sort" or self.prompt == "RadixSort":
                print(test2.retrieve('Radix_Sort'))
            
            elif self.prompt == "Linear Search" or self.prompt == "linear search":
                print(test2.retrieve('Linear*Search'))

            elif self.prompt == "Naive Pattern Search" or self.prompt == "Naive Pattern Search ":
                print(test2.retrieve("Naive_Pattern_Search"))

            elif self.prompt == "Breadth-First Search" or self.prompt == "Breadth-First Search":
                print(test2.retrieve("Bfs"))
            
            elif self.prompt == "Depth-First Search" or self.prompt == "Depth-First Search ":
                print(test2.retrieve("DFS_"))
            
            elif self.prompt == "Binary Search" or self.prompt == "Binary Search":
                print(test2.retrieve("Bin_Search"))
            
            elif self.prompt == "Heapsort" or self.prompt == "heapsort":
                print(test2.retrieve("heapsort"))
            
            elif self.prompt == "/quit":
                break 
            else:
                print("That algorithm does seem to be registered in this software")
                print("Please type one of the algorithms that are listed above")

player1 = Menu()
#print(player1)
