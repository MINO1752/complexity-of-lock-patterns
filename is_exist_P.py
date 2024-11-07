# 건너뛰기 규칙: 특정 점을 건너뛰기 위해 지나야 하는 점을 정의
skip = {
    (1, 3): 2, (1, 7): 4, (1, 9): 5, (2, 8): 5, (3, 7): 5, 
    (3, 9): 6, (4, 6): 5, (7, 9): 8
}

def is_exist_pattern(pattern):
    # 모든 이웃하는 점들에 대해:
    for i, point in enumerate(pattern[:-1]):  # 마지막 점은 이웃이 없으므로 제외
        next_point = pattern[i + 1]
        
        if (point, next_point) in skip:  # 만약 건너뛰기 경로를 사용한다면:
            required = skip[(point, next_point)]  # 건너뛰기 규칙에 해당하는 점
            if required not in pattern[:i]:  # 만약 건너뛰기 규칙을 만족하지 못했다면:
                return False  # False를 반환
        if (next_point, point) in skip:  # 만약 건너뛰기 경로를 사용한다면:
            required = skip[(next_point, point)]  # 건너뛰기 규칙에 해당하는 점
            if required not in pattern[:i]:  # 만약 건너뛰기 규칙을 만족하지 못했다면:
                return False  # False를 반환

    # 모든 건너뛰기 규칙을 만족했으면 True 반환
    return True

# 예시 잠금 패턴
# pattern = [6, 4, 3, 9, 1, 7, 5]
# print(is_exist_pattern(pattern))