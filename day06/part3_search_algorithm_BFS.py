# part3_search_algorithm_BFS.py
# 너비우선탐색(Breadth-First Search) 알고리즘
# 시작지점으로부터 목적지까지의 최단거리를 확인하고 할 때 사용하는 탐색 알고리즘이다.
# 가까운 지점부터 먼 곳까지 순차적으로 모든 곳을 방문하는 방식을 취한다.
# 미로의 지도를 그릴 때도 사용하는 것은 모든 곳을 방문한다는 성질을 이용하는 것이다.
# 너비우선탐색은 큐 자료구조를 사용하여 이진트리를 기준으로 생각했을 때,
# 같은 레벨을 먼저 탐색한다는 성질을 가진다.

# BFS_algorithm(graph:dict, start:str) -> None:
def BFS_algorithm(graph:dict, start:str) -> None:
    """
    너비우선탐색 함수
    큐 자료구조를 활용하여 가까운 노드부터 방문, 모든 노드를 탐색하는 알고리즘이다.
    Args:
        graph(dict): 그래프를 파이썬의 딕셔너리 자료구조로 표현해놓은 그래프
        start(str): 그래프에서 탐색의 시작점을 딕셔너리의 키값으로 전달받는 매개변수
    """
    # 방문한 노드들을 기록해놓은 변수 선언
    visited = set()
    # 시작노드를 포함한 큐 생성
    queue = [start]

    # 시작노드를 방문처리
    visited.add(start)

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 가장 왼쪽 노드를 꺼냄(선입선출)
        vertex = queue.pop(0)
        # 현재 방문중인 노드 출력
        print(vertex, end=" ")

        # 현재 노드의 이웃 노드들을 순회하기 전에, 방문했는지 여부를 검사
        not_visited = [e for e in graph[vertex] if e not in visited]
        # 만약 주변 이웃이 모두 방문한 상태라면, 다음 반복으로 이동(조기종료와 비슷)
        if len(not_visited) == 0: continue

        for neighbor in not_visited:
            # 방문 예정 처리
            visited.add(neighbor)
            # 큐에 추가
            queue.append(neighbor)

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['A', 'D'],
        'D': ['C']
    }
    target = 'C'
    BFS_algorithm(graph, target) # C A D B