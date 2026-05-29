
def visualize_trap(height, water=None):
    """接雨水可视化 - 终端版
    
    height: 柱子高度数组
    water:  可选，接水量数组。如果不提供，自动计算
    
    输出:
        ██ = 柱子 (深灰)
        ░░ = 水 (亮青)
    """
    n = len(height)
    
    if water is None:
        # 自动计算接水量
        left_max = [0] * n
        right_max = [0] * n
        lm = 0
        for i in range(n):
            left_max[i] = lm
            lm = max(lm, height[i])
        rm = 0
        for i in range(n-1, -1, -1):
            right_max[i] = rm
            rm = max(rm, height[i])
        water = [max(0, min(left_max[i], right_max[i]) - height[i]) for i in range(n)]
    
    max_level = max(h + w for h, w in zip(height, water))
    
    FG_DARK = "\033[90m"
    FG_BLUE = "\033[96m"
    RESET = "\033[0m"
    
    print("=" * (n * 2 + 4))
    
    for level in range(max_level, 0, -1):
        line = "  "
        for col in range(n):
            h = height[col]
            w = water[col]
            if level <= h:
                line += FG_DARK + "██" + RESET
            elif level <= h + w:
                line += FG_BLUE + "░░" + RESET
            else:
                line += "  "
        print(line)
    
    # 地面
    line = "  "
    for col in range(n):
        line += FG_DARK + "██" + RESET
    print(line)
    
    print("  " + "─" * (n * 2))
    ruler = "  "
    for h in height:
        ruler += f"{h:2d}"
    print(ruler)
    print("=" * (n * 2 + 4))
    
    print(f"height: {height}")
    print(f"water:  {water}")
    print(f"total:  {sum(water)}")


if __name__ == "__main__":
    # 示例
    visualize_trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
