#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

def canUnlockAll(boxes):
    # The list of unlocked boxes, starting with box 0 unlocked
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    
    # We can use a stack or queue for DFS or BFS
    # Use a stack (for DFS) initialized with box 0
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        
        # Explore all keys in the current box
        for key in boxes[current_box]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    
    # Check if all boxes are unlocked
    return all(unlocked)
