# 中科院软件所 - RISC-V测试框架开发 (2024.07-2024.11)

![OpenEuler RISC-V](https://repo.openeuler.org/openEuler-23.09/logo.png){ width=200 align=right }

## 核心贡献

### 1. AI算子测试框架

**技术架构**：
```python
class AITestFramework:
    def __init__(self):
        self.backends = ["ONNX", "TFLite"]
        self.ops_to_test = self.load_ops_from_yaml()
        
    def generate_test_cases(self):
        for op in self.ops_to_test:
            for backend in self.backends:
                self.run_single_test(op, backend)
                
    def run_single_test(self, op, backend):
        # 自动化测试逻辑...
```

**优化成果**：
- 测试用例减少30% (通过参数化测试实现)
- 发现PyTorch RISC-V后端性能问题3处
- 建立跨架构性能对比数据库

### 2. 热力图分析系统

**技术栈组合**：
```mermaid
graph LR
    A[perf stat] --> B[数据采集]
    B --> C[Pandas处理]
    C --> D[Seaborn可视化]
    D --> E[HTML报告]
```

**典型输出**：
![热力图示例](assets/images/perf_heatmap.png){ width=600 }

[查看完整报告样例](https://example.com/perf-report)
