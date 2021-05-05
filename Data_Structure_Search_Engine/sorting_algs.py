
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

initialize = Algs()
