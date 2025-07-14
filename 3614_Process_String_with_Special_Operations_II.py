class Solution(object):
    def processStr(self, s, k):
        ops = [] 
        curr_len = 0
        curr_rev = False

        for ch in s:
            if 'a' <= ch <= 'z':
                curr_len += 1
            elif ch == '*':
                curr_len = max(0, curr_len - 1)
            elif ch == '#':
                curr_len *= 2
            elif ch == '%':
                curr_rev = not curr_rev
            ops.append((curr_len, curr_rev))

        if k >= curr_len:
            return '.'

        curr_k = k

        for i in range(len(s) - 1, -1, -1):
            op = s[i]
            prev_len, prev_rev = ops[i - 1] if i > 0 else (0, False)

            if op == '%':
                curr_rev = not curr_rev
                curr_k = curr_len - 1 - curr_k 
            elif op == '#':
                if prev_len == 0:
                    curr_k = 0
                elif curr_k >= prev_len:
                    curr_k -= prev_len
            elif op == '*':
                if prev_len < curr_len:
                    if curr_k >= prev_len:
                        return '.'
            elif 'a' <= op <= 'z':
                if curr_len == prev_len + 1 and curr_k == prev_len:
                    return op

            curr_len = prev_len
            curr_rev = prev_rev

        return '.'
