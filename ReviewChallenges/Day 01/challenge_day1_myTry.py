'''
🚀 Let's Start: Day 1 - Simple Problem
🧠 Problem: Unique Characters in a String
Description:
Write a function has_unique_characters(s) that returns True if all characters in the string s are unique, and False otherwise.

Examples:
has_unique_characters("abcdef") ➞ True  
has_unique_characters("aabbcc") ➞ False  
has_unique_characters("") ➞ True  

Constraints:
No use of external libraries.
Try to avoid brute force (nested loops).
'''

# Chat GPT proposal: 'set()' function removes the duplicates, then you can compare the length - If it is the same, then you have only unique charact.
'''
def has_unique_characters(s):
    return len(set(s)) == len(s)
'''

def has_unique_characters(s):
    char_list = list(s)
    char_list.sort()            # ['a', 'b', 'c', 'd', 'e', 'f']
    backup = list()

    for i in range(len(char_list)):
        if char_list[i] in backup:
            return False
        else:
            backup.append(char_list[i])
    return True

def main():
    s = 'abcdef'
    print(has_unique_characters(s))

if __name__ == '__main__':
    main()