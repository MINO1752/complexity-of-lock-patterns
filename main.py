import itertools
from is_exist_P import is_exist_pattern
from calc_C import calculate_complexity
from draw_P import draw_pattern

# n개의 점을 사용하는 모든 패턴 만들기(순열)
dots = list(range(1, 10))
raw_patterns = [list(p) for p in itertools.permutations(dots, 9)]

# 실제로 가능한 패턴들을 필터링
patterns = [tuple(p) for p in raw_patterns if is_exist_pattern(p)]
print(len(patterns))
# 각 패턴들의 복잡도 계산
complexities = {p: calculate_complexity(p) for p in patterns}

# 복잡도가 큰 순서대로 나열
sorted_complexities = dict(sorted(complexities.items(), key=lambda item: item[1], reverse=True))

# 상위 10개 항목만 추출
#top_10_complexities = dict(list(sorted_complexities.items())[:10])

# 출력
print(sorted_complexities)

# 그림 출력
# draw_pattern([2, 4, 1, 3])
