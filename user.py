
class Init:
    def __init__(self):
        prompting = True 
        print("Welcome to the CS-102 Search Engine! ")
        print("You can search up: ")
        print("-------------------------------------")
        print("1) Advanced and Linear Data Structures ")
        print("2) Sorting Algorithms ")
        while prompting:
            prompt2 = input("Please type in a corresponding number that you would like to access: ")

            if prompt2 == '1':
                from Hashmap import player 
            elif prompt2 == '2':
                from sorting_hash import player1 
            elif prompt2 == '/quit':
                break 
            else:
                print("HMMmm, seems like that option is not available! ")
            



test3 = Init()
print(test3)