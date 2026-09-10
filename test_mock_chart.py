import time
import random
from datetime import datetime, timedelta

# 导入你原有的脚本
import make_star_chart

def mock_fetch_stargazers(repo, token):
    """
    假数据生成引擎，根据 repo 名称的关键字返回特定形态的 Star 数据
    """
    print(f"⟳ [Mock] 正在生成极限数据: {repo}")
    time.sleep(0.05)
    dates = []
    
    # 1. ZERO - 全部 0 stars
    if "zero" in repo:
        return []
        
    # 2. SINGLE - 只有 1 star
    elif "single" in repo:
        return [datetime(2023, 5, 1)]
        
    # 5. LONG - 跨多年 (2015 - 2026)
    elif "long" in repo:
        base_date = datetime(2015, 1, 1)
        for _ in range(150):
            # 随机散布在 10 年（3650天）内
            dates.append(base_date + timedelta(days=random.randint(0, 3650)))
            
    # 3. NORMAL - 普通稳步增长
    else:
        base_date = datetime(2023, 1, 1)
        for _ in range(random.randint(20, 100)):
            # 随机散布在 1 年内
            dates.append(base_date + timedelta(days=random.randint(0, 365)))
            
    return sorted(dates)

# 狸猫换太子，拦截原代码的网络请求
make_star_chart.fetch_stargazers = mock_fetch_stargazers

if __name__ == "__main__":
    print("➚ 开始执行多维度 UI 极限测试...\n")
    
    # 测试 1: ZERO - 0 Star 项目测试
    make_star_chart.generate_dark_chart(
        repos=["zero-project-1", "zero-project-2"],
        title="Mock Zero", output_file="mock_1_zero.png", token="fake"
    )
    
    # 测试 2: SINGLE - 仅 1 Star 项目测试
    make_star_chart.generate_dark_chart(
        repos=["single-star-project"],
        title="Mock Single", output_file="mock_2_single.png", token="fake"
    )
    
    # 测试 3: NORMAL - 普通单项目测试
    make_star_chart.generate_dark_chart(
        repos=["normal-project"],
        title="Mock Normal", output_file="mock_3_normal.png", token="fake"
    )
    
    # 测试 4: MULTI - 极端多项目测试 (模拟 30 个项目撑爆 UI 的场景)
    many_repos = [f"repo-{i:02d}" for i in range(1, 31)]
    make_star_chart.generate_dark_chart(
        repos=many_repos,
        title="Mock Multi (UI Overflow Test)", output_file="mock_4_multi_extreme.png", token="fake"
    )
    
    # 测试 5: LONG - 跨长达 10 年的时间轴测试，看 X 轴文字是否会重叠糊掉
    make_star_chart.generate_dark_chart(
        repos=["long-history-project"],
        title="Mock Long Years", output_file="mock_5_long.png", token="fake"
    )
    
    print("\n✓ 测试完毕！请查看生成的 5 张 mock_*.png 图片。")