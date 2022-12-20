'''
@author : Harshitha Benakanahalli Nagaraj
 file : food_truck.py
'''

'''
This program computes the optimal location for a food truck
using two different algorithms
:the QuickSort, and  a selection algorithm called QuickSelect.
'''


import os
import random
import sys
import time


# function to perform QuickSort

def quickSort(list_of_distances):
    empty_list = []

    if len(list_of_distances) == 0:
        return empty_list
    else:
        # select a random pivot
        pivot_selectindex = random.randint(0, len(list_of_distances) - 1)
        pivot = list_of_distances[pivot_selectindex]
        less_list = []
        equal_list = []
        greater_list = []

        for i in range(0, len(list_of_distances)):
            # append all the elements lesser than pivot to less-list
            if list_of_distances[i] < pivot:
                less_list.append(list_of_distances[i])
            # append all the elements greater than pivot to greater_list
            if list_of_distances[i] > pivot:
                greater_list.append(list_of_distances[i])
            # append the elements equal to pivot to equal_list
            if list_of_distances[i] == pivot:
                equal_list.append(list_of_distances[i])
            else:
                empty_list.append(list_of_distances[i])

        return quickSort(less_list) + equal_list + quickSort(greater_list)


# function to find the optimal location using QuickSort.
def optimal_solution(sort_list):
    sorted_list = quickSort(sort_list)
    # returns the median.
    return sorted_list[int(len(sort_list) / 2)]


# program to compute the sum of distances
def sum_of_distances(list_sum):
    sumOfDistances = 0
    list_final = quickSort(list_sum)
    optimal = optimal_solution(list_final)
    for i in range(0, len(list_final)):
        sumOfDistances = sumOfDistances + abs(int(list_final[i]) - optimal)
    return sumOfDistances


# function to implement Selection algorithm : QuickSelect and find optimal location.
def quick_select(select_list, low, high):
    pivot = select_list[high]
    pivotpoint = low
    for i in range(low, high):
        if select_list[i] < pivot:
            list_1 = select_list[i]
            select_list[i] = select_list[pivotpoint]
            select_list[pivotpoint] = list_1
            pivotpoint = pivotpoint + 1
    list_1 = select_list[pivotpoint]
    select_list[pivotpoint] = select_list[high]
    select_list[high] = list_1
    return pivotpoint


# function to pass kth element to QuickSelect.
def quickSelect_optimal(k_list, k, low, high):
    pivot_point = quick_select(k_list, low, high)
    if pivot_point == k - 1:
        return k_list[pivot_point]
    if pivot_point < k - 1:
        return quickSelect_optimal(k_list, k, pivot_point + 1, high)
    if pivot_point > k - 1:
        return quickSelect_optimal(k_list, k, low, pivot_point - 1)


# main function.
def main():
    # read the file
    if len(sys.argv) < 3:
        with open(sys.argv[-1], 'r') as f:
            distances = f.readlines()
            distances_list = []
            for string in distances:
                distances_truck = string.rstrip('\n').split(" ")
                distances_list.append(int(distances_truck[1]))
        print("File :", sys.argv[-1])
        print("Number of buildings:", len(distances_list))
        print("Using Quick Sort to find Optimal Location:")
        start = time.perf_counter()
        optimal_point = optimal_solution(distances_list)
        end = time.perf_counter() - start
        print("\tElapsed time:", end, " seconds")
        print("\tOptimal food truck location is :", optimal_point)
        print("\tSum of Distances  :", sum_of_distances(distances_list))

        sorting_list = quickSort(distances_list)

        indexOf = optimal_solution(distances_list)
        k = sorting_list.index(indexOf) + 1

        print("Using Quick Select to find optimal location:")
        start = time.perf_counter()
        got_k_element = quickSelect_optimal(distances_list, k, 0, len(distances_list) - 1)
        end = time.perf_counter() - start
        print("\tElapsed time:", end, " seconds")
        print("\tOptimal food truck location:", got_k_element)
        print("\tSum of Distances :", sum_of_distances(distances_list))
    # prints usage message if there are more number of arguments.
    else:
        print('Usage: ' + os.path.basename(sys.argv[0] + " " + os.path.basename(sys.argv[-1])))
        sys.exit(1)


# main function call.
if __name__ == "__main__":
    main()
