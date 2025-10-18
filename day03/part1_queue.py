# part1_queue.py
# 큐 자료구조
# 큐 자료구조는 먼저 들어온 데이터가 먼저 나가는 그러한
# 구조를 가리킨다.
# list로 구현을 하는 경우, 새로운 데이터는 0번째에 삽입(insert)하고
# 먼저 들어온 데이터를 추출하는 것은 -1번째 요소를 추출하는
# pop()을 사용한다.
# 이를 Queue라는 클래스 이름으로 구현해보자.
class Queue: # 상속받는 클래스가 없다면 소괄호() 생략 가능
	def __init__(self, head:int=None):
		""" docstring
		head:int -> 정수형 데이터로 Queue의 리스트에서 첫번째 요소를
		가리킨다.
		head가 입력되었는지 여부에 따라 빈리스트로 할지 head의 값을 요소로 하는
		리스트를 만들지가 결정된다.
		"""
		# 실제로 데이터를 저장할 속성(객체의 변수)
		self.datas:list = list()
		# head를 입력받았다면 첫번째 요소로 head 값을 삽입한다.
		if head is not None: # head가 None이 아니라면
			# 값을 입력받은 것으로 취급하여
			self.datas.append(head) # 데이터에 값을 추가한다.
	
	# 데이터 삽입
	# enqueue(self, 정수값)
	def enqueue(self, data:int):
		# 0번째 요소에 데이터 삽입
		self.datas.insert(0, data)
		return self # 체이닝 기법

	# 데이터 추출
	# pop(self) -> int
	def pop(self) -> int:
		# 반환할 값을 담을 변수 선언
		result = None
		# self.datas에 요소가 있다면
		# 마지막(-1) 요소를 반환한다.
		if len(self.datas) > 0:
			result = self.datas.pop()
		# else: # 요소가 없다면
			# return None
		return result
	
	# 모든 데이터 나열 및 출력
	# self.datas에 있는 모든 요소를 한 줄로 출력한다.
	# 반환값은 None으로 고정한다.
	def print_all(self):
		print("Queue[", end="")
		# for e in self.datas:
		# 	print(f"{e}, ")
		# Queue[1, 2, 3, ]
		# -> 문제점: 마지막에 반점,과 공백이 대괄호 왼쪽에 들어가게 된다.

		# 문자열.join(이터)은 해당 이터러블 객체의 요소 사이에 문자열 구분자를
		# 삽입한 문자열을 반환한다. 
		print(", ".join(map(str, self.datas)), end="")
		print("]")

	# 문자열 표현(__str__)
	# str(Queue객체)를 사용했을 때 호출되는 매직메서드
	def __str__(self)->str:

		result:str = None
		string = map(str, self.datas)
		result = f"Queue[{", ".join(string)}]"
		return result

if __name__ == "__main__":
	q = Queue()
	q.enqueue(3)\
		.enqueue(5)\
		.enqueue(7)
	# 중간확인
	# print(q.datas) # [7, 5, 3]
	
	print(q.pop()) # 3
	# print(q.datas) # [7, 5]

	# 데이터 형태 출력
	q.print_all()

	# Queue 객체의 문자열 표현 출력하기
	print("datas: ", str(q))