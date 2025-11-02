# day08/part1_initpy.py
# 다른 폴더에 있는 clock 기능을 이 파일로 가져왔다.
# __init__에서 workspace 폴더를 이미 환경변수로 등록했기 때문에
# 따로 환경변수를 등록할 필요가 없다.
from __init__ import clock
from day05.part1_sort_quick import quick_sort
from day05.part2_sort_merge import merge_sort, merge
from day06.part1_sort_heap import MaxHeap, MaxHeap2

@clock
def quick(datas):
    return quick_sort(datas)

@clock
def merge_sort2(datas):
    return merge_sort(datas)

@clock
def heap_sort(datas):
    heap = MaxHeap()
    [heap.insert(e) for e in datas]
    result = [heap.extract_max() for e in datas]
    return result

if __name__ == "__main__":
    import random as r
    datas = list(range(300000))
    r.shuffle(datas)
    print(datas[:10])
    # ====================
    print("퀵 정렬 시간 측정:")
    copied = datas.copy()
    result = quick(copied)
    print("정렬결과:", result[0][:10])

    # =====================
    print("병합 정렬 시간 측정:")
    copied = datas.copy()
    result = merge_sort2(copied)
    print("정렬결과:", result[0][:10])

    # =======================
    print("힙 정렬 시간 측정:")
    copied = datas.copy()
    result = heap_sort(copied)
    print("정렬결과:", result[0][:10])
