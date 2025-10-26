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
    
    def _heapify_up(self, index) -> None:
        # 만약에 현재 인덱스(index)가 루트노드 인덱스라면
        # 부모노드 인덱스가 없을 것이다.
        if not MaxHeap2.has_parent(index):
            # 부모노드가 없는 경우, 조기 종료
            return
        current_data = self.heap[index]
        parent_index = MaxHeap2.parent(index)
        parent_data = self.heap[parent_index]
        if current_data > parent_data:
            self.heap[index], self.heap[parent_index] = \
                parent_data, current_data
            self._heapify_up(parent_index)

    def _heapify_down(self, index) -> None:
        largest_index = index
        left_index = MaxHeap2.left_child(index)
        right_index = MaxHeap2.right_child(index)
        if left_index < len(self.heap) and self.heap[left_index] > self.heap[largest_index]:
            largest_index = left_index

        if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index
    
        if largest_index != index:
            self.heap[index], self.heap[largest_index] =\
                self.heap[largest_index], self.heap[index]
            self._heapify_down(largest_index)

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

    # 가장 큰 값(루트노드의 값)을 제거하지 않고 확인하는 메서드
    def peek(self):
        return self.heap[0] if self.heap else None
    
    # 힙에 저장된 요소의 개수(힙 크기) 반환
    def size(self) -> int:
        """힙 크기 반환"""
        return len(self.heap)
    
    # 힙이 비어있는지 여부
    def is_empty(self):
        """힙이 비어있는지 확인"""
        return len(self.heap) == 0 # 요소의 개수가 0개면 True 반환
    
    # 힙 구조 출력
    def print_heap(self):
        """힙 구조 출력"""
        # print(f"MaxHeap2: {self.heap}")
        print(self.__str__())
        return 
    
    # 대표 문자열 반환
    def __str__(self):
        return f"MaxHeap2: {self.heap}"

if __name__ == "__main__":
    heap = MaxHeap2()
    heap.insert(3)
    heap.insert(4)
    heap.insert(7)
    print(heap) # 7 3 4
    heap.print_heap()

    heap.insert(10)\
        .insert(13)\
        .insert(8)
    
    print(heap)
    print(heap.peek())
    print(heap)

    