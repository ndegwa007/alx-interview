#!/usr/bin/python3
"""lockboxes problem"""
from collections import deque


def canUnlockAll(boxes):
    """checks if all boxes can be opened"""
    if len(boxes) == 0:
        return False
    n = len(boxes)
    visited = [False] * n
    # first box is open
    visited[0] = True

    # using BFS create a queue and put the first box
    queue = deque([0])

    while queue:
        checked_box = queue.popleft()
        if checked_box > len(boxes):
            return False
        for key in boxes[checked_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
