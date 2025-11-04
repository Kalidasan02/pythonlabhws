paragraph = """  
Python is a powerful programming language that is easy to learn. 
This course helps beginners understand Python concepts clearly 
and provides hands-on practice with real examples.  
"""

length = len(paragraph)
print("Length of paragraph:", length)

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("Preview (first 50 chars):", paragraph[:50])

paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacement:\n", paragraph)

paragraph = paragraph.lower()
print("\nLowercase paragraph:\n", paragraph)

paragraph = paragraph.strip()

words = paragraph.split()
print("\nList of words:\n", words)

if "course" in words:
    print("\nThe word 'course' is found in the paragraph.")
else:
    print("\nThe word 'course' is not found in the paragraph.")

message = "The course description is {} characters long and has {} words.".format(length, len(words))
print("\n" + message)
