
class Algs:
    def bubble_sort(self):
        string = """ 

        # Initial Input: [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]
        # Resulted Ouput: [147, 151, 380, 387, 439, 542, 585, 743, 820, 860, 865, 924]

        def bubble_sort(my_list):
            for i in range(len(my_list)):
                for idx in range(len(my_list) - i - 1):
                    if my_list[idx] > my_list[idx + 1]:
                        my_list[idx], my_list[idx + 1] = my_list[idx + 1], my_list[idx]

                    print(my_list)
        
        ###
        Time Complexity: O(N^2)
        ###
        """

        return string 
    
    def merge_sort(self):
        string = """ 

        # Initial Input: [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]
        # Resulted Ouput: [147, 151, 380, 387, 439, 542, 585, 743, 820, 860, 865, 924]

        def merge_sort(my_list):
            if len(my_list) <= 1:
                return my_list 
            else:
                middle_index = len(my_list) // 2
                left_split = my_list[:middle_index]
                right_split = my_list[middle_index:]
                left_sorted = merge_sort(left_split)
                right_sorted = merge_sort(right_split)
                return merge(left_sorted, right_sorted)
            

        def merge(left, right):
            result = []
            while (left and right):
                if left[0] < right[0]:
                    result.append(left[0])
                    left.pop(0)
                else:
                    result.append(right[0])
                    right.pop(0)
                
            if left:
                result += left 
            elif right:
                result += right 
            return result 
       ------------------------------------------------
       RECURSIVE METHOD:
       def merge(left, right, result=[]):
            if len(left) == 0 or len(right) == 0:
                if left:
                    result += left 
                elif right:
                    result += right 
                return result
            else:
                if left[0] < right[0]:
                    result.append(left[0])
                    left.pop(0)
                else:
                    result.append(right[0])
                    right.pop(0)
            return merge_recursive(left, right, result)
            
        ### 
        Time complexity: O(N log N)
        ###
        """

        return string
    
    def quicksort(self):
        string = """

        from random import randrange 

        def quicksort(lst, start, end):
            if start >= end:
                return lst 
            else:
                pivot_idx = randrange(start, end)
                pivot_element = lst[pivot_element]
                lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]
                lesser_than_pointer = start 
                
                for i in range(start, end):
                    if lst[i] < pivot_element:
                        lst[i], lst[lesser_than_pointer] = lst[lesser_than_pointer], lst[i]

                        lesser_than_pointer += 1 

                lst[end], lst[lesser_than_pointer] = lst[lesser_than_pointer], lst[end]
                quicksort(lst, start, lesser_than_pointer - 1)
                quicksort(lst, lesser_than_pointer + 1, end)
        
        ### 
        Time Complexity: O(N log N)
        ### 
        """
        return string

    def radix_sort(self):
        string = """

        def radix_sort(lst):
            maximum_value = max(lst)
            max_exponent = len(str(maximum_value))
            being_sorted = lst[:]
            
            for exponent in range(max_exponent):
                position = exponent + 1
                index = -position 
                digits = [ [] for i in range(10)]

                for number in being_sorted:
                    string_number = str(number)
                    try:
                        digit = string_number[index]
                    except IndexError:
                        digit = 0 
                    digit = int(digit)
                    digits[digit].append(number)
                    being_sorted = []
                    for numeral in digits:
                        being_sorted.extend(numeral)

            return being_sorted

            ###
            Time Complexity: O(N)
            ###
            """
        return string

    def linear_search(self):
        string = """

        def linear_search(lst, target_value):
            matches = []
            for i in range(len(lst)):
                if lst[i] == target_value:
                    matches.append(target_value)
            if len(matches) > 0:
                return matches 
            else:
                raise ValueError("{o} is not present in the array".format(o=target_value))


        ###
        Average Time Complexity: O(N) / 2 == O(N)
        Best Case: O(1)
        Worst Case: O(N)
        """

        return string


    def naive_pattern_search(self):
        string = """

        def naive_pattern_search(text, pattern):
            print("Input Text: {}".format(text))
            print("Input Pattern: {}".format(pattern))

            for index in range(len(text)):
                print("Text Index: {}".format(index))

                match_count = 0 

                for char in range(len(pattern)):
                    print("Pattern Index: {}".format(char))

                    if pattern[char] == text[char + index]:
                        print("Match found!" )
                        print("Match count at {}".format(match_count))
                        match_count += 1
                    else:
                        break 
                
                if match_count == len(pattern):
                    print("The pattern has been found at index {}".format(index))
            

            ###
            Average Time Complexity: O(nk) 
            Worse Time Complexity: O(n^2)
            ###
        """

        return string 

    def bfs(self):
        string = """
        
        bfs.py
        ---------------
        from collections import deque
        def bfs(root_node, goal_value):
            path_queue = deque()
            initial_path = [root_node]
            path_queue.appendleft(initial_path)

            while path_queue:
                current_path = path_queue.pop()
                current_node = current_path[-1]
                priint("Searching node with value: {}".format(current_node.value)
                if current_node.value == goal_value:
                    return current_path 
                
                for child in current_node.children:
                    new_path = current_path[:]
                    new_path.append(child)
                    path_queue.appendleft(new_path)
        
        return None 

        ----------------
        script.py
        ----------------
        from tree import TreeNode       # The Tree data structure is the same as the one listed in the software. 
        from bfs import bfs 

        goal_path = bfs(root_node, sample_goal_value)
        if goal_path == None:
            print("No path has been found")
        else:
            print("Path found" )
            for node in goal_path:
                print(node.value)

        ###
        TIME COMPLEXITY: O(N)
        SPACE COMPLEXITY: O(N) + O(1)
        ###
        
        """
    
        return string 
    
    def dfs(self):
        string = """

        from tree import TreeNode # The Tree data structure is the same as the one listed in the software. 

        def dfs(root_node, goal_value, path=()):
            path = path + (root_node,)

            if root_node.value == goal_value:
                return path 
            for child in root_node.children:
                path_found = dfs(child, goal_value, path)

                if path_found != None:
                    return path_found

            return None

            ###
            TIME COMPLEXITY: O(N)
            SPACE COMPLEXITY: O(1)
            ###
        """
        return string

    def binary_search(self):
        string = """
        
        def binary_search(sorted_list, goal):
            if not sorted_list:
                return 'value not found'
            else:
                mid_idx = len(sorted_list) // 2
                mid_val = sorted_list[mid_idx]
                if mid_val == goal:
                    return mid_idx 
                elif mid_val > goal:
                    left_side = sorted_list[:mid_idx]
                    return binary_search(left_side, goal)
                elif mid_val < goal:
                    right_side = sorted_list[mid_idx + 1:]
                    result = binary_search(right_side, goal)
                    if result == 'value not found':
                        return result 
                    else:
                        return reult + mid_idx + 1
                    
        ### 
        TIME COMPlEXITY: O(N/2)
        SPACE COMPLEXITY: O(1)
        ###
        """
        return string

            



            
initialize = Algs()
