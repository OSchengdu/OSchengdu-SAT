{% macro profile() %}
<div class="profile-card">
  <img src="/assets/images/avatar.png" alt="头像" width="120" style="border-radius: 50%">
  <div>
    <h1>谭峻瀚</h1>
    <p>开源开发者 | RISC-V贡献者 | 全栈工程师</p>
    <div class="social-links">
      <a href="https://github.com/polypopopo" title="GitHub">
        <span class="twemoji">{% include ".icons/fontawesome/brands/github.svg" %}</span>
      </a>
      <a href="mailto:ppolitenhammerc@gmail.com" title="Email">
        <span class="twemoji">{% include ".icons/fontawesome/solid/envelope.svg" %}</span>
      </a>
    </div>
  </div>
</div>
{% endmacro %}

{{ profile() }}

## 技术领域

<div class="grid cards" markdown>

- __系统编程__  
  ![RISC-V](https://img.shields.io/badge/RISC--V-FE0016?style=for-the-badge)  
  ![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust)  
  - 操作系统开发
  - 嵌入式系统优化

- __Web全栈__  
  ![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react)  
  ![Vue](https://img.shields.io/badge/Vue-4FC08D?style=for-the-badge&logo=vue.js)  
  - 前端性能优化
  - 区块链DApp开发

- __安全工程__  
  ![Tor](https://img.shields.io/badge/Tor-7D4698?style=for-the-badge&logo=tor-project)  
  ![CTF](https://img.shields.io/badge/CTF-FFD700?style=for-the-badge)  
  - 匿名网络研究
  - 漏洞分析
</div>

## 精选项目

{{ project_card("Gitlings", "git", "Rust实现的Git教学系统，已被OpenCamp采用", "projects/gitlings") }}
{{ project_card("SynthNexus", "search", "集成Tor的深网搜索引擎", "projects/synthnexus") }}
