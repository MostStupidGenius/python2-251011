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
	def __init__(self, data:int, next):
		self.data = data
		self.next:Node = next

# 노드들을 요소로 하는 연결 리스트 구현
# LinkedList: self.head:Node, (self.tail:Node)
class LinkedList:
	def __init__(self, head=None):
		self.head = head
		# self.tail = tail
	# 추가
	# self.next가 None인 노드를 찾아서 그 주소값을 새로 만든 노드의 주소값으로
	# 설정하면 삽입이 완료된다.(append)
	# 1. data를 받아서 그 데이터를 self.data로 삼는 새로운 노드를 생성해
	# 삽입을 할 것이냐
	# 2. Node객체를 직접 전달받아서 마지막 .next에 저장할 것이냐.

	# 삽입
	# 특정 노드와 그 노드 다음 노드 사이에 새로운 노드를 삽입하는 동작
	# 특정 노드를 입력받아 동작한다.

	# 삭제

	# 탐색

	# 순회

