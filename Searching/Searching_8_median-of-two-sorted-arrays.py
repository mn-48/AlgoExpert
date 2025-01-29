# O(log(min(n, m))) time | O(1) space
def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    smallArray = arrayOne if len(arrayOne) <= len(arrayTwo) else arrayTwo
    bigArray = arrayOne if len(arrayOne) > len(arrayTwo) else arrayTwo

    leftIdx = 0
    rightIdx = len(smallArray)
    mergedLeftIdx = (len(smallArray) + len(bigArray)-1)//2

    while True:
        smallPartitionIdx = (leftIdx + rightIdx) // 2
        bigPartitionIdx = mergedLeftIdx - smallPartitionIdx - 1

        smallMaxLeftValue = (
            smallArray[smallPartitionIdx] if smallPartitionIdx >= 0 else float(
                "-inf")
        )

        smallMinRightValue = (
            smallArray[smallPartitionIdx + 1]
            if smallPartitionIdx + 1 < len(smallArray)
            else float("inf")
        )

        bigMaxLeftValue = bigArray[bigPartitionIdx] if bigPartitionIdx >= 0 else float(
            "-inf")

        bigMinRightValue = (
            bigArray[bigPartitionIdx + 1]
            if bigPartitionIdx + 1 < len(bigArray)
            else float("inf")
        )

        if smallMaxLeftValue > bigMinRightValue:
            rightIdx = smallPartitionIdx - 1
        elif bigMaxLeftValue > smallMinRightValue:
            leftIdx = smallPartitionIdx + 1
        else:
            if (len(smallArray) + len(bigArray)) % 2 == 0:
                return (
                    max(smallMaxLeftValue, bigMaxLeftValue) +
                    min(smallMinRightValue, bigMinRightValue)
                ) / 2
            return max(smallMaxLeftValue, bigMaxLeftValue)


if __name__ == "__main__":

    arrayOne = [1, 3, 4, 5]
    arrayTwo = [2, 3, 6, 7]
    ans = medianOfTwoSortedArrays(arrayOne, arrayTwo)
    print(ans)
