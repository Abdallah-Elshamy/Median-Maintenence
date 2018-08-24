#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 14:19:47 2018

@author: abdallah
"""
import heapq

def median_maintenence(nums):
    h_low = []
    h_high = []
    sum_of_medians = 0
    for num in nums:
        if len(h_low) == 0 :
            heapq.heappush(h_low,-num)
        elif num < -h_low[0]:
            heapq.heappush(h_low,-num)
        else:
            heapq.heappush(h_high,num)
            
        if len(h_low) > len(h_high)+1 :
            heapq.heappush( h_high, -heapq.heappop(h_low) )
        if len(h_high) > len(h_low)+1 :
            heapq.heappush(h_low, -heapq.heappop(h_high) )
        
        if len(h_high) == len(h_low):
            sum_of_medians -= h_low[0]
        else:
            if len(h_high) < len(h_low):
                sum_of_medians -= h_low[0]
            else:
                sum_of_medians += h_high[0]
    return sum_of_medians
            
            
nums = []
with open('Median.txt') as f:
    data = f.readlines()
    for line in data:
        nums.append(int(line))
f.close()

print(median_maintenence(nums) % 10000 )