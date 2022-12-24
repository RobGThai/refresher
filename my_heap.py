from typing import List
class MaxHeap:
    def __init__(self):
        self.items = []
        self.items_size = 0
    
    def move_up(self, pos: int) -> bool:
        if pos < 0:
            return False
        
        curr = pos
        print(f"curr[{curr}]")
        while(curr // 2 >= 0):
            print(f"Check p[{self.items[curr // 2]}] curr[{self.items[curr]}]")
            if self.items[curr // 2] < self.items[curr]:
                print("Parent need swap")
                self.items[curr], self.items[curr // 2] = self.items[curr // 2], self.items[curr]
                if not self.move_up(curr // 2):
                    break

            break
        
    def push(self, item: int):
        self.items.append(item)
        self.items_size += 1
        
        if self.items_size > 1:
            self.move_up(self.items_size - 1)
        
    def nlargest(self, n: int) -> List[int]:
        if n == 1:
            return self.items[0:0]

        if n > self.items_size:
            "Cover all items"
            return sorted(self.items, reverse=True)

        i = 1
        max_current_cap = 1
        while(True):
            max_current_cap = (2 ** i - 1)
            "Find depth and maximum items need to evaluate"
            i += 1
            if max_current_cap >= n:
                break

        if max_current_cap > self.items_size:
            max_current_cap = self.items_size - 1

        return sorted(self.items[0:max_current_cap], reverse=True)[0:n]



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        heap = MaxHeap()
        
        for n in nums:
            heap.push(n)
            print(f"Storage: {heap.items}")
            
        largest = heap.nlargest(k)
        print(f"largest: {largest}")
        return largest[-1]

if __name__ == "__main__":
    input = [3,2,1,5,6,4]
    nth = 2
    expect = 5
    result = Solution().findKthLargest(input, nth)

    print(f"result[{expect == result }]: expect[{expect}] got[{result}]")