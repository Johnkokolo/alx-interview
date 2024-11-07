#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (list of lists): List of boxes, where each box contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = {0}  # Start with the first box unlocked
    keys = [0]      # Stack of boxes to explore, starting with box 0

    while keys:
        current_box = keys.pop()  # Take a box to explore its keys
        for key in boxes[current_box]:
            if key not in unlocked and key < n:  # If we haven't unlocked this box and it's a valid box
                unlocked.add(key)               # Unlock it
                keys.append(key)                # Add to the stack to explore its keys

    # If the number of unlocked boxes equals the total number of boxes, return True
    return len(unlocked) == n
