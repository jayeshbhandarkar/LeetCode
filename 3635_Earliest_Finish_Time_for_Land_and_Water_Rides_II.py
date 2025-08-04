import bisect

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        tup = (landStartTime, landDuration, waterStartTime, waterDuration)

        def solve(r1, r2):
            r2.sort(key=lambda x: x[0])

            n_second = len(r2)

            if n_second == 0:
                return float('inf')

            min_f_sfx = [float('inf')] * n_second
            cur_fin = float('inf')
            
            for k in range(n_second - 1, -1, -1):
                s_start, s_duration = r2[k]
                cur_fin = min(cur_fin, s_start + s_duration)
                min_f_sfx[k] = cur_fin
            
            min_d_pfx = [float('inf')] * n_second
            cur_dur = float('inf')
            
            for k in range(n_second):
                s_start, s_duration = r2[k]
                cur_dur = min(cur_dur, s_duration)
                min_d_pfx[k] = cur_dur

            min_fin = float('inf')

            for f_start, f_duration in r1:
                f_finish = f_start + f_duration

                idx = bisect.bisect_left(r2, (f_finish, 0))

                if idx < n_second:
                    fin1 = min_f_sfx[idx]
                    min_fin = min(min_fin, fin1)

                if idx > 0:
                    fin2 = f_finish + min_d_pfx[idx - 1]
                    min_fin = min(min_fin, fin2)
            
            return min_fin

        lr = [(landStartTime[i], landDuration[i]) for i in range(len(landStartTime))]
        wr = [(waterStartTime[j], waterDuration[j]) for j in range(len(waterStartTime))]

        ans1 = solve(lr, wr)
        ans2 = solve(wr, lr)

        return min(ans1, ans2)
