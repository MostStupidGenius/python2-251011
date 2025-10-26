# part3_heap.py
# 힙 구조(heap structure)
# 힙 구조는 완전 이진 트리를 기반으로, 부모노드의 값과 자식노드의 값을 비교하여
# 상하관계를 유지하는 자료구조를 가리킨다.
# 이때 부모노드의 값이 자식노드의 값보다 크게 유지하는 것을
# 최대heap 속성이라고 하며, 반대는 최소heap이라고 부른다.
# 비교 대상은 항상 부모노드이며, 형제노드(같은 부모를 가진 노드)나
# 부모의 형제노드와는 비교하지 않는다.

# 최대힙 속성을 만족하는 힙 구조를 만들고 나면
# 루트노드의 값은 전체 리스트의 데이터 중 가장 큰 값이 위치하게 된다.

# 최대힙 구조를 구성하는 클래스 정의
class MaxHeap:
    def __init__(self):
        self.heap = list()

    # 삽입 연산
    # insert(self, value) -> None:
    def insert(self, value) -> None:
        # 1. 힙 구조의 마지막 요소로 데이터 추가
        self.heap.append(value)
        # 2. 추가된 값이 힙 속성을 만족하지 못하게 만들 수 있으므로
        # 힙속성을 유지하기 위한 heapify함수를 호출한다.
        self._heapify_up(len(self.heap) - 1)

        # 체이닝 기법(chaining method)
        # 반환값을 self로 하면 사용하는 쪽에서 연쇄적으로 메서드를 사용할 수 있다.
        return self
    
    # 힙속성 만족을 위한 상향조정 함수
    # _heapify_up(self, index) -> None:
    def _heapify_up(self, index) -> None:
        # 재귀함수로, 힙속성을 만족할 때까지 부모노드를 타고 올라간다.
        # 재귀케이스
        # 부모노드와 값을 비교하여 재귀적으로 타고 올라가며
        # 힙속성 유지를 위해 더 큰 값이 위에 위치하도록
        # 자리를 맞바꾸는 동작을 한다.

        # 만약에 현재 인덱스의 값이 부모노드의 값보다 크다면
        # if self.heap[index] > 부모노드의 값
        # + 부모노드가 존재하면서.
        current_data = self.heap[index]
        parent_index = (index - 1) // 2
        parent_data = self.heap[parent_index]
        if (index - 1) // 2 >= 0 and current_data > parent_data:
            # 맞바꾼다.
            self.heap[index], self.heap[parent_index] = \
                parent_data, current_data
            # 이를 재귀적으로 상향 조정
            self._heapify_up(parent_index)

        # 기본케이스
        # 아무 동작을 취하지 않는다.
        else:
            pass

    # 삭제 연산
    # 최대값을 추출하는 연산 => 힙 구조에서의 0번째 요소를 추출
    # extract_max(self) -> int:
    def extract_max(self) -> int|None:
        # 힙 구조의 길이가 0이라면
        if len(self.heap) == 0: return None

        # 1. 힙 구조에서 가장 큰 값인 0번째 요소의 값을 저장
        max_value = self.heap[0]
        # 2. 마지막 요소(가장 작은 값들 중 하나)를 루트 노드로 이동
        self.heap[0] = self.heap[-1]
        # 2-1. 마지막 요소를 제거하여 힙 구조의 크기를 1 줄인다.
        self.heap.pop()

        # 3. 힙속성을 만족할 때까지 하향 조정
        if len(self.heap) > 0:
            self._heapify_down(0)
        
        # 4. 아까 추출해둔 가장 큰 값을 반환
        return max_value
    
    def _heapify_down(self, index) -> None:
        # 1. 가장 큰 값의 인덱스를 전달받은 인덱스로 일단 취급한다.
        largest_index = index
        left_index = index * 2 + 1
        right_index = left_index + 1
        # 2. 왼쪽 자식과 비교하여 왼쪽 자식이 더 큰 경우 largest를 바꿔준다.
        if left_index < len(self.heap) and self.heap[left_index] > self.heap[largest_index]:
            largest_index = left_index

        # 3. 병렬적으로 오른쪽 자식과도 비교하여 같은 동작을 수행한다.
        if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        # 4. 위 과정을 거쳤다면 부모노드(index)와 자식노드들(left,right) 중 가장 큰 값을 가진 노드의
        # 인덱스가 largest에 담겼을 것이다.
        # largest 인덱스의 값과 부모노드의 값을 맞바꾸어 힙 속성을 유지한다.
        # 이때 부모노드의 값이 더 작았다면 아래로 조정되므로 하향조정이라고 부르는 것이다.
        
        # 5. 교환이 필요한 경우
        # largest의 초기값이 index였으므로 그 값이 서로 다르다면 
        # 더 큰 값을 가진 자식 노드가 있다는 의미가 된다.
        if largest_index != index:
            self.heap[index], self.heap[largest_index] =\
                self.heap[largest_index], self.heap[index]
            # 하향조정이 된 경우에 한해서 재귀적으로 하향조정 실행
            # largest에 해당하는 인덱스는 하향조정된 index이므로
            # 다음 heapify에서는 또 자식노드와 비교를 하게 된다.
            self._heapify_down(largest_index)

if __name__ == "__main__":
    # 힙 구조 인스턴스화
    heap = MaxHeap()

    # 데이터 추가
    heap.insert(7)
    heap.insert(4)
    heap.insert(6)
    print(heap.heap) # 7, 4, 6
    # 기존 힙 구조에서 가장 큰 값이 7인데
    heap.insert(8) # 그보다 큰 값이 들어왔을 때
    # 데이터리스트를 출력해보면 0번째 값이 가장 큰값인지 확인해보자.
    print(heap.heap) # 8, 7, 6, 4

    # 데이터를 무작위 순서로 삽입해보자.
    dummy = list(range(10, 23))
    import random as r
    r.shuffle(dummy)
    for e in dummy:
        heap.insert(e)
    
    # 삽입된 값들이 힙속성을 유지하는지 확인
    print(f"datas: {heap.heap}")

    # 이를 이용한 간단한 힙정렬
    result = []
    # 반복문을 통해서 heap구조의 0번째 요소를 모든 요소를 소모할 때까지 추출해
    # result에 append한다.
    for i in range(len(heap.heap)):
        print(f"힙구조 {i}:\n\t{heap.heap}")
        result.insert(0, heap.extract_max())
        print(f"result:\n\t{result}")
    print(result)