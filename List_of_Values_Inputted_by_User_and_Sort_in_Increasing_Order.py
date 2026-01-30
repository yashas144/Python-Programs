def bubble_sort(arr):
    """
    Sorts a list of numbers in increasing order using the Bubble Sort algorithm.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def get_user_list():
    """
    Prompts the user to enter a series of numbers and returns a list.
    """
    user_list = []
    print("Enter numbers to add to the list. Type 'done' when finished.")
    while True:
        user_input = input("Enter a number or 'done': ")
        if user_input.lower() == 'done':
            break
        try:
            # Convert input to a float to allow for non-integer numbers
            number = float(user_input)
            user_list.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
    return user_list

# Main part of the program
if __name__ == "__main__":
    my_list = get_user_list()
    if not my_list:
        print("The list is empty. No sorting required.")
    else:
        print(f"\nOriginal list: {my_list}")
        sorted_list = bubble_sort(my_list)
        print(f"Sorted list (increasing order): {sorted_list}")
