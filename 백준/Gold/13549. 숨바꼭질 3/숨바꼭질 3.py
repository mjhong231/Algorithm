import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())  # 수빈이 위치 N, 동생 위치 K

def dik(start):
    hq = []
    dp = [float('inf')] * 100001
    dp[start] = 0
    heapq.heappush(hq, (0, start))  # (시간, 위치)

    while hq:
        cur_t, cur_pos = heapq.heappop(hq)

        if dp[cur_pos] < cur_t:
            continue

        for next_pos, time in [(cur_pos - 1, 1), (cur_pos + 1, 1), (cur_pos * 2, 0)]:
            if 0 <= next_pos < 100001:  
                next_time = cur_t + time  
                
                if next_time < dp[next_pos]:
                    dp[next_pos] = next_time
                    heapq.heappush(hq, (next_time, next_pos))

    return dp[K]

print(dik(N))
