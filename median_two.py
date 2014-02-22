class Solution:
    # @return a float
    def find_mids(self, total, start_a, end_a, start_b, end_b):
        gap = (end_a - start_a) + (end_b - start_b)
        frac_remain = gap / float(total)
        frac_a = float(end_a - start_a) / gap
        offset = frac_a * 
        mid_a = start_a + offset
        mid_b = start_b + gap - offset
#        mid_b = total/2 - mid_a - 1
        return mid_a, mid_b

    def bi_sear(self, vals, target, start, end):
        if end - start < 2:
            return start

        mid = start + (end - start)/2
        if target < vals[mid]:
            return self.bi_sear(vals, target, start, mid)
        else:
            return self.bi_sear(vals, target, mid, end)

    def base_case(self, sorted_vals, total):
        if len(sorted_vals) == 1:
            return sorted_vals[0]
        elif len(sorted_vals)==2:
            return (sorted_vals[0] + sorted_vals[1])/2.
        elif len(sorted_vals)==3:
            return solrted_vals[1]
        else:
            if total%2==0:
                return (sorted_vals[1] + sorted_vals[2])/2.
            else:
                return sorted_vals[2]

    def find_median(self, A, B, start_a, end_a, start_b, end_b):
        missing = (end_a - start_a) + (end_b-start_b)
        if missing < 5:
            vals = sorted(A[start_a:end_a] + B[start_b:end_b])
            return self.base_case(vals, len(vals))

        mid_a, mid_b = self.find_mids(len(A) + len(B), start_a, end_a, start_b, end_b)
        print mid_a, mid_b, start_a, end_a, start_b, end_b
        if A[mid_a] < B[mid_b]:
            end_a = min(self.bi_sear(A, B[mid_b], mid_a, end_a) + 2, end_a)
            start_b = self.bi_sear(B, A[mid_a], 0, mid_b)
            return self.find_median(A, B, mid_a, end_a, start_b, mid_b+1)
        else:
            start_a = self.bi_sear(A, B[mid_b], 0, mid_a)
            end_b = min(self.bi_sear(B, A[mid_a], mid_b, end_b) + 2, end_b)
            return self.find_median(A, B, start_a, mid_a+1, mid_b, end_b)

    def findMedianSortedArrays(self, A, B):
        if A is None or B is None:
            return None
        if not A or not B:
            full = A + B
            if len(full)==0:
                return None
            mid = len(full)/2
            if len(full)%2==0:
                return (full[mid-1] + full[mid])/2.
            else:
                return full[mid]
        
        return self.find_median(A, B, 0, len(A), 0, len(B))
        

s = Solution()
A = [2,3,4,5,7] 
B = [1,6,8,9,10]
print s.findMedianSortedArrays(A, B)
