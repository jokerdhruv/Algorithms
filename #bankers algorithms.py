#bankers algorithms
from typing import List, Tuple

def is_safe(processes: List[int], available: List[int], allocated: List[List[int]], need: List[List[int]]) -> bool:
    work = available.copy()
    finish = [False] * len(processes)
    safe_seq = []
    
    while not all(finish):
        found = False
        for i, process in enumerate(processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(len(available))):
                finish[i] = True
                found = True
                safe_seq.append(process)
                for j in range(len(available)):
                    work[j] += allocated[i][j]
        if not found:
            return False
    
    print("Safe Sequence:", safe_seq)
    return True

def main():
    num_processes = 5
    num_resources = 3
    processes = [i for i in range(num_processes)]
    available = [3, 3, 2]
    allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
    need = [[7, 4, 3], [0, 2, 0], [6, 0, 0], [0, 1, 1], [4, 3, 1]]
    if is_safe(processes, available, allocated, need):
        print("System is safe.")
    else:
        print("System is unsafe.")
        
if __name__ == "__main__":
    main()
