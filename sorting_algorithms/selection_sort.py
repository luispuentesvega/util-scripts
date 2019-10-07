# https://stackabuse.com/sorting-algorithms-in-python/
# This algorithm segments the list in two parts: sorted and unsorted
# We continuously remove the smallest element of the unsorted segment of the list
# and append it to the sorted segment


def selection_sort(nums):
    for i in range(len(nums)):
        # We assume that the first item of the unsorted element is the smallest
        lowest_value_index = i
        # Iterate over the unsorted items
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Swap the values of the lowest unsorted element with the first unsorted element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

# Testing
random_list = [6, 4, 5, 3, 2]
selection_sort(random_list)
print(random_list)
