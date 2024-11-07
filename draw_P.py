import matplotlib.pyplot as plt

def draw_pattern(pattern):
    # 회전된 3x3 격자의 점들 (1부터 9까지)
    grid_positions = {
        1: (0, 0), 2: (1, 0), 3: (2, 0),
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2)
    }

    # 그림 설정
    plt.figure(figsize=(5, 5))
    plt.xlim(-0.5, 2.5)
    plt.ylim(2.5, -0.5)
    
    # 각 점 그리기
    for point, (x, y) in grid_positions.items():
        plt.plot(x, y, 'ko', markersize=20)
        plt.text(x, y, str(point), ha='center', va='center', color='white', fontsize=14)

    # 선 연결하기 (패턴에 따라)
    for i in range(len(pattern) - 1):
        start = pattern[i]
        end = pattern[i + 1]
        x_start, y_start = grid_positions[start]
        x_end, y_end = grid_positions[end]
        plt.plot([x_start, x_end], [y_start, y_end], 'k-', lw=2)

    # 불필요한 축 제거
    plt.axis('off')

    # 그림 출력
    plt.show()

# 예시 잠금 패턴
# pattern = [5, 2, 8, 4, 6, 7, 1, 3, 9]
# draw_pattern(pattern)
