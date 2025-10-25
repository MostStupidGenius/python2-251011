# part1_sort_quick.py
# 퀵 정렬(quick sort)
# 퀵 정렬은 분할 알고리즘을 활용하는 고급 정렬 알고리즘 중 하나로
# 피벗(pivot)이라는 개념을 사용하여 기준을 잡은 뒤
# 그보다 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 정렬하여
# 더이상 분해할 수 없을 때까지 이를 반복한 뒤
# 해당 순서 그대로 병합(combine)하여 전체의 리스트를 정렬 하는
# 정렬 알고리즘이다.
# 1. 피벗(pivot) 2. 재귀함수

# 동작 순서
# 0. 기본케이스: 만약 전달받은 리스트의 길이가 1 이하이면 정렬할 것이 없으므로 그대로 반환한다.
# 1. 리스트에서 기준이 될 피벗(pivot) 값을 하나 고른다.(실존하는 요소여야 한다.)
# 2. 해당 피벗과 같은 그룹, 피벗보다 작은 그룹(left), 피벗보다 큰 그룹(right) 등
# 총 세 개의 그룹으로 나눈다.
# 3. 그렇게 나뉜 그룹 중 피벗그룹을 제외한 좌우 그룹을 재귀적으로
# 퀵정렬에 전달한다.
# 4. 좌우 그룹이 정렬된 결과를 피벗의 좌우에 연결하여 하나의 리스트로 합친다(combine)
# 5. 하나로 합친 결과 리스트를 반환한다.
# quick_sort(datas:list) -> list:
def quick_sort(datas:list, show:bool=False) -> list:
    # 0. 기본케이스:
    # 만약 전달받은 리스트의 길이가 1 이하이면 정렬할 것이 없으므로 그대로 반환한다.
    if len(datas) <= 1: return datas

    # 1. 리스트에서 기준이 될 피벗(pivot) 값을 하나 고른다.(실존하는 요소여야 한다.)
    # 전체 길이의 반절번째 요소(위치상 중간값)를 고른다
    # + 어떤 값을 고르든 상관없으나 가능하면 중앙값(median)을 고르는 것이 효율적이다.
    pivot = datas[len(datas) // 2]
    if show: print(pivot)
    # 2. 해당 피벗과 같은 그룹, 피벗보다 작은 그룹(left), 피벗보다 큰 그룹(right) 등
    # 총 세 개의 그룹으로 나눈다.
    left = [x for x in datas if x < pivot]
    middle = [x for x in datas if x == pivot]
    right = [x for x in datas if x > pivot]
    if show:
        print(f"divide:\n{left}\t{middle}\t{right}")
    # 3. 그렇게 나뉜 그룹 중 피벗그룹을 제외한 좌우 그룹을 재귀적으로 퀵정렬에 전달한다.
    sorted_left = quick_sort(left, show)
    sorted_right = quick_sort(right, show)
    # 4. 좌우 그룹이 정렬된 결과를 피벗의 좌우에 연결하여 하나의 리스트로 합친다(combine)
    result = sorted_left + middle + sorted_right
    # 5. 하나로 합친 결과 리스트를 반환한다.
    return result


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
    sorted = quick_sort(datas, True)
    print("=" * 50)
    # 정렬 완료 메시지
    print(f"정렬 완료:\n{sorted}\n")