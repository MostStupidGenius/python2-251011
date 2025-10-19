# part3_basic_bubble.py
# 기본 정렬 알고리즘: 버블 정렬
# 버블 정렬은 가장 구현하기 쉬운 정렬 알고리즘으로,
# 인접한 두 요소를 비교하여 맞교환하는 가장 쉬운 알고리즘이다.

# 데이터는 리스트 자료구조를 사용
# 인덱스를 이용하여 데이터를 식별하고 맞교환할 것이다.

# 실행시간 측정을 위한 데코레이터 함수 만들기
# clock(func, *args)->func
def clock(func, *args):
	import time
	# 내부 함수
	def wrapper(args):
		# 실행 전 시각 추출
		before = time.time()
		# 함수 실행
		func(args)
		# 함수 실행 후 시각 추출
		after = time.time()
		# 실행 후 시간에서 실행 전 시간을 빼면
		# 동작시간이 나온다.
		run_time = f"{after - before:.2f}"
		# :.2f는 소숫점 아래 2자리까지만 표시

		print(f"실행시간: {run_time}s")
		return after - before # 측정된 시간 반환
	return wrapper

# 데코레이터 함수는 타겟 함수보다 먼저 정의되어야 한다.

# 버블 정렬 기본 함수
@clock
def bubble_sort1(datas:list):
	# 인덱스 접근을 위해 전체 길이를 추출해야 한다.
	n = len(datas)

	# 전체 요소의 개수만큼 반복을 진행한다.
	# 이때 외부 for문은 몇 개나 정렬이 완료되었는지를 알 수 있게 해준다.
	for i in range(n):
		print(f"{i+1}/{n}")
		# 개수가 10개인 경우 0부터 9까지 반복
		# 외부 for문의 각 반복은 패스(path)라고 불린다.
		# 내부 for문
		# j번째 요소와 j+1번째 요소를 비교하여 순서가 잘못되어 있으면
		# 둘을 맞교환한다.
		for j in range(n-1):
			# 인접한 두 요소를 비교하여 순서가 잘못되어 있으면 교환
			# [3, 1, 2, 4]
			if datas[j] > datas[j+1]:
				# 두 인접 요소를 맞교환
				datas[j], datas[j+1] = datas[j+1], datas[j]
				# 교환이 일어났으므로 다음 반복으로 이동
				# continue
	return datas

# 최적화가 적용된 버블 정렬
# 버블 정렬에서 마지막부분부터 path 횟수 만큼은 정렬된 데이터다.
# 즉, 확인할 필요가 없는 데이터이므로 길이에 따라 정렬대상에서 제외 시킨다.
@clock
def bubble_sort2(datas:list):
	n = len(datas)
	# 한번이라도 교환이 이루어졌다면
	# 아직 완전히 정렬된 것이 아니다.
	# 교환여부를 체크하기 위한 변수 선언
	swapped = False # 각 패스마다 초기화하고, 교환이 이루어진 경우
	# True로 바꾼다.
	# 각 패스가 끝났을 때 이 변수의 값을 확인하여 조기종료 여부를 결정한다.
	count = 0
	for i in range(n):
		print(f"{i+1}/{n}")
		count += 1
		# 한 path가 종료될 때마다 마지막 요소로부터 i개 요소는
		# 정렬된 것으로 취급한다.
		# 때문에 내부for문에서 마지막 i개 요소는 확인하지 않는다.
		for j in range(n-1-i): # 이를 위해 i를 빼준다.
			if datas[j] > datas[j+1]:
				datas[j], datas[j+1] = datas[j+1], datas[j]
				# 교환이 이루어졌으므로 swapped를 True로 바꿔준다.
				swapped = True
			
		# 외부 for문에서 swapped를 검사하여
		# 이번 패스에서 교환이 한번도 이루어지지 않았다면
		# 모두 정렬된 것으로 취급하여 정렬을 조기종료한다.
		if swapped is False:
			break # 외부 for문 탈출
	print(count)
	return datas # 굳이 반환할 필요는 없지만 마무리해준다.

if __name__ == "__main__":
	# 데이터를 섞기 위한 랜덤 라이브러리 임포트
	import random as r
	
	# 순차 데이터 생성
	datas = list(range(10000))
	# 리스트 형태의 데이터를 셔플(섞기)
	r.shuffle(datas)
	# 정렬 전 데이터 출력
	# print(datas)
	# 두 개 정렬에 사용되는 데이터가 같으면 실험이 안 되므로
	# 복사를 통해서 각각 실행시간을 측정한다.
	# sort1_time = bubble_sort1(datas.copy())
	sort2_time = bubble_sort2(datas.copy())
	# print(f"{sort1_time/sort2_time * 100:.2f}%")
	# print(datas)