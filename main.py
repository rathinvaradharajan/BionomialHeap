from BinomialHeap import BinomialHeap

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    heap = BinomialHeap()
    heap.insert(10)
    heap.insert(1)
    heap.insert(12)
    heap.insert(25)
    heap.insert(18)
    print(heap)
    print(heap.min())
    print(heap.extract_min())
    print(heap)


if __name__ == '__main__':
    main()
