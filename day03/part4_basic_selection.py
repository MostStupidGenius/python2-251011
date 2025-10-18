# part4_basic_selection.py
# 선택 정렬
# 전체 요소를 확인하여 가장 작은 값을 가진 요소의 인덱스를 추출한다.
# 가장 작은 값의 인덱스와 현재 바꾸려는 요소의 인덱스를 맞교환하여
# 가장 작은 값부터 순차적으로 쌓아나가는 방식이다.
# 버블정렬보다는 효율적이지만 여전히 대규모 데이터셋에서는 비효율적이다.

# 시간측정 함수를 임포트해온다.
from part3_basic_bubble import clock

# 특징: 추가적인 변수를 사용하지 않기 때문에 메모리 공간을 절약할 수 있다.
# 불안정정렬-> 같은 값을 가진 요소간의 순서가 유지되지 않는다.

# seletion_sort1(datas:list)->list
@clock
def selection_sort1(datas:list)->list:
	# 리스트의 길이 추출
	n = len(datas)
	for i in range(n):
		# 현재 위치를 최소값을 가진 인덱스로 일단 설정한다.
		min_idx = i
		# i+1번째 요소부터 끝까지 순회하며
		# 가장 작은 값을 가진 요소의 인덱스를 찾는다.
		for j in range(i+1, n):
			# 만약에 j번째 요소가 min_idx요소보다 작다면
			if datas[j] < datas[min_idx]:
				# 최소값 인덱스를 j로 설정
				min_idx = j
		# 현재 위치의 원소와 찾은 최소값의 위치를 맞교환
		datas[i], datas[min_idx] = datas[min_idx], datas[i]
	return datas

if __name__ == "__main__":
	import random as r
	datas = list(range(10000))
	r.shuffle(datas)

	times = list()
	# 정렬 시작
	# for i in range(10):
	# 	time = selection_sort1(datas)
	# 	times.append(time)
	# avg = sum(times)/len(times)
	# print(f"{avg:.2f}")
	selection_sort1(datas)
	# 정렬 후 데이터 확인
	# print(datas)