import urllib.parse

# 配置 github 用户名
USERNAME = "yHUJibXnPx"

# 在这里配置普通项目 (Repo Name)
# 这些项目会自动加入到 Star History 趋势图中
REPOS = [
    "BeautyFetcher",
    "docker-arch-pyenv-jupyter",
    "docker-arch-miniforge-jupyter",
    "docker-arch-resilio-sync",
    "docker-arch-s-tip",
    "docker-arch-samba",
    "docker-arch-test",
    "docker-arch-subs",
    "MacMini-M4-QEMU-Lab",
    "make-sing-box-envs",
    "make-sing-box-envs-nanopir3s-armbian",
    "make-mihomo-envs",
    "make_sing-box_server_ubuntu",
    "safe_uninstall_app_script_for_macos",
]

# 在这里配置带有 Package 下载量的项目 (Repo Name)
PKGS = [
    "docker-arch-pyenv-jupyter",
    "docker-arch-miniforge-jupyter",
    "docker-arch-resilio-sync",
    "docker-arch-s-tip",
    "docker-arch-samba",
    "docker-arch-test",
]

# 在这里配置 Gist ("标题", "ID"),
GISTS = [
]


def generate_markdown():
    # --- 动态生成 Star History 的 URL ---
    # href 用 &
    # 选取前 5 个 Package 生成趋势图，避免图表过于拥挤
    #chart_repos = [f"/{repo}&{USERNAME}" for repo in REPOS[:5]]
    chart_repos_href = "&".join([f"{USERNAME}/{repo}" for repo in REPOS])

    # api 用 ,
    chart_repos_api = ",".join([f"{USERNAME}/{repo}" for repo in REPOS])

    md = f"# Hi there, I'm {USERNAME}\n"
    md += "这里是我的项目控制台，实时展示项目健康状态。\n\n"
    
    # 顶部徽章
    md += f"![Watchers](https://img.shields.io/github/watchers/{USERNAME}/{USERNAME}) "
    md += f"![Stars](https://img.shields.io/github/stars/{USERNAME}/{USERNAME}) "
    md += f"![Forks](https://img.shields.io/github/forks/{USERNAME}/{USERNAME}) "
    md += f"![Vistors](https://visitor-badge.laobi.icu/badge?page_id={USERNAME}.{USERNAME}) "
    md += "![LICENSE](https://img.shields.io/badge/license-MIT-green.svg)\n\n"

    # [！2026.7新政策失效]Star History 图表 (动态根据 repo 生成)
    #md += f"""[![Star History Chart](https://api.star-history.com/svg?repos={USERNAME}/{USERNAME}&type=timeline&theme=dark&logscale&legend=top-left)](https://www.star-history.com/#{USERNAME}/{USERNAME}&type=timeline&logscale&legend=top-left)\n\n"""
    md += f"""<!-- START_STAR_HISTORY_SELF -->\n\n<!-- END_STAR_HISTORY_SELF -->\n\n"""
    # 目录结构 (使用代码块包裹，防止缩进混乱)
    md += """### 目录结构
    .
    ├── LICENSE                                     # TIM 协议  
    ├── make_readme.py                              # 创建 README.md 脚本  
    ├── test_mock_chart.py                          # 模拟 星星统计 脚本  
    ├── requestment.txt                             # Python脚本所需依赖  
    ├── make_star_chart.py                          # 生成 星星统计 脚本  
    └── README.md                                   # 项目全景看板  \n"""

    processed = set()

    for pkg in PKGS:
        processed.add(pkg)

    # -----------------------
    # Normal Repos
    # -----------------------
    md += "\n### General Repositories\n"

    # [！2026.7新政失效]Star History 图表 (动态根据 repo 生成)
    #md += f"""[![Star History Chart](https://api.star-history.com/svg?repos={chart_repos_api}&type=timeline&theme=dark&logscale&legend=top-left)](https://www.star-history.com/#{chart_repos_href}&type=timeline&logscale&legend=top-left)\n\n"""
    md += f"""<!-- START_STAR_HISTORY_ALL -->\n\n<!-- END_STAR_HISTORY_ALL -->\n\n"""

    md += "| 项目名称 | Visits | Stars | Forks | Issues | Last Commit | Packages |\n"
    md += "| :--- | :---: | :---: | :---: | :---: | :---: | :--- |\n"

    for repo in REPOS:
        url = f"https://github.com/{USERNAME}/{repo}"
        badge_visit = f"https://visitor-badge.laobi.icu/badge?page_id={USERNAME}.{repo}&left_text=%20"
        badge_star  = f"https://img.shields.io/github/stars/{USERNAME}/{repo}?style=for-the-badge&logo=%20&label=%20"
        badge_fork  = f"https://img.shields.io/github/forks/{USERNAME}/{repo}?style=for-the-badge&logo=%20&label=%20"
        badge_issue = f"https://img.shields.io/github/issues/{USERNAME}/{repo}?style=for-the-badge&logo=%20&label=%20&logoColor=red"
        badge_commit = f"https://img.shields.io/github/last-commit/{USERNAME}/{repo}?style=for-the-badge&logo=%20&label=%20"
        if repo in processed:
            pkgs_url = f"[**{repo}**](https://github.com/{USERNAME}/{repo}/pkgs/container/{repo})"
        else:
            pkgs_url = f"![R](https://img.shields.io/badge/PKGS-null-lightgrey?style=for-the-badge&logo=%20&label=%20)"
        md += f"| [**{repo}**]({url}) | ![V]({badge_visit}) | ![S]({badge_star}) | ![F]({badge_fork}) | ![I]({badge_issue}) | ![L]({badge_commit}) |  {pkgs_url} |\n"

    # -----------------------
    # Gists
    # -----------------------
    md += "\n### Gist Knowledge Base\n\n"
    md += "| 文档标题 | Visits | Stars | Last Commit |\n"
    md += "| :--- | :---: | :---: | :---: |\n"

    for title, gid in GISTS:
        title2 = title.replace(".md", "")
        url = f"https://gist.github.com/{USERNAME}/{gid}"
        badge_visit = f"https://visitor-badge.laobi.icu/badge?page_id={USERNAME}.gist.{gid}&left_text=%20"
        badge_star  = f"https://img.shields.io/github/gist/stars/{gid}?style=for-the-badge&logo=%20&label=%20"
        badge_commit = f"https://img.shields.io/github/gist/last-commit/{gid}?style=for-the-badge&logo=%20&label=%20"

        md += f"| [{title2}]({url}) | ![V]({badge_visit}) | ![S]({badge_star}) | ![L]({badge_commit}) |\n"

    md += f"\n[查看更多 Gists...](https://gist.github.com/{USERNAME})"

    return md

if __name__ == "__main__":
    # 生成内容
    content = generate_markdown()
    print("README generated successfully!")
    print(content)
    # 写入文件
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)