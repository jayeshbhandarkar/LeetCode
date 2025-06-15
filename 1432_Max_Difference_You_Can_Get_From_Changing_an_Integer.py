class Solution(object):
    def maxDiff(self, num):
        s = str(num)

        for ch in s:
            if ch != '9':
                maxi = s.replace(ch, '9')
                break

            else:
                maxi = num

        if s[0] != '1':
            mini = s.replace(s[0], '1')
        
        else:
            for ch in s[1:]:
                if ch != '0' and ch != s[0]:
                    mini = s.replace(ch, '0')
                    break

                else:
                    mini = num

        return int(maxi) - int(mini)
