# part2_binary_tree.py
# 이진트리(Binary Tree)란
# 기본적으로 연결리스트와 같이 노드와 이를 관리하는 자료구조로 이루어져 있다.
# 그런데 연결 리스트와 다른 점은 연결 리스트는 선형구조인 반면
# 이진트리는 비선형구조라는 점이다.
# 비선형 구조란, 모든 데이터를 조회하기 위해서 한쪽 방향으로만 나아가서는
# 안 되는 구조를 가리킨다.
# 노드로부터 좌우 노드를 가리키는 속성이 존재한다.
# self.data: 저장할 데이터
# self.left: 왼쪽 노드를 가리키는 변수
# self.right: 오른쪽 노드를 가리키는 변수

# Node
class Node:
	def __init__(self, data:int):
		self.data = data
		self.left = None
		self.right = None
	
# 이진 트리 자료구조
# 자식 노드를 최대 2개까지만 보유할 수 있는 노드로 이루어진
# 트리 구조다.
# Binary_tree: self.root
class Binary_tree:
	def __init__(self, root:Node=None):
		# 이진 트리 구조의 시작점을 담당할 루트 노드만 설정된다.
		self.root = root

	# 노드 추가(append)
	# append(self, data:int=None, node:Node) -> bool
	def append(self, data:int=None, node:Node=None) -> bool:
		# 추가할 노드를 구성
		new_node = Node(data) if data is not None else node
		if new_node is None: # data도 Node도 입력하지 않은 경우
			return False # 실패 처리
		# self.root가 None인 경우, self.root를 새로운 노드로 설정한다.
		if self.root is None:
			self.root = new_node
			return True

		# 현재 확인하고 있는 노드를 담을 변수 선언
		current_node = self.root

		# 반복문으로 좌우 자식을 모두 검사한다.
		# * 이때 검사할 노드를 리스트에 담아서 Queue 자료구조 방식으로
		# 순차적으로 검사한다.
		queue = [self.root]

		while queue: # queue에 요소가 남아있는 동안 무한히 반복
			# 큐에 담긴 첫번째 요소를 추출하여 검사를 진행한다.
			current_node = queue.pop(0)
			# current_node를 활용하여 좌우 자식을 추출해
			# queue에 담는다.
			# 이때 좌우 자식이 None이 아닌지 검사한다.
			if current_node.left is None:
				current_node.left = new_node
				return True
			elif current_node.right is None:
				current_node.right = new_node
				return True
			else: # 좌우 자식 모두 None이 아닌 경우
				# 해당 자식노드의 자식노드를 검사해야 한다.
				# 검사 목록에 현재 좌우 노드를 추가한다.
				queue.append(current_node.left)
				queue.append(current_node.right)
	# 순회(order)
	# 이진트리에서 데이터를 순회하며 출력하는 방식은 총 세 가지가 존재한다.
	# 이 방법에서 출력하는 데이터의 기준은 부모노드를 언제 출력하는가에 있다.
	# 1. 전위순회(pre-): 자식노드를 출력하기 전에 부모노드의 데이터를 먼저 출력한다.
	# 2. 중위순회(in-): 자식노드 중 왼쪽 자식을 먼저 순회한 뒤 오른쪽 자식을 순회하기 전에
	# 부모노드의 데이터를 출력한다.
	# 3. 후위순회(post-): 자식노드를 모두 순회한 뒤에 부모 노드를 출력한디.
	# 이러한 순회방식은 재귀적으로 호출되어 탐색하게 된다.
	# -> 재귀함수
	@staticmethod
	def preorder(node:Node):
		# 1. 재귀함수의 기본케이스
		# 재귀함수의 반복적인 자기호출을 중단시키기 위한 조건
		# 이러한 기본 케이스는 일반적으로 재귀함수의 첫부분에 작성된다.
		# 특정 조건을 만족하면 재귀함수를 호출하지 않고 그냥 반환된다.
		# 이 순회함수의 경우에는 전달받은 노드가 None이라면
		# 아무 동작도 하지 않고 함수가 종료된다.
		if node is None: return

		# 2. 재귀함수의 재귀 케이스
		# 재귀함수의 핵심으로, 자기자신을 호출하는 파트다.
		# 이때 무한재귀에 걸리지 않도록 계획적으로 함수를 꾸며야 한다.
		print(f"data: {node.data}")
		Binary_tree.preorder(node.left)
		Binary_tree.preorder(node.right)

	def inorder(node:Node):
		pass

	def postorder(node:Node):
		pass


if __name__ == "__main__":
	# 이진 트리 객체 인스턴스화
	tree = Binary_tree()
	# 더미 데이터 추가 (1 ~ 9)
	for i in range(1, 10):
		tree.append(i)
	
	# 루트로부터 좌우 자식을 직접 조회해보자.
	print("root: ", tree.root.data)
	left = tree.root.left
	right = tree.root.right
	print("root.left: ", left.data) # 2
	print("root.right: ", right.data) # 3

	print("left.left:", left.left.data) # 4
	print("left.right:", left.right.data) # 5
