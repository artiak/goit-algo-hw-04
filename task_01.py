"""
Compares time complexity of Insertion Sort,
Merge Sort and Tim Sort algorithms

Example of relusts for list with int elements:
'Insert Sort' for '20000' elments takes '4746' ms
'Merge Sort' for '20000' elments takes '204' ms
'Tim Sort' for '20000' elments takes '1' ms

Tim Sort is the most effective sorting algorithm.
"""
import random
import timeit


def _lst(num: int) -> list:
    res: list = []
    for _ in range(num):
        res.append(random.randint(0, 99))

    return res


def _insert_sort(src: list) -> None:
    for i in range(1, len(src)):
        cur = src[i]
        j: int = i - 1
        while j >= 0 and cur < src[j]:
            src[j+1] = src[j]
            j -= 1
        src[j+1] = cur


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


def _measure(name: str, src: list, func: callable = None) -> None:
    seconds = timeit.timeit(lambda: func(src) if func else src.sort(), number=10)
    millis = int(seconds * 1000)
    print(f"{name} for '{len(src)}' elments takes '{millis}' ms")


if __name__ == "__main__":
    lst_size: int = 20_000

    lst = _lst(lst_size)
    _measure("Insert Sort", lst, _insert_sort)
    lst = _lst(lst_size)
    _measure("Merge Sort", lst, _merge_sort)
    lst = _lst(lst_size)
    _measure("Tim Sort", lst)
