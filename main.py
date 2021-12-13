from BinomialHeap import BinomialHeap

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    heap = BinomialHeap()
    heap.make_heap([10, 1, 12, 25])
    heap.insert(18)
    print("Heap\n", heap)
    print("Min: ", heap.min())
    heap.extract_min()
    print("Heap:\n", heap)
    print("Min: ", heap.min())
    heap.decrease_key(25)
    print("Heap:\n", heap)
    heap.delete(18)
    print("Heap:\n", heap)

    another_heap = BinomialHeap()
    another_heap.insert(1)
    another_heap.insert(2)
    print("Heap:\n", another_heap)
    print("Min: ", another_heap.min())
    heap.union(another_heap)
    print("Heap:\n", heap)


if __name__ == '__main__':
    main()
