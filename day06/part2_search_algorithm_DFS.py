# part2_search_algorithm_DFS.py
# 깊이 우선 탐색(Depth-First Search) 알고리즘
# 가장 멀리 있는 요소부터 탐색을 하는 알고리즘이다.
# 한쪽 방향으로 향하여 막다른 골목이 나오기 전까지 쭉 달리는 모양새를 취한다.
# 막다른 골목이 등장하면 가장 가까운 갈림길로 돌아가서 다른 길로 들어간다.
# 이때, 방문했는지 여부를 저장할 변수 저장공간이 필요하다.
# visited라는 변수를 활용하여 방문 여부를 저장할 것이다.
# 이러한 깊이우선탐색은 스택 자료구조를 기반으로 하여 구현되며
# 구현을 할 때에는 스택 방식과 스택 메모리를 활용하는 재귀함수 방식 등
# 두 가지 방식으로 구현할 수 있다.

# 스택 자료구조를 활용한 깊이우선탐색 함수
# DFS_stack(graph:dict, start:str) -> None:
def DFS_stack(graph:dict, start:str) -> None:
    """
    깊이우선탐색 알고리즘을 스택 자료구조를 활용하여 구현하는 함수
    목적지 키값없이 모든 요소를 순회하면서 데이터를 출력하는 방식으로 진행
    Args:
        graph(dict): 그래프를 딕셔너리 데이터 구조로 전달받는다.
        start(str): 그래프의 키값 중 시작점의 키값을 전달받는다.

    Retruns:
        None: 출력만 하고 반환값은 없다.
    """
    # 방문한 노드를 저장할 변수 선언 및 정의
    visited = set()

    # 시작노드를 스택에 추가
    stack = [start]

    # 스택이 비어있지 않은 동안 무한 반복
    while stack: # 리스트가 비면 반복을 멈춘다.
        # 스택에서 노드(정점:vertex)를 꺼낸다.
        vertex = stack.pop()
        # 해당 정점이 visited에 등록되어 있는지 묻는다.
        if vertex not in visited: # 만약 해당 정점이 visited에 있지 않다면
            # 방문에 해당 정점을 추가
            visited.add(vertex)
            # 방문했으니 출력해준다.
            print(vertex, end=" ")

            # 현재 정점의 이웃정점들을 스택에 추가
            # 방문한 적 없는 이웃들을 임시변수에 담는다.
            not_visited = [e for e in graph[vertex] if e not in visited]
            stack.extend(not_visited)
    # 스택이 비면 여기로 도달.
    # 따로 무언가 행동을 하지는 않는다.
    print("출력끝")
    return

# DFS를 재귀함수를 활용하여 구현하는 함수
# DFS_recursive(graph:dict, start:str) -> None:
def DFS_recursive(graph:dict, start:str, visited:set=None) -> None:
    # visited를 전달받는 이유는, 재귀적으로 호출할 때 방문일지를 다른 재귀함수에게
    # 전달하기 위함이다.
    # visited가 None이라는 것은 재귀함수가 시작되기 전이라는 의미이므로
    # 새로 set 자료형을 넣어준다.
    if visited is None:
        visited = set()
    
    # 현재 노드(정점)을 방문 처리
    visited.add(start)
    # 출력
    print(start, end=" ")

    # 이웃한 노드들 중 방문하지 않은 노드를 추출
    not_visited_neighbor = [e for e in graph[start] if e not in visited]

    # 기본케이스
    # 만약에 이웃한 노드 중 단 하나도 방문한 적이 없는 노드가 없다면
    # 이 경우 조기 종료한다.
    if not not_visited_neighbor: return

    # 재귀케이스
    # 현재 노드의 방문하지 않은 이웃 노드들을 탐색
    for neighbor in reversed(not_visited_neighbor):
        DFS_recursive(graph, neighbor, visited)

"""
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C']
}
"""
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['A', 'D'],
        'D': ['C']
    }
    target = 'D'
    DFS_stack(graph, target)
    DFS_recursive(graph, target)