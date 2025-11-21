# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module contains three sorting algorithms: bubble sort, quick sort, and insertion sort.
"""

import time
import psutil


def bubble(int_list):
    """Returns a sorted list using the bubble sort algorithm.

    @param1 int_list: list of integers to sort
    @return sorted: list of integers
    """
    n = len(int_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
                swapped = True
        if not swapped:
            break
        print("Bubble Sort - CPU Usage:", psutil.cpu_percent())  # print CPU usage
        time.sleep(0.5)  # delay execution by 0.5 seconds
    return int_list


# Quick Sort
def quick(int_list):
    """Returns a sorted list using the quick sort algorithm.

    @param1 int_list: list of integers to sort
    @return sorted: list of integers
    """
    start = time.time()  # get start time of program
    if len(int_list) <= 1:
        return int_list

    pivot = int_list[len(int_list) // 2]
    left = [x for x in int_list if x < pivot]
    mid = [x for x in int_list if x == pivot]
    right = [x for x in int_list if x > pivot]

    end = time.time()  # get end time of program
    print(
        "Quick Sort - Runtime:", end - start
    )  # print difference of end and start times
    return quick(left) + mid + quick(right)


# Insertion Sort
def insertion(int_list):
    """Returns a sorted list using the insertion sort algorithm.

    @param1 int_list: list of integers to sort
    @return sorted: list of integers
    """
    for i in range(1, len(int_list)):
        key = int_list[i]
        j = i - 1
        while j >= 0 and key < int_list[j]:
            int_list[j + 1] = int_list[j]
            j -= 1
        int_list[j + 1] = key
    print(
        "Insertion Sort - Memory Usage:", psutil.virtual_memory().percent
    )  # print memory usage of after code is complete
    return int_list
