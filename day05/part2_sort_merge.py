# part2_sort_merge.py
# 병합 정렬(merge sort)
# 병합 정렬은 나눌 때는 단순하게, 병합할 때 정렬하기
# 이를 기초로 삼는 정렬 알고리즘이다.
# divide 과정에서는 단순히 전체를 반으로 쪼개듯이 나누고
# 더이상 쪼갤 수 없을 때 combine을 하면서 정렬을 진행하는 방식이다.
# 때문에, 전체 프로세스와 재귀함수를 담당하는 함수가 있으며
# 병합하는 함수를 따로 만들어 병합과정을 진행한다.

# 병합정렬 함수
# merge_sort(datas:list, show:bool=False) -> list:
def merge_sort(datas:list, show:bool=False) -> list:
    # 재귀함수이기 때문에 기본 케이스와 재귀 케이스를 나눠 생각한다.
    # 1. 기본 케이스
    # 전달받은 데이터의 길이가 1이하이면 정렬할 필요가 없으므로 그대로 반환한다.
    if len(datas) <= 1: return datas

    # 2. 재귀케이스
    # 2-1. 좌우 서브리스트로 쪼갠다. 이때 중앙인덱스를 기준으로 삼는다.
    # + 파이썬의 경우 슬라이싱 기능으로 쉽게 나눌 수 있다.
    mid_index = len(datas) // 2
    left = datas[:mid_index]
    right = datas[mid_index:]
    # 2-2. 좌우 서브리스트를 재귀적으로 병합정렬 함수에 전달하여
    # 정렬을 진행한다.
    sorted_left = merge_sort(left, show)
    sorted_right = merge_sort(right, show)
    if show: print(f"{sorted_left}\t{sorted_right}")
    
    # 3. 정렬된 좌우 서브 리스트를 병합한다.
    sorted_list = merge(sorted_left, sorted_right, show)
    if show: print(f"{sorted_list}")

    # 4. 정렬된 최종 리스트를 반환한다.
    return sorted_list

# 병합 함수
# merge(left:list, right:list, show:bool=False)
def merge(left:list, right:list, show:bool=False) -> list:
    # 반환할 리스트를 선언한다.
    # 이때 반환될 리스트의 요소 개수는
    # 전달받은 좌우서브리스트 요소 개수의 합과 같다.
    result = list() # or []

    # 좌우 리스트에서 현재 검사받고 있는 요소의 인덱스를 가리킬 변수 선언
    left_index, right_index = 0, 0

    # 두 리스트의 현재 인덱스의 값끼리 크기를 비교하여 
    # 더 작은 값이 result에 추가되어야 한다.
    # 이때 검사하는 인덱스의 크기는 각 리스트의 길이를 넘을 수 없다.
    while left_index < len(left) and right_index < len(right):
        # 만약 왼쪽 리스트의 현재 인덱스 요소가
        # 오른쪽 리스트의 현재 인덱스 요소보다 작거나 같다면
        if left[left_index] <= right[right_index]:
            # 해당 왼쪽 요소의 값을 result에 추가하고
            result.append(left[left_index])
            # 왼쪽 현재 인덱스를 1 증가시켜 다음 인덱스를 가리키게 한다.
            left_index += 1
        else:
            # 해당 오른쪽 요소의 값을 result에 추가하고
            result.append(right[right_index])
            # 오른쪽 현재 인덱스를 1 증가시켜 다음 인덱스를 가리키게 한다.
            right_index += 1
    # while문 탈출
    # left_index 혹은 right_index 중 하나라도 해당 리스트의 길이를 넘어갔다면
    # 반복문을 탈출한다.
    # 이때, 넘어가지 않은 쪽의 인덱스가 요소가 남았다면
    # 그 남은 요소를 result에 추가해주어야 한다.
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

my_sort = merge_sort

if __name__ == "__main__":
    # 요소 섞기를 위한 임포트
    import random as r
    # 더미데이터 생성
    datas = list(range(10))
    # 더미데이터 섞기
    r.shuffle(datas)
    # 안내 출력
    print(f"원본:\n{datas}\n")
    print("=" * 50)
    # 정렬 시작
    sorted = my_sort(datas, True)
    print("=" * 50)
    # 정렬 완료 메시지
    print(f"정렬 완료:\n{sorted}\n")