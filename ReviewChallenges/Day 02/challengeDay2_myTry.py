'''
🚀 Day 2 - Problem: "Anagram Check"
🧠 Description:
    Write a function are_anagrams(s1, s2) that returns True if the strings s1 and s2 are anagrams of each other, and False otherwise.

    An anagram is a word formed by rearranging the letters of another word, using all original letters exactly once.

🔍 Examples:
    are_anagrams("listen", "silent") ➞ True  
    are_anagrams("triangle", "integral") ➞ True  
    are_anagrams("apple", "papel") ➞ True  
    are_anagrams("rat", "car") ➞ False  
    are_anagrams("a", "A") ➞ False (case-sensitive)

✅ Constraints:
    Do not use external libraries like collections.
    Case-sensitive.
    You may assume both inputs are strings and non-null.
'''

# Chat GPT proposal: 'sorted()' function separate the string into characteres and then organize using alphabet. So, if both are equals, you have a True
# def are_anagrams(s1, s2):
#     return sorted(s1) == sorted(s2)

def are_anagrams(s1, s2):
    # s1_list = list(s1)
    # s1_list.sort()
    s1_list = sorted(s1)
    s2_list = sorted(s2)

    if len(s1_list) != len(s2_list):            # this is not necessary, but my thought was that could be easier to verify long strings quickly
        return False

    for i in range(len(s1_list)):
        if s1_list[i] != s2_list[i]:
            return False
    
    return True

def main():
    s1 = "listen"
    s2 = "silent"
    print(are_anagrams(s1, s2))
    print(are_anagrams("a", "A"))        # False (case-sensitive)
    print(are_anagrams("", ""))          # True
    print(are_anagrams("ab", "ba"))      # True
    print(are_anagrams("abc", "cba"))    # True
    print(are_anagrams("abcc", "cbca"))  # False

if __name__ == '__main__':
    main()

