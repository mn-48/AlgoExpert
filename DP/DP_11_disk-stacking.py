#  O(n^2) Time | O(n) Space

def diskStacking(disks):
    disks.sort(key=lambda disk: disk[2])
    heights = [disk[2] for disk in disks]
    sequences = [None for disk in disks]
    maxHeightIdx = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            if checkDisk(otherDisk, currentDisk):
                if heights[i] <= heights[j] + currentDisk[2]:
                    heights[i] = heights[j] + currentDisk[2]
                    sequences[i] = j  # It is tricky
        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i
    return buildSequence(disks, sequences, maxHeightIdx)


def checkDisk(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]


def buildSequence(array, sequences, currentIdx):
    # print(sequences)
    sequence = []
    while currentIdx is not None:
        # print(currentIdx)
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))


if __name__ == "__main__":
    disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
    print(diskStacking(disks))
