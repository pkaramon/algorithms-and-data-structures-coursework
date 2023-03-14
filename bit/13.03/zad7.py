class RangeCounter:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        self.counts = [0]*(k+1)
        self._compute_counts()


    def _count_n(self, n):
        if n == 0:
            return self.counts[0]
        return self.counts[n] - self.counts[n-1]

    def _compute_counts(self):
        for x in self.nums:
            self.counts[x] += 1
        for i in range(1,len(self.counts)):
            self.counts[i] += self.counts[i-1]
    
    # 2 5
    # x y
    # x - 0 <= n <= 2
    # y - 0 <= n <= 5
    # y - x - (2,5]
    # 2 =    
    #
    # 2 3 
    # x y
    # y - x = ilość trójek
    # 0--1--2
    # 0--1--2--3



    def count_num_in_range(self, a, b):
        return self.counts[b] - self.counts[a] + self._count_n(a)
        
        

