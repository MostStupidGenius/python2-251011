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
	def search(self, data:int, before=False) -> Node|tuple[Node, Node]:
		# 반환할 찾은 노드를 담을 변수 선언
		result_node:Node = None
		before_node:Node = None
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

			# + before 매개변수가 True라면 이전 노드의 정보를 같이 반환해야 하므로
			# .next를 current에 담기 전에 current를 before_node에 담아준다.
			if before is True:
				before_node = current_node

			# 찾는 데이터를 가지지 않았다면 .next 노드를 current에 담는다.
			current_node = current_node.next

		# 만약 current_node가 None이라면
		if current_node is None and before is False:
			return None
		
		if current_node is None and before is True:
			return (None, None)

		# 여기까지 왔다면 current_node의 data가 찾는 data라는 뜻이다.
		# current_node를 반환하면 끝난다.
		return (before_node, current_node) if before is True else current_node

	# 4. 삭제
	# 특정 데이터를 가진 노드를 찾아서 삭제
	# search 메서드를 활용하여 조회한 데이터를 삭제할 것이다.
	# delete(self, data:int) -> bool
	def delete(self, data:int) -> bool:
		# 문제가 생겨서 삭제하지 못하면 False로 바꿔서 반환한다.
		# search 메서드를 이용하여 데이터를 조회
		before, current = self.search(data=data, before=True)

		# 조회한 노드가 None이라면 데이터를 찾지 못한 것이므로
		# False를 반환한다.
		if current is None: return False

		# 여기까지 내려왔다면 node에 담긴 것은 실제 노드 객체일 것이다.
		# 해당 노드를 삭제하려면 앞 노드의 next를 지우려는 node의 next로 바꿔줘야 한다.

		# 삭제하려는 노드 앞에 위치한 노드 정보가 필요해졌다.
		# why? 앞의 노드.next의 값을 삭제하려는 노드.next 객체 정보로 바꿔줘야 한다.

		# 만약 current 노드가 head라면 before 노드가 없을 수 있다(None) -> 처리 필요
		# print("before.data: ", before.data)
		# print("current.data: ", current.data)
		# 이때 head를 삭제하는 경우에는 self.head도 기존 head의 next로 바꿔주어야 한다.

		# 지우려는 데이터가 self.head가 가진 데이터라면
		# before 노드가 None이라면 self.head라고 볼 수 있다.
		if before is None:
			# self.head를 다음 노드로 저장
			self.head = self.head.next
			# 기존 head를 제거
			del current
			# 정상 제거 되었음을 반환
			return True
		
		# 만약 지우려는 데이터를 헤드가 아닌 노드가 가지고 있다면
		# next를 이전하는 작업을 해주어야 한다.
		# 지우려는 노드의 next 노드를 이전 노드의 next에 저장한다.
		before.next = current.next
		# 지우려는 노드를 지운다.
		del current
		return True

	# 5. 삽입
	# 특정 노드와 그 노드 다음 노드 사이에 새로운 노드를 삽입하는 동작
	# 특정 노드를 입력받아 동작한다.
	# search() 메서드의 before 변수를 활용하여 삽입하고자 하는 노드의 데이터를 기준으로
	# current 노드를 찾아서 before 노드와 current 노드 사이에 새로운 노드를 삽입한다.
	# insert(self, data:int, after_data:int)
	def insert(self, new_data:int, after_data:int):
		# search로 after_data를 가진 노드를 찾아서
		# after의 before 노드와 after 사이에 새로운 노드를 삽입한다.
		new_node = Node(new_data)
		# search로 before, after 노드를 찾는다.
		before, after = self.search(after_data, True)

		# 만약 before가 None이라면, after가 None인지도 검사해야 한다.
		# 이는 찾는 데이터가 없다는 의미이므로 None을 반환한다.
		if before is None and after is None: return None
		
		# before는 None인데 after는 None이 아니라면
		# after가 head라는 의미이므로
		if before is None and after is not None:
			new_node.next = after # 이 경우 after는 기존 head와 같은 객체다.
			self.head = new_node # head를 바꿔준다.
			return True # 정상 종료

		# new 노드의 next에 after 노드를 저장한다.
		new_node.next = after

		# before 노드의 next에 new 노드를 저장한다.
		before.next = new_node

		# 정상 종료
		return True

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

	link.delete(13)
	print(link) # 3 -> 10 -> 11 -> 12 -> 13 -> 14

	# link.insert(23, 12) # 중간에 삽입
	# print(link) # 3 -> 10 -> 11 -> 23 -> 12 -> 13 -> 14 
	link.insert(23, link.head.data) # head 앞에 추가
	print(link) # 23 -> 3 -> 10 -> 11 -> 12 -> 13 -> 14 

	link.insert(333, link.head.data) # head 앞에 추가
	print(link) # 333 -> 23 -> 3 -> 10 -> 11 -> 12 -> 13 -> 14 