from collections import deque

def is_valid(m_left, c_left, m_right, c_right):
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def bfs():
    start = (3, 3, 0)     # (Missionaries Left, Cannibals Left, Boat Side)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path + [state]

        m_left, c_left, boat = state

        if boat == 0:
            moves = [(2,0), (0,2), (1,1), (1,0), (0,1)]
        else:
            moves = [(-2,0), (0,-2), (-1,-1), (-1,0), (0,-1)]

        for m, c in moves:
            new_m_left = m_left - m
            new_c_left = c_left - c

            if 0 <= new_m_left <= 3 and 0 <= new_c_left <= 3:
                new_m_right = 3 - new_m_left
                new_c_right = 3 - new_c_left

                if is_valid(new_m_left, new_c_left,
                            new_m_right, new_c_right):
                    new_state = (new_m_left, new_c_left, 1 - boat)
                    queue.append((new_state, path + [state]))

solution = bfs()

print("Solution Path:")
for step in solution:
    print(step)
