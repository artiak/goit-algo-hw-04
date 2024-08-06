"""
Compares time complexity of Insertion Sort,
Merge Sort and Tim Sort algorithms.
"""
import random
# from timeit import timeit
import timeit


def _insert_sort(lst: list) -> None:
    for i in range(1, len(lst)):
        cur = lst[i]
        j: int = i - 1
        while j >= 0 and cur < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = cur


def _merge_sort(src: list) -> list:
    src_len: int = len(src)

    if src_len <= 1:
        return src

    mdl_idx: int = src_len // 2
    lft: list = _merge_sort(src[:mdl_idx])
    rgt: list = _merge_sort(src[mdl_idx:])

    lft_idx: int = 0
    rgt_idx: int = 0

    lft_len: int = len(lft)
    rgt_len: int = len(rgt)

    tgt: list = []

    while lft_idx < lft_len and rgt_idx < rgt_len:
        lft_val: int = lft[lft_idx]
        rgt_val: int = rgt[rgt_idx]
        if lft_val < rgt_val:
            tgt.append(lft_val)
            lft_idx += 1
        else:
            tgt.append(rgt_val)
            rgt_idx += 1

    for idx in range(lft_idx, lft_len):
        tgt.append(lft[idx])

    for idx in range(rgt_idx, rgt_len):
        tgt.append(rgt[idx])

    return tgt


def _src(num: int) -> list:
    res: list = []
    for _ in range(num):
        res.append(random.randint(0, 99))

    return res

def _measure_sort(name: str, func: callable, src: list = None) -> None:
    seconds = timeit.timeit(lambda: func(src) if src else func(), number=10)
    millis = int(seconds * 1000)
    print(f"{name} for '{len(src)}' elments takes '{millis}' ms")

if __name__ == "__main__":
    lst_size: int = 10_000
    src: list = _src(lst_size)

    _measure_sort("Insert Sort", _insert_sort, src)
    _measure_sort("Merge Sort", _measure_sort, src)
    _measure_sort(name = "Tim Sort", func = src.sort)
