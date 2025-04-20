# RISC-V开发实战笔记

## SBI调用深度解析

```rust
// RustSBI中的ecall处理
#[inline]
fn handle_ecall(&mut self) -> SbiRet {
    match self.trap.ecall() {
        SbiEcall::Legacy => self.handle_legacy_sbi(),
        SbiEcall::Timer => self.handle_timer(),
        _ => SbiRet::not_supported(),
    }
}
```

## 性能优化案例

**问题**：QEMU模拟器下指令CPI过高

**解决方案**：
1. 使用`perf stat`定位热点
2. 发现`mstatus`寄存器访问瓶颈
3. 重写CSR访问路径：

优化前 | 优化后
---|---
5 cycles/access | 2 cycles/access

**验证方法**：
```bash
perf stat -e instructions,cycles ./benchmark
```

## 调试技巧

```gdb
# 在QEMU中调试
(gdb) target remote :1234
(gdb) hbreak *0x80000000
(gdb) monitor pmemsave 0x80000000 4096 dump.bin
```
