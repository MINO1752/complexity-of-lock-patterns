# 건너뛰기 규칙: 특정 점을 건너뛰기 위해 지나야 하는 점을 정의
skip = {
    (1, 3): 2, (1, 7): 4, (1, 9): 5, (2, 8): 5, (3, 7): 5, 
    (3, 9): 6, (4, 6): 5, (7, 9): 8
}

def filter_connections(pattern):
    # 각 점에 대한 연결 정보를 저장할 사전, 집합(set)으로 중복 제거
    connections = {p: set() for p in pattern}
    
    # 패턴 내에서 직접 이웃하는 점들만 기본 연결로 추가
    for i in range(len(pattern) - 1):
        point = pattern[i]
        next_point = pattern[i + 1]
        connections[point].add(next_point)
        connections[next_point].add(point)
        
        # 건너뛰기 규칙에 따라 연결 추가
        if (point, next_point) in skip:
            required = skip[(point, next_point)]
            # 필요한 점이 패턴에 있는 경우 연결 추가
            if required in pattern:
                connections[point].add(required)
                connections[next_point].add(required)
                connections[required].add(point)
                connections[required].add(next_point)
        elif (next_point, point) in skip:
            required = skip[(next_point, point)]
            if required in pattern:
                connections[point].add(required)
                connections[next_point].add(required)
                connections[required].add(next_point)
                connections[required].add(point)
    
    # 집합을 리스트로 변환하여 반환
    return {k: list(v) for k, v in connections.items()}

def calculate_complexity(pattern):
    connections = filter_connections(pattern)  # 필터링된 연결 구성
    visited_paths = []  # 가능한 모든 경로를 저장할 리스트

    def dfs(current, visited):
        # 더 진행할 경로가 없는 경우, 현재 경로를 기록
        if all(item in visited for item in connections[current]):
            visited_paths.append(list(visited))
            return 1  # 경로 하나를 완성했으므로 1을 반환
        
        count = 0
        for next_point in connections[current]:
            if next_point not in visited:
                # 스킵 경로 확인: 중간 점을 거치지 않은 스킵 경로는 탐색하지 않음
                if (current, next_point) in skip:
                    required = skip[(current, next_point)]
                    if required not in visited:
                        continue
                elif (next_point, current) in skip:
                    required = skip[(next_point, current)]
                    if required not in visited:
                        continue

                # 다음 점을 방문하고 DFS 호출
                count += dfs(next_point, visited + [next_point])
        return count
    
    # 첫 번째 점부터 시작하여 모든 경로 탐색
    total_paths = 0
    for start_point in pattern:
        total_paths += dfs(start_point, [start_point])
    
    # 복잡도 수치(총 가능한 경로 수)와 각 경로 출력
    # print("가능한 경로들:")
    # for path in visited_paths:
    #    print(" -> ".join(map(str, path)))
    
    return total_paths

# 예시 잠금 패턴
# pattern = [5, 7, 3, 8, 2, 9, 1, 6, 4]
# complexity = calculate_complexity(pattern)

# print("\n총 가능한 경로 수 (복잡도):", complexity)



