
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    # O(n) Time | O(1) space
    def buildHeap(self, array):
        # start with first parent that exists
        first_parent = (len(array) - 1) // 2

        # for every parent inclusive of first parent upto root
        for parent in reversed(range(first_parent + 1)):
            # siftdown every parent idx
            self.siftDown(parent, len(array) - 1, array)

        return array


    # O(log(n)) Time | O(1) space
    def siftDown(self, cidx, endidx, heap):
        child_one_idx = cidx * 2 + 1

        # is child one a valid idx or does child one exist?
        while child_one_idx <= endidx:

            # does child two exist?
            child_two_idx = cidx * 2 + 2 if cidx * 2 + 2 <= endidx else -1

            # if child two exist and it's value is smaller than child one
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:

                # then the child we will compare with current node will be child two
                potential_swap_idx = child_two_idx

            else:
                # otherwise we will compare child one with the current node
                potential_swap_idx = child_one_idx

            # if the child is smaller than the current node
            if heap[potential_swap_idx] < heap[cidx]:

                # swap them
                self.swap(cidx, potential_swap_idx, heap)

                # new current node = the child index with which we swapped
                cidx = potential_swap_idx

                # new child one of this current node
                # we compute child to see if the child exist in the while loop above
                # if child exist, means we have to keep sifting down; otherwise we can stop
                child_one_idx = cidx * 2 + 1

            else:
                # if current node is smaller than both of it's children
                # we can stop, no need to sift down
                break

    # O(log(n)) Time | O(1) space
    def siftUp(self, idx, heap):
        parent_idx = (idx - 1) // 2

        # while idx > 0, because we can't siftup root node
        # while we can still sift up i.e parent is greater than child
        while idx > 0 and heap[idx] < heap[parent_idx]:
            # keep swapping current node with parent
            self.swap(idx, parent_idx, heap)
            # update the current node and the parent index
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    # O(1) Time | O(1) space
    def peek(self):
        # return the minimum of heap
        return self.heap[0]

    # O(1) Time | O(1) space
    def remove(self):
        # swap the last node with the root
        self.swap(0, len(self.heap)-1, self.heap)
        # extract the minimum value
        min_value = self.heap.pop()
        # sift down the root to it's correct position
        self.siftDown(0, len(self.heap)-1, self.heap)
        # return the minimum value
        return min_value

    # O(1) Time | O(1) space
    def insert(self, value):
        # insert the value at the end of the heap as the last node
        self.heap.append(value)
        # sift the value up to it's correct position
        self.siftUp(len(self.heap)-1, self.heap)


    # O(1) Time | O(1) space
    def swap(self, idx1, idx2, heap):
        # basic swap function
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]