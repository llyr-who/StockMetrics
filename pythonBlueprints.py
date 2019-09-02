# this is collection of functions
# that get some possibly useful information
# from a time-series

import numpy as np
import matplotlib.pyplot as plt
import queue as q
A = [1,2,4,37,45,3,45,7,2,23,45,6,73,2,3]

plt.plot(A)

# returns the maximum drawdown
# and the time at which this occurs
def max_drawdown(X):
    T = 0;
    t = 0;
    mdd = 0
    peak = X[0]
    for x in X:
        if x > peak: 
            peak = x
        dd = (peak - x) / peak
        if dd > mdd:
            mdd = dd
            T = t;
        # increment time
        t += 1
    return (mdd,T)

# calculate the average time
# between new maximumss
def avg_time_between_max(X):
    avg = 0.0
    max_count = 0;
    t = 0;
    peak = X[0]
    for x in X:
        if x > peak:
            peak = x
            avg += t
            t = 0
            max_count += 1
        t += 1
    if max_count == 0:
        return None
    else:
        return avg/max_count

# calculate the average time
# between new max peaks
def avg_time_between_max_peaks(X):
    avg = 0.0
    t = 0
    sz = len(X)
    peak = X[0]
    peak_count = 0
    for i in range(sz-1):
        if X[i] > peak and X[i+1] < X[i]:
            peak = X[i]
            avg += t
            t = 0
            peak_count += 1
        t += 1
    if peak_count == 0:
        return None
    else:
        return avg/peak_count

# find the span of the stock price
#
# e.g return an array where T[i] 
# tells us how long it has 
# been since there has been
# a price higher than A[i]
# A = [100,90,80,70]
# T = [1,1,1,1]
# 
# A = [1,2,3,4,5,6]
# T = [1,2,3,4,5,6]
#
# A = [1,3,5,2,9,14]
# T = [1,2,3,1,5,6]
#
# A = [1,9,4,6,4,5,7,3,6,2]
# T = [1,2,1,2,1,2,5,1,2,1]
def span(X):
    sz = len(X)
    stk = [0]
    T = [1]
    for i in range(1,sz):
        while len(stk) > 0 and X[stk[-1]] <= X[i]:
            stk.pop()
        if len(stk) == 0:
            T.append(i + 1)
        else:
            T.append(i - stk[-1])
        stk.append(i)
    print(stk)
    return T


# Given the price of share on n days,
# find the maximum profit that you can 
# make by buying and selling a share at most twice.

print("The data " + str(A))
print("(MDD,time) = " + str(max_drawdown(A)))
print("average time between max = " + str(avg_time_between_max(A)))
print("average time between max = " + str(avg_time_between_max_peaks(A)))
print("The span " + str(span(A)))
