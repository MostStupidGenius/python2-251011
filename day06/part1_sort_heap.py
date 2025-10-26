# part1_sort_heap.py
# 최대힙 클래스 가져오기

# day05 폴더는 현재 day06/par1_sort_heap.py가 있는 폴더와 다른 폴더다
# 모듈을 불러오는 시작점을 부모폴더로 지정해야 한다.
import sys
import os

# 현재 파일의 경로를 추출 -> __file__
# 부모폴더의 경로를 추출 -> os.path.dirname(경로)
workspace_path = os.path.dirname(os.path.dirname(__file__))
print(workspace_path) # d:\python2_0930_ljs_2510\workspace

# sys 모듈을 이용하여 시스템 환경변수에 등록한다.
sys.path.append(workspace_path)

# d:\python2_0930_ljs_2510\workspace 안의 day05에 접근할 수 있게 된다.
from day05.part3_heap import MaxHeap

# 기존에 만들었던 MaxHeap 클래스를 부모클래스로 하여 기능을 확장해보자.
# 이때, 기존에 만들었던 메서드를 재활용하는 경우엔 작성할 필요가 없고
# 재정의하는 경우엔 상속받은메서드임을 작성하는 것이 좋다.
class MaxHeap2(MaxHeap):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        return super().insert(value)

    def extract_max(self):
        return super().extract_max()
    
    def _heapify_up(self, index):
        return super()._heapify_up(index)
    
    def _heapify_down(self, index):
        return super()._heapify_down(index)

    # 부모노드의 인덱스를 반환하는 단순함수
    @staticmethod
    def parent(i):
        return (i - 1) // 2

    # 왼쪽 자식의 인덱스를 반환하는 단순함수
    @staticmethod
    def left_child(i):
        return i * 2 + 1
    
    # 오른쪽 자식의 인덱스를 반환하는 단순함수
    @staticmethod
    def right_child(i):
        return i * 2 + 2
    
    # 부모노드를 가지고 있는지 여부(bool)를 반환하는 단순함수
    # has_parent(self, i) -> bool: # self를 받는 이유는 다른 메서드를 활용하기 위해서
    @staticmethod
    def has_parent(i) -> bool:
        return MaxHeap2.parent(i) >= 0
    
    # 왼쪽자식이 있는지 여부
    @staticmethod
    def has_left_child(self, i):
        return MaxHeap2.left_child(i) < len(self.heap)
    
    # 오른쪽 자식이 있는지 여부
    @staticmethod
    def has_right_child(self, i):
        return MaxHeap2.right_child(i) < len(self.heap)


if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(3)
    heap.insert(4)
    heap.insert(7)
    print(heap.heap) # 7 3 4
    pass