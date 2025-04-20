# SynthNexus 深网搜索引擎

![架构图](https://github.com/OSchengdu/SynthIQNexus_-/raw/main/image/1.png){ width=600 }

## 核心技术模块

### 1. Tor匿名管道

```python
from stem import Signal
from stem.control import Controller

def renew_tor_identity():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)  # 切换出口节点
```

**反检测策略**：
- 请求延迟随机化：`random.gauss(300, 50)` ms
- UA轮换池：5种浏览器指纹
- 自动重试机制：指数退避算法

### 2. 混合搜索语法生成

**Dork+SQL转换示例**：
```python
def convert_query(user_input):
    if "价格" in user_input:
        return {
            'dork': 'intitle:"价格" filetype:pdf',
            'sql': 'SELECT * FROM products WHERE price IS NOT NULL'
        }
```

### 3. 本地向量搜索

```sql
-- 使用sqlite-vss扩展
CREATE VIRTUAL TABLE vss_articles USING vss0(
    embedding(384),
    distance_metric='L2'
);
```

[查看实时演示](https://synthnexus.demo)
