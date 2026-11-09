import sys

def rotate_pansem(dx, dy, t):
    t = t % 4
    if t == 0:
        return dx,dy
    if t == 1:
        return dy, -dx
    if t == 2:
        return -dx,-dy
    return -dy, dx

def combine_pansem(t1, t2):
    dx1, dy1, r1 = t1
    dx2, dy2 ,r2 = t2
    rx2, ry2 = rotate_pansem(dx2, dy2, r1)
    return (dx1+rx2, dy1+ry2, (r1 + r2)%4)

def repeat_pansem(t,count):
    if count == 0:
        return (0,0,0)
    
    dx, dy, rot = t

    if rot % 4 == 0:
        return (dx*count, dy*count, 0)
    count = count % 4
    if (count * rot) % 4 == 0:
        return (0, 0, 0)
    answer = t
    for _ in range(1, count):
        answer = combine_pansem(answer,t)

    return answer

def solve_pansem():
    s = sys.stdin.readline().strip()
    if not s:
        return
    
    basic_moves = {
        'F': (0, 1, 0),
        'B': (0, -1, 0),
        'L': (-1, 0, 0),
        'R': (1, 0, 0),
        ')': (0, 0, 1),
        '(': (0, 0, 3),
    }
    stack = [(0,0,0)]
    counts = []
    i=0
    n=len(s)

    flag = True
    while i < n:
        char = s[i]

        if char in basic_moves:
            stack[-1] = combine_pansem(stack[-1], basic_moves[char])
            i+=1

        elif char in '0123456789':
            val = char
            i+=1
            while s[i] in '0123456789':
                val+=s[i]
                i+=1
            val = int(val)
            i+=1
            counts.append(val)
            stack.append((0,0,0))

        elif char == ']':
            povtor = stack.pop()
            k = counts.pop()
            repeated = repeat_pansem(povtor, k)
            stack[-1] = combine_pansem(stack[-1], repeated)
            i+=1

    answer_dx, answer_dy, t = stack[0]
    return answer_dx, answer_dy
if __name__ == '__main__':
    try:
        a_1, a_2 = solve_pansem()
        print(f'{a_1} {a_2}')
    except BaseException as e:
        print(f'пупупу{e}')