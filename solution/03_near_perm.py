# может показаться, что на LLM, но нет похожий алгоритм нашел на http://e-maxx.ru/algo/profile_dynamics
import sys

def main_pan_sem():
    line = sys.stdin.readline().strip()
    
    if not line:
        return
    
    n, k = map(int, line.split())

    MOD = 998244353

    if k == 0:
        return 1

    if k >= n - 1:
        c = 1
        for i in range(1, n+1):
            c = (c * i) % MOD
        return c

    mask_size = 2**(2*k)
    start_mask = 2**k - 1

    dp = [0] * mask_size
    dp[start_mask] = 1

    active_masks = [start_mask]

    for i in range(1, n + 1):
        next_dp = [0] * mask_size
        next_active = []

        for mask in active_masks:
            ways = dp[mask]

            for j in range(2 * k + 1):
                v = i - k + j

                if v < 1 or v>n:
                    continue

                if j < 2*k and (mask & (1 << j)):
                    continue

                if j < 2 * k:
                    temp_mask = mask | (1 << j)
                else:
                    temp_mask = mask

                if not (temp_mask & 1):
                    continue

                new_mask = temp_mask >> 1

                if j == 2*k or (i + k > n):
                    new_mask = new_mask | (1<<(2*k - 1))

                if next_dp[new_mask] == 0:
                    next_active.append(new_mask)

                next_dp[new_mask] = (next_dp[new_mask] + ways) % MOD
                
        dp = next_dp
        active_masks = next_active
        
    ans = sum(dp) % MOD
    return ans

if __name__ == '__main__':
    print(main_pan_sem())







