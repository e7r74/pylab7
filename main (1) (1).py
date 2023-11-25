print("TASK 1")
def read_file_line_by_line(file_path: str) -> None:
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())
            
read_file_line_by_line('text1.txt')
# print("TASK 2")
# import random

# def read_random_line(file_path: str) -> str:
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         return random.choice(lines)
# random_line = read_random_line('text1.txt')
# print(random_line)
# print("task3")
# def count_uppercase_characters(file_path: str) -> int:
#     count = 0
#     with open(file_path, 'r') as file:
#         for line in file:
#             for character in line:
#                 if character.isupper():
#                     count += 1
#     return count
# count = count_uppercase_characters('text1.txt')
# print(count)
# print("task 4")
# def count_lines_not_starting_with_D(file_path: str) -> int:
#     count = 0
#     with open(file_path, 'r') as file:
#         for line in file:
#             if not line.startswith('D'):
#                 count += 1
#     return count
# count = count_lines_not_starting_with_D('text1.txt')
# print(count)
# print("task 5")
# def count_words_ending_with_f(file_path: str) -> int:
#     count = 0
#     with open(file_path, 'r') as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 if word.endswith('F') or word.endswith('f'):
#                     count += 1
#     return count
# count = count_words_ending_with_f('text1.txt')
# print(count)
# print("task 6")
# def count_all_and_none_words(file_path: str) -> tuple:
#     all_count = 0
#     none_count = 0
#     with open(file_path, 'r') as file:
#         for line in file:
#             words = line.split()
#             all_count += words.count('all') + words.count('All')
#             none_count += words.count('none') + words.count('None')
#     return all_count, none_count
# all_count, none_count = count_all_and_none_words('text1.txt')
# print(all_count, none_count)
# print("task 7")
# import string

# def count_word_frequency(file_path):
#     try:
#         with open(file_path, 'r') as file:
        
#             content = file.read()

#             content = content.translate(str.maketrans("", "", string.punctuation))
#             content = content.lower()

#             words = content.split()

#             word_frequency = {}

#             for word in words:
#                 if word in word_frequency:
#                     word_frequency[word] += 1
#                 else:
#                     word_frequency[word] = 1

#             return word_frequency

#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#         return None
#     except Exception as e:
#         print(f"Error: {e}")
#         return None


# file_path = 'text1.txt' 
# word_frequency = count_word_frequency(file_path)

# if word_frequency is not None:
#     print(file_path)
#     for word, frequency in word_frequency.items():
#         print(f"{word}: {frequency}")
# print("task8")
# def find_longest_word(file_path):
#     try:
#         with open(file_path, 'r') as file:
         
#             content = file.read()

#             words = [word.strip(".,!?()[]{}\"'") for word in content.split()]
#             longest_word = max(words, key=len)

#             return longest_word

#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#         return None
#     except Exception as e:
#         print(f"Error: {e}")
#         return None
# file_path = 'text1.txt' 
# longest_word = find_longest_word(file_path)

# if longest_word is not None:
#     print(file_path+" "+ longest_word)
# print("task9")
# def display_corrected_content(file_path):
#     try:
#         with open(file_path, 'r') as file:
      
#             content = file.read()

#             corrected_content = content.replace('B', 'J')

      
#             print(corrected_content)

#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"Error: {e}")
# file_path = 'text1.txt'  
# display_corrected_content(file_path)
# print("task10")
# def count_occurrences_A_B(file_path):
#     try:
#         with open(file_path, 'r') as file:
        
#             content = file.read()

           
#             count_A = 0
#             count_B = 0

#             for char in content:
        
#                 if char == 'A' or char == 'a':
#                     count_A += 1
#                 elif char == 'B' or char == 'b':
#                     count_B += 1

#             print(f" 'A' and 'a': {count_A}")
#             print(f" 'B' and 'b': {count_B}")

#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"Error: {e}")

# file_path = 'text1.txt'  
# count_occurrences_A_B(file_path)
