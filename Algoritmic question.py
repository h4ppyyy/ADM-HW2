from collections import deque

# Read the number of instructions

correct_num = False
while correct_num != True:
    try:
        print("Print number of instructions: ")
        num_instructions = int(input())
        correct_num = True
    except:
        continue


# Initialize a deque to represent the bookshelf
shelf = deque()

# Process each instruction
for _ in range(num_instructions):
    instructions = input().split()
    try:
        instr, book_id = instructions[0], int(instructions[1])
    except Exception as ex:
        print(ex)
        continue
    
    if instr == 'L':
        # Place the book to the left of the leftmost existing book
        shelf.appendleft(book_id)
    elif instr == 'R':
        # Place the book to the right of the rightmost existing book
        shelf.append(book_id)
    elif instr == '?':
        # Calculate the minimum number of books to pop from both sides
        try:
            left_count = shelf.index(book_id)
        except Exception as ex:
            print(ex)
            continue

        right_count = len(shelf) - left_count - 1
        # Print the result
        print(min(left_count, right_count))

### 2. Ask ChatGPT or any other LLM chatbot tool to check your code's time complexity (the Big O notation). 
# Do you believe this is correct? How can you double-check it? 
# Elaborate about your answer.

# ChatGPT answer:
# Reading the nu,ber of instructions:
#The time complexity of this part is O(1) because it involves only input/output operations and basic arithmetic.

#Initializing a deque:
#The time complexity of initializing a deque is O(1).

#Processing each instruction in the loop:
#Each instruction involves either appending to the left or appending to the right of the deque, which takes O(1) time.

#The "?" action involves searching for the index of a book in the deque using 'bookshelf.infex(book_id)'.
#In the worst case, this operation takes O(n), where n is the number of books in the deque.

#Printing the result:
#The time complexity of printing is O(1)

#Since the main loop iterates through all the instuctions and each instruction takes O(1) time except for the "?" action, the overall time complexity is dominated by the search operation in the worst case.
#Therefore, the overall time complexity of the algorith is O(n^2), where n is the number of instructions or the number of books in the deque.

# I disagree with the ChatGPT, because overall time complexity is determined by the maximum cost per insturction.
# Which means that time complexity of the algorithm is O(n), where n is the number of book in deque.

### 3. Yes the proposed algorithm is optimal one, i cannot sugest a better algorithm.