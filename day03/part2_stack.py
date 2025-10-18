# part2_stack.py
# 스택 자료구조
# 스택이란, 먼저 들어온 데이터가 아래쪽에 깔리는 구조로,
# 나중에 들어온(Last In) 데이터가 먼저 나가는(First Out) 자료구조를 가리킨다.

# 스택은 리스트의 append(): 마지막에 요소 추가하기
# pop(): 마지막 요소 추출하기
# 이렇게 두 가지 함수만 사용하면 된다.

class Stack:
	def __init__(self, head:int=None):
		self.datas = [head] if head is not None else list()
	
	# 데이터 삽입
	# append(self, 정수값)->self
	def append(self, data:int):
		# 만약에 입력받은 데이터가 int 타입이 아니라면
		if not isinstance(data, int):
			# 데이터를 삽입하지 않고 경고메시지를 출력한 뒤
			print("입력된 데이터가 정수가 아닙니다.")
			# None을 반환한다.
			return None
		# self.datas에 append를 통해서 data를 뒤에 붙인다.
		self.datas.append(data)
		return self

	# 추출 예정 데이터 확인
	# self.datas의 길이를 확인하여 1이상인 경우,
	# -1번째 요소를 반환한다.
	# 이때, pop을 사용하지 않음으로써 데이터가 그대로 남아있다.
	# next(self)->int
	def next(self)->int:
		result = None
		result = self.datas[-1] if len(self.datas) >= 1 else None
		return result

	# 데이터 추출
	# .pop()를 이용하여 마지막 요소를 추출한다.
	# -> -1번째 요소를 추출하되 요소가 없다면 기본값으로 None을 반환
	# pop(self)->int|None
	def pop(self)->int|None:
		result = None

		# pop 대신에 datas를 dict로 변환하여
		# get을 이용하여 요소를 추출해보자.
		# get(키값, 부재시 기본값)
		# get을 사용하면 [key]로 데이터를 접근했을 때와 달리
		# key값이 존재하지 않더라도 오류가 발생하지 않는다.
		my_dict = dict()
		for i, e in enumerate(self.datas):
			key = i - len(self.datas)
			my_dict[key] = e
		result = my_dict.get(-1, None)
		# 만약에 result의 값이 None이 아니라면
		# self.datas에서 key(index)가 -1인 요소를 제거한다.
		del self.datas[-1]
		return result

if __name__ == "__main__":
	s = Stack(1)
	s.append(2).append(3).append(4)
	print(s.datas) # 데이터 확인
	# 마지막에 들어온 요소를 확인
	print(s.next())

	# s.next()로 조회된 데이터를 추출할 것이다.
	print(s.pop())

	# 남은 데이터 확인
	print(s.datas)