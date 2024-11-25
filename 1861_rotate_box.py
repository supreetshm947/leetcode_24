import numpy as np

def rotateTheBox(box):
    """
    :type box: List[List[str]]
    :rtype: List[List[str]]
    """
    out = np.zeros(())
    for index, sub in enumerate(box):
        i = len(sub) - 2
        while i >= 0:
            if sub[i] == "#":
                j = i + 1
                while j < len(sub):
                    if sub[j] == "." and sub[j - 1] == "#":
                        sub[j] = "#"
                        sub[j - 1] = "."
                    else:
                        break
                    j += 1
            i -= 1

    return np.fliplr(np.array(box).T).tolist()

box = [["#",".","#"]]
#print(rotateTheBox(box))
box1 = [["#",".","*","."],["#","#","*","."]]
print(rotateTheBox(box1))