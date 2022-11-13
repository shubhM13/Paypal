#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13, 2022
@author: anirban-mac
"""
"""
https://www.hackerrank.com/contests/hack-it-to-win-it-paypal/challenges/largest-subset-sum
Q1 Largest Subset Sum locked
Given an integer, k, we want to find the largest subset of integers in the 
inclusive range from  1 to k such that the Least Common Multiple (LCM) of the 
elements in the subset is equal to k. We then want to find the of all integers 
in this subset.
Complete the maxSubsetSum function in the editor below. It has one parameter: 
    an array of n integers, k . 
    The function must return an array of n long integers where the value at each 
    index  i (where 0<=i<=n), denotes the sum  of the elements in the largest 
    subset of integers in the inclusive range from 1 to ki such that the LCM of 
    the elements in the subset is ki .
Input Format
The first line contains an integer, n , denoting the number of elements in k. 
Each line i of the n subsequent lines (where 0<=i<=n ) contains an integer 
describing ki.
Output Format
The function must return an array of n long integers where the value at each 
index i (where 0<=i<=n ), denotes the sum of the elements in the largest subset 
of numbers in the inclusive range from 1 to ki such that the LCM of the elements
 in the subset is ki.
Sample Input 0
2
2
4
Sample Output 0
3
7
Sample Input 1
1
10
Sample Output 1
18
Sample Input 2
2
5
6
Sample Output 2
6
12
"""
#!/bin/python3




import math
def maxSubsetSum(k):
    # Complete this function
    sums = []
    for lcm in k:
        sum = 0
        for i in range(1, int(math.sqrt(lcm)) + 1):
            if lcm % i == 0:
                if lcm/i == i:
                    sum = sum + i
                else:
                    sum = sum + i
                    sum = sum + lcm//i
        sums.append(sum)
    return sums


if __name__ == "__main__":
    size = int(input().strip())
    k = []
    k_i = 0
    for k_i in range(size):
        k_t = int(input().strip())
        k.append(k_t)
    res = maxSubsetSum(k)
    for sum in res:
        print(sum)

# TIP: sqrt(n) for time complexity
