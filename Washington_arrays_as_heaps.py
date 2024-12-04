def heapify(arr, n, i):
    """Helper function to maintain the heap property."""
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree

def build_heap(arr):
    """Function to build a max-heap from a given array."""
    n = len(arr)

    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

if __name__ == "__main__":
    # User input to create the heap
    print("Enter the elements of the heap (space-separated): ")
    user_input = input()
    heap_array = list(map(int, user_input.split()))

    # Build the heap
    build_heap(heap_array)

    # Output the array representing the heap
    print("Array representation of the max-heap:")
    print(heap_array)
