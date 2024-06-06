# 0x01. Lockboxes

## Description

This project contains a method to determine if all the boxes can be opened. Each box may contain keys to other boxes. The objective is to check if you can access and open all boxes starting from the first one.

## How It Works

1. Initialization:

- The function starts by unlocking the first box (box 0).
- A set opened_boxes keeps track of the boxes that have been opened.
- A list keys contains the keys you currently have, starting with the key for box 0.

2. Collect Keys and Open Boxes:

- The function uses a while loop to continue processing as long as there are keys available.
- It pops a key from the keys list and uses it to open a corresponding box if it hasn't been opened yet.
- It then collects all keys from the newly opened box and adds them to the keys list.

3. Final Check:

- After processing all keys, the function checks if the number of opened boxes equals the total number of boxes.
- If all boxes are opened, it returns True; otherwise, it returns False.

## Test Cases

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Should return True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Should return True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Should return False
```
