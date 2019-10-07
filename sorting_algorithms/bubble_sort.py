# https://stackabuse.com/sorting-algorithms-in-python/
# Bubble sort iterates over a list, comparing elements in pairs and swapping them until the
# larger element "bubble up" to the end of the list, and the smaller elements at the "bottom"


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) -1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
                print('swapped', swapped)


# Testing
random_list = [6, 4, 5, 3, 2]
bubble_sort(random_list)
print(random_list)
