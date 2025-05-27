'''
🚀 Day 3 - Problem: "Valid Palindrome"
🧠 Description:
    Write a function is_valid_palindrome(s) that checks whether a given string is a valid palindrome, ignoring non-alphanumeric characters and case.

    A palindrome reads the same forward and backward, e.g., "madam", "racecar".

🔍 Rules:
    Ignore spaces, punctuation, and case.
    Only alphanumeric characters matter (a-z, A-Z, 0-9).

📥 Examples:
    is_valid_palindrome("A man, a plan, a canal: Panama") ➞ True  
    is_valid_palindrome("race a car") ➞ False  
    is_valid_palindrome("No 'x' in Nixon") ➞ True  
    is_valid_palindrome("") ➞ True  
    is_valid_palindrome(".,") ➞ True

✅ Constraints:
    Don't use external libraries like re.
    Use only built-in string methods like .isalnum(), .lower(), slicing, etc.
'''

# Chat GPT proposal: 'sorted()' function separate the string into characteres and then organize using alphabet. So, if both are equals, you have a True
# def is_valid_palindrome(s):
#     filtered = [char.lower() for char in s if char.isalnum()]
#     return filtered == filtered[::-1]

def is_valid_palindrome(s):
    s_worked = ""
    s = s.lower().strip()

    for char in s:
        if char.isalnum():
            s_worked += char

    return s_worked == s_worked[::-1]       # You can reverse a list or string in Python with slicing: [::-1]

def main():
    print(is_valid_palindrome("A man, a plan, a canal: Panama"))
    print(is_valid_palindrome("race a car"))
    print(is_valid_palindrome("No 'x' in Nixon"))  
    print(is_valid_palindrome(""))
    print(is_valid_palindrome(".,"))

if __name__ == '__main__':
    main()