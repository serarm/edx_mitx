def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    sizeL=len(L)
    max_so_far,max_ending_here=0,0
    for i in range(sizeL):
        max_ending_here+=L[i]
        if max_ending_here<0:
            max_ending_here=0
        elif max_so_far<max_ending_here:
            max_so_far=max_ending_here
    return max_so_far

assert max_contig_sum([3, 4, -1, 5, -4])==11
assert max_contig_sum([3, 4, -8, 15, -1, 2])==16
assert max_contig_sum([1])==1
print("All testcases paassed")