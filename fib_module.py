import numpy as np

def fib_series(n):
    ans_list=np.ones((n))
    for i in range(2,n):
        ele=ans_list[i-1]+ans_list[i-2]
        ans_list[i]=ele
    return ans_list

