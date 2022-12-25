import heapq

class MatItem:
    def __init__(self, mat: List[int], total: int, position: int):
        self.mat = mat
        self.total = total
        self.position = position
        
    def __lt__(self, other) -> bool:
        print(f"lt: st[{self.total}] ot[{other.total}] sp[{self.position}] op[{other.position}]")
        return (self.total, self.position) < (other.total, other.position)
        
    def __le__(self, other) -> bool:
        print(f"le: st[{self.total}] ot[{other.total}] sp[{self.position}] op[{other.position}]")
        return (self.total, self.position) <= (other.total, other.position)
        
    def __gt__(self, other) -> bool:
        print(f"gt: st[{self.total}] ot[{other.total}] sp[{self.position}] op[{other.position}]")
        return (self.total, self.position) > (other.total, other.position)
        
    def __ge__(self, other) -> bool:
        print(f"ge: st[{self.total}] ot[{other.total}] sp[{self.position}] op[{other.position}]")
        return (self.total, self.position) >= (other.total, other.position)
        
    def __eq__(self, other) -> bool:
        print(f"eq: st[{self.total}] ot[{other.total}] sp[{self.position}] op[{other.position}]")
        return (self.total, self.position) == (other.total, other.position)
        
    def __ne__(self, other) -> bool:
        print(f"ne: st[{self.total}] ot[{other.total}] sp[{self.position}] op[{other.position}]")
        return (self.total, self.position) != (other.total, other.position)

def sort_total_position(m: type[MatItem]) -> tuple[int, int]:
    return (m.total, m.position)

class Solution:
    """
    https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/solutions/501705/official-solution/
    """
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        simple_mat = []
        for i, m in enumerate(mat):
            tot = 0
            for n in m:
                tot += n
            simple_mat.append(MatItem(mat, tot, i))
            
        heapq.heapify(simple_mat)
        h = list(map(lambda x: x.position, simple_mat))
        print(f"sim: {h}")
        result = heapq.nsmallest(k, simple_mat, key=sort_total_position)
        print(f"result: {result}")
        return list(map(lambda x: x.position, result))
    