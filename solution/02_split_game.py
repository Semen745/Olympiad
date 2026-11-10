import sys

def granize_pansem(m,k):
    b_min = (m + k) // (k+1) # округляем вверх, так-то пишется m//(k+1)
    b_max = (m-1) // 2
    return b_min, b_max
def get_mex_pansem(to_kuda_we_mogem_popast_za_one_xod): # каюсь формулу саму подсмотрел в интернете но не LLM
    used = [False] * (len(to_kuda_we_mogem_popast_za_one_xod) + 1)

    for val in to_kuda_we_mogem_popast_za_one_xod:
        if val < len(used):
            used[val] = True

    for mex in range(len(used)):
        if not used[mex]:
            return mex 
def g_pansem(a, k):
    max_a = max(a)
    g = [0] * (max_a + 1)

    for m in range(1, max_a + 1):
        b_min, b_max = granize_pansem(m, k)

        if b_min > b_max:
            continue

        sobiraem_vse_XOR = []

        for b in range(b_min, b_max+1):
            sobiraem_vse_XOR.append(g[b] ^ g[m-b])
        g[m] = get_mex_pansem(sobiraem_vse_XOR)

    return g

def finally_pansem(a,k):
    g = g_pansem(a,k)

    total_xor = 0
    for x in a:
        total_xor ^= g[x]

    if total_xor == 0:
        return "Lose 0"

    win_moves = 0
    for m in set(a):
        b_min,b_max = granize_pansem(m,k)

        if b_min > b_max:
            continue

        target = total_xor ^ g[m]
        for b in range(b_min, b_max + 1):
            if (g[b] ^ g[m-b]) == target:
                win_moves +=1
    return f'Win {win_moves}'

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
    all_t = int(line)
    answers = []
    for _ in range(all_t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        answers.append(finally_pansem(a,k))
    for answer in answers:
        print(answer)
if __name__ == '__main__':
    main()
