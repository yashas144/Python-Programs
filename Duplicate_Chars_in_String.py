'''# Python Code to print duplicate characters and their counts using Hashing

# Function to print duplicate characters with their count
def printDuplicates(s):

    # Hash map to store frequency of each character
    freq = {}

    # Count frequency of each character
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # Traverse the map and print characters with count > 1
    for key in freq:
        if freq[key] > 1:
            print(["{}".format(key), freq[key]], end=", ")

if __name__ == "__main__":

    s = input("Enter a string: ")

    printDuplicates(s)'''


# Python Code to print all characters and their counts using Hashing (using dictionary to store data in key:value pairs)
# Hash Map: This is the architectural design (the logic) used to make the dictionary work. 
# It uses a "hash function" to turn your key (like the character 'a') into a specific index in memory.


# simply put, I used a Python Dictionary, which is a Hash Map by design in this program.

def printAllFrequencies(s):
    # Hash map to store frequency of each character
    freq = {}

    # Count frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Print a header for clarity
    print(f"\nCharacter counts for: '{s}'")
    print("-" * 30)

    # Traverse the map and print every character and its count
    for key in freq:
        # Using f-strings for cleaner output formatting
        print(f"'{key}': {freq[key]}")

if __name__ == "__main__":
    user_ip = input("Enter a string: ")
    printAllFrequencies(user_ip)


# Alternative approach using collections.Counter, which is a built-in Python class specifically designed for counting hashable objects.
from collections import Counter

s = input("Enter a string: ")
counts = Counter(s)

for char, count in counts.items():
    print(f"{char}: {count}")