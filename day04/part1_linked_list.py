# part1_linked_list.py
# 연결 리스트(Linked List)란
# 노드(Node)라는 객체에 data와 다음 노드를 가리키는 주소값을 저장하여
# 새로운 노드 데이터의 추가와 삭제, 삽입을 빠르고 효율적으로 수행할 수 있게 해주는
# 리스트의 초기버전이다.
# 기존의 프로그래밍 언어는 고정길이 배열을 사용했기 때문에
# 추가와 삭제가 쉽지 않았다. -> 가변길이 배열을 구현하기 위해
# 이러한 연결 리스트라는 개념이 등장했다.

# 1. 노드는 데이터를 저장할 변수와 다음 노드를 가리킬 주소값을 저장할 변수
# 두 가지가 필요하다.
# Node: self.data:int, self.next:Node
class Node:
	def __init__(self, data:int, next=None):
		self.data = data
		self.next:Node = next

# 노드들을 요소로 하는 연결 리스트 구현
# LinkedList: self.head:Node, (self.tail:Node)
class LinkedList:
	def __init__(self, head=None):
		self.head = head
		# self.tail = tail
	
	def __str__(self):
		return self.traversal()
	# 1. 추가
	# self.next가 None인 노드를 찾아서 그 주소값을 새로 만든 노드의 주소값으로
	# 설정하면 삽입이 완료된다.(append)
	# 1. data를 받아서 그 데이터를 self.data로 삼는 새로운 노드를 생성해
	# 삽입을 할 것이냐
	# 2. Node객체를 직접 전달받아서 마지막 .next에 저장할 것이냐.
	# append(self, data:int=None, new_node:Node=None)
	def append(self, data:int=None, new_node:Node=None):
		# 전달받은 data가 있다면 Node()에 전달하여 
		# 새로운 노드 객체를 생성한다
		# 전달받은 data가 없거나 None이라면 전달받은 new_node를
		# 추가할 노드로 삼는다.
		node = Node(data) if data is not None else new_node
		# 만약에 위에서 이렇게 만들어진 노드가 None이라면
		# data도 new_node도 입력하지 않은 것이므로
		# 경고문구를 출력하고 None을 반환하여 메서드를 종료한다.
		if node is None:
			print("data 혹은 new_node 중 하나는 입력해야 합니다.")
			return None

		# 위에서 무사히 노드가 생성되었다면 아래에서
		# self.head부터 시작하여 마지막 노드까지 순회하며
		# .next가 None인 노드를 찾아 .next의 값으로 node를 저장한다.

		# 1. self.head가 None인 경우
		if self.head is None:
			self.head = node
			return
		
		# 추가할 노드(A) 앞에 위치할 노드(B)를 찾기 위해서
		# B를 임시로 저장할 변수를 선언한다.
		current_node = self.head # self.head 노드를 첫번째 노드로 삼는다.

		# while문으로 .next가 None이 아니라면 계속 반복하여 다음 노드를 탐색한다.
		while current_node.next is not None:
			# .next가 비어있지 않다면 .next에 저장된 노드를
			# current_node에 저장하여 이를 반복한다.
			current_node = current_node.next
		
		# 여기까지 왔다면 current_node.next가 None일 것이다.
		# 즉, 위에서 새로 삽입하기로 했던 node를 current_node.next로 저장하면 된다.
		current_node.next = node
		return # 메서드 종료

	# 2. 순회
	# 데이터 저장된 위치를 도식화하는 코드
	# 1 -> 2 -> 3 -> 4
	# 리스트로 변환하여 반환
	# " -> ".join(map(str, datas))
	# traversal(self) -> str
	def traversal(self):
		# 1. self.head에서 시작하여 .data를 추출, 리스트로 저장한다.
		# 2. 저장된 해당 리스트를 " -> ".join()을 이용하여 도식화한다.
		# 3. 해당 문자열을 반환한다.

		# 0. 데이터를 담을 리스트를 선언한다.
		datas = list()

		# ? 만약 self.head가 None이라면? -> None 또는 "[]"
		if self.head is None: return "LinkedList[]"

		# 1. self.head를 current_node에 저장하여 순서대로 조회한다.
		current_node = self.head

		# 2. 반복문에서 반복적으로 노드를 순회하며 data를 datas에 추가한다.
		while True: # 무한 반복
			# 현재 노드의 data를 datas에 담는다.
			datas.append(current_node.data)
			# 다음 노드가 있는지 확인하고 없다면 반복문을 탈출한다.
			if current_node.next is None:
				break
			else: # 다음 노드가 있다면 다음 타자 등장
				current_node = current_node.next
		# print("datas: ", datas) # 데이터 추출 중간확인

		# 3. "".join을 이용하여 도식화된 문자열로 만든다.
		# [1, 2, 3]
		# 1 -> 2 -> 3
		result = " -> ".join(map(str, datas))

		return "LinkedList " + result # LinkedList 1 -> 2 -> 3

	# 3. 탐색
	# 연결 리스트에서 가장 먼저 만나는, 특정 데이터를 가진 노드를 반환
	# 순회를 하며 찾는 데이터가 없는 경우는, .next가 None이 나오도록
	# 데이터를 못 찾은 경우일 것이다.
	# search(self, data) -> Node
	def search(self, data:int) -> Node:
		# 반환할 찾은 노드를 담을 변수 선언
		result_node = None
		# self.head가 비어있다면 데이터가 아예 없는 것이므로
		# 조기종료한다.
		if self.head is None: return None

		# 현재 보고 있는 노드를 담을 변수 선언
		# 초기값은 self.head를 저장한다.
		current_node = self.head

		# 현재 보고 있는 노드가 None이 아니라면 무한반복
		# 다만, 찾는 데이터를 가진 노드를 발견하면 반복 종료
		while current_node is not None:
			# 만약에 current_node.data가 찾는 data와 같다면
			# 조기종료
			if current_node.data == data:
				break
			# 찾는 데이터를 가지지 않았다면 .next 노드를 current에 담는다.
			current_node = current_node.next

		# 만약 current_node가 None이라면
		if current_node is None: return None

		# 여기까지 왔다면 current_node의 data가 찾는 data라는 뜻이다.
		# current_node를 반환하면 끝난다.
		return current_node

	# 4. 삭제
	# 특정 데이터를 가진 노드를 찾아서 삭제
	# 


	# 5. 삽입
	# 특정 노드와 그 노드 다음 노드 사이에 새로운 노드를 삽입하는 동작
	# 특정 노드를 입력받아 동작한다.





if __name__ == "__main__":
	# 연결 리스트 객체 생성
	link = LinkedList()
	# 연결 리스트에 새로운 데이터를 추가해보자.
	link.append(data=3) # 값 직접 입력 방식
	print(link.head.data)
	# 데이터를 하나 더 추가(노드 방식)
	link.append(new_node=Node(13))
	print(link.head.next.data)
	# 더미 데이터 삽입
	for i in range(10, 15):
		link.append(data=i)

	# result = link.traversal()
	# print(result)
	print(link)

	print(link.search(10).next.data)