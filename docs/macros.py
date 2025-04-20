def define_env(env):
    @env.macro
    def project_card(title, icon, description, url):
        return f"""
<div class="project-card" onclick="window.location='{url}'">
  <div class="card-icon">
    <span class="twemoji">{% include ".icons/fontawesome/solid/{icon}.svg" %}</span>
  </div>
  <h3>{title}</h3>
  <p>{description}</p>
  <button class="md-button">查看详情</button>
</div>
        """
    
    @env.macro
    def tech_badge(tech):
        badges = {
            "rust": ("Rust", "000000", "rust"),
            "riscv": ("RISC-V", "FE0016", None),
            "tor": ("Tor", "7D4698", "tor-project")
        }
        name, color, logo = badges.get(tech.lower(), (tech, "gray", None))
        logo_str = f"&logo={logo}" if logo else ""
        return f"![{name}](https://img.shields.io/badge/{name}-{color}?style=flat{logo_str})"""
