from typing import List

def constructDistancedSequence(n: int) -> List[int]:
    def backtrack(index):
        if index == size:
            return True
        if final_seq[index] != -1:
            return backtrack(index + 1)
        for i in range(n,0,-1):
            if not is_num_used[i]:
                is_num_used[i] = True
                final_seq[index] = i
                if i == 1:
                    if backtrack(index+1):
                        return True
                else:
                    second_index = index+i
                    if second_index < size and final_seq[second_index] == -1:
                        final_seq[index+i] = i
                        if backtrack(index+1):
                            return True
                        final_seq[index + i] = -1
                final_seq[index] = -1
                is_num_used[i] = False
        return False

    size = 2*n-1
    final_seq = [-1]*size
    is_num_used = [False]*(n+1)
    backtrack(0)
    return final_seq
n=5
print(constructDistancedSequence(n))
