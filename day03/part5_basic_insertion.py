# part5_basic_insertion.py
# 삽입 정렬
# 삽입 정렬은 0번째 요소를 정렬된 상태로 취급하고
# 이후에 등장하는 요소들을 정렬된 요소들과 일일이 비교하여
# 더 작으면 작은 인덱스의 요소와 비교하고
# 만약 비교하고 있는 정렬된 요소보다 값이 크다면 
# 해당 위치에 값을 저장한다.(정착)
from part3_basic_bubble import clock

# insertion_sort(datas)->list:
@clock
def insertion_sort(datas:list)->list:
	# 요소의 개수 추출
	n = len(datas)

	# 전체 패스 구성
	# 0번째 요소는 비교를 위해서 정렬된 것으로 취급해야 하므로
	# 전체 반복은 1번째 요소부터 시작해야 한다.
	for i in range(1, n):
		print(f"{i+1}/{n}")
		# 정렬되지 않은 요소 중 첫번째 요소, 즉 i번째 요소를
		# 현재 삽입할 숫자로 정한다. -> key
		key = datas[i]
		# 현재 숫자의 이전 위치
		# 정렬된 마지막 요소의 인덱스
		j = i-1

		# 정렬된 데이터 중 현재 key의 값보다 큰 숫자를
		# 오른쪽으로 복사해 옮긴다.
		# 비교할 요소의 인덱스j가 0보다 크거나 같고(존재하고)
		# key의 값이 해당 요소의 값보다 작다면
		# 복사해 옮기고 j의 인덱스를 1 감소시킨다.
		# 보고 있는 대상을 왼쪽 대상으로 바꾼다.
		while j >= 0 and key < datas[j]:
			datas[j+1] = datas[j]
			j -= 1 # 보고 있는 대상에 대한 시야를 왼쪽으로 옮긴다.
		# 반복문을 탈출했다면 해당 위치에 key 값을 삽입한다.
		datas[j+1] = key
	return datas

if __name__ == "__main__":
	import random as r
	datas = list(range(10000))
	r.shuffle(datas)

	insertion_sort(datas)
	# print(datas)
