from BinomialHeap import BinomialHeap

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    heap = BinomialHeap()
    heap.make_heap([10, 1, 12, 25])
    heap.insert(18)
    print(heap)
    print(heap.min())
    print(heap.extract_min())
    print(heap)
    heap.decrease_key(25)
    print("Heap:\n", heap)
    heap.delete(18)
    print("Heap:\n", heap)


if __name__ == '__main__':
    main()
