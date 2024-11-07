import matplotlib.pyplot as plt

def draw_lock_pattern(ax, pattern):
    # 회전된 3x3 격자의 점들 (1부터 9까지)
    grid_positions = {
        1: (0, 0), 2: (1, 0), 3: (2, 0),
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2)
    }

    # 그림 설정
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(2.5, -0.5)
    
    # 각 점 그리기
    for point, (x, y) in grid_positions.items():
        ax.plot(x, y, 'ko', markersize=20)
        ax.text(x, y, str(point), ha='center', va='center', color='white', fontsize=14)

    # 선 연결하기 (패턴에 따라)
    for i in range(len(pattern) - 1):
        start = pattern[i]
        end = pattern[i + 1]
        x_start, y_start = grid_positions[start]
        x_end, y_end = grid_positions[end]
        ax.plot([x_start, x_end], [y_start, y_end], 'k-', lw=2)

    # 불필요한 축 제거
    ax.axis('off')

def plot_multiple_patterns(patterns):
    # 여러 패턴을 한 번에 출력할 서브플롯 생성
    n = len(patterns)
    rows = 2  # 행
    cols = 3  # 열
    
    fig, axs = plt.subplots(rows, cols, figsize=(15, 10))
    axs = axs.flatten()  # 서브플롯을 일차원 배열로 변환

    # 각 패턴을 서브플롯에 출력
    for i, pattern in enumerate(patterns):
        draw_lock_pattern(axs[i], pattern)
    
    # 남은 서브플롯에 대해서는 빈 플롯을 생성
    for j in range(i + 1, len(axs)):
        axs[j].axis('off')

    # 전체 그림 출력
    plt.tight_layout()
    plt.show()

# 예시 잠금 패턴들
patterns = [
    (1, 6, 3, 5, 2, 4, 9, 8, 7),
    (4, 9, 2, 1, 6, 3, 5, 7, 8),
    (5, 8, 1, 4, 2, 6, 3, 7, 9),
    (7, 5, 3, 2, 8, 4, 6, 9, 1),
    (5, 7, 3, 8, 2, 9, 1, 6, 4),
    ()
]

# 여러 개의 패턴을 출력
plot_multiple_patterns(patterns)
