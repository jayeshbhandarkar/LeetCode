class Solution(object):
    def popcountDepth(self, nums, queries):
        def compute_depth(x):
            depth = 0
            while x > 1:
                x = bin(x).count('1')
                depth += 1
            return depth

        class BIT:
            def __init__(self, size):
                self.n = size + 2
                self.tree = [0] * self.n

            def update(self, i, delta):
                i += 1
                while i < self.n:
                    self.tree[i] += delta
                    i += i & -i

            def query(self, i):
                i += 1
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i & -i
                return res

            def range_query(self, l, r):
                return self.query(r) - self.query(l - 1)

        n = len(nums)
        arr = nums[:] 

        max_depth = 6
        bits = [BIT(n) for _ in range(max_depth + 1)]
        depths = [0] * n

        for i in range(n):
            d = compute_depth(arr[i])
            depths[i] = d
            bits[d].update(i, 1)

        res = []

        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                if k > max_depth:
                    res.append(0)
                else:
                    res.append(bits[k].range_query(l, r))
            else:
                _, idx, val = q
                old_d = depths[idx]
                new_d = compute_depth(val)
                if old_d != new_d:
                    bits[old_d].update(idx, -1)
                    bits[new_d].update(idx, 1)
                    depths[idx] = new_d
                arr[idx] = val

        return res
