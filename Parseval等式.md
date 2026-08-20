# Parseval 等式是什么意思？

## 一句话回答

> **Parseval 等式 = Fourier 级数版本的"勾股定理"——函数的"能量"等于各频率分量"能量"之和。**

---

## 数学形式

设 $f(x)$ 以 $2\pi$ 为周期，其 Fourier 级数为：

$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty}(a_n\cos nx + b_n\sin nx)$$

则 Parseval 等式为：

$$\boxed{\frac{1}{\pi}\int_{-\pi}^{\pi} f^2(x)dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty}(a_n^2 + b_n^2)}$$

| 左边 | 右边 |
|------|------|
| 函数的"总能量"（均方值） | 各频率分量的"能量"之和 |

---

## 直观理解

### 类比：声音的频谱

想象 $f(x)$ 是一段声音波形：

- **左边** $\int f^2$：这段声音的**总功率**（物理上的能量）
- **右边** $\sum(a_n^2+b_n^2)$：把声音拆成各个频率（基频 $n=1$、倍频 $n=2$…）后，**每个频率分量的功率之和**

Parseval 等式说：**总功率 = 各频率功率之和**。能量不会凭空消失，也不会凭空多出来。

### 类比：向量勾股定理

在 $n$ 维空间中，向量 $\mathbf{v} = (v_1, v_2, \ldots, v_n)$ 的长度平方：

$$\|\mathbf{v}\|^2 = v_1^2 + v_2^2 + \cdots + v_n^2$$

Fourier 级数把函数"展开"在一组**正交基** $\{1, \cos nx, \sin nx\}$ 上。Parseval 等式就是把函数长度平方分解到每个基向量上——和勾股定理完全一样的道理，只是从有限维变成了无穷维。

---

## 考试中怎么用？

Parseval 等式最常见的用途是**求级数和**。

### 典型套路

**步骤1**：把 $f(x)$ 展开成 Fourier 级数，算出所有 $a_n, b_n$。

**步骤2**：写出 Parseval 等式：
$$\frac{1}{\pi}\int_{-\pi}^{\pi} f^2(x)dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty}(a_n^2 + b_n^2)$$

**步骤3**：左边直接积分（通常很简单），右边是已知系数的平方和。

**步骤4**：解出要求的级数和。

---

### 经典例子：求 $\sum_{n=1}^{\infty} \frac{1}{n^2}$

$f(x) = x$ 在 $[-\pi, \pi]$ 上的 Fourier 级数（奇函数，$a_n=0$）：

$$b_n = \frac{2}{\pi}\int_0^\pi x\sin nx\,dx = \frac{2(-1)^{n-1}}{n}$$

$$x \sim 2\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}\sin nx$$

代入 Parseval：

$$\frac{1}{\pi}\int_{-\pi}^{\pi} x^2 dx = \sum_{n=1}^{\infty} \frac{4}{n^2}$$

左边：$\frac{1}{\pi} \cdot \frac{2\pi^3}{3} = \frac{2\pi^2}{3}$

所以 $\sum_{n=1}^{\infty} \frac{4}{n^2} = \frac{2\pi^2}{3}$，即：

$$\boxed{\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}}$$

这就是著名的 **Basel 问题**的答案。

---

### 再例：$f(x) = x$ 在 $[0,\pi]$ 上的正弦展开

（见复习讲义 0.20 题）

$$b_n = \frac{2}{\pi}\int_0^\pi x\sin nx\,dx = \frac{2(-1)^{n-1}}{n}$$

正弦级数的 Parseval 形式（只积 $[0,\pi]$）：

$$\frac{2}{\pi}\int_0^{\pi} f^2(x)dx = \sum_{n=1}^{\infty} b_n^2$$

左边：$\frac{2}{\pi} \cdot \frac{\pi^3}{3} = \frac{2\pi^2}{3}$

右边：$\sum_{n=1}^{\infty} \frac{4}{n^2}$

同样得到 $\sum \frac{1}{n^2} = \frac{\pi^2}{6}$，然后奇偶分离：
$$\sum_{n=1}^{\infty}\frac{1}{(2n-1)^2} = \frac{\pi^2}{8}$$

---

## 三种常见的 Parseval 形式

| 展开类型 | Parseval 等式 |
|----------|---------------|
| 全 Fourier（$[-\pi,\pi]$） | $\frac{1}{\pi}\int_{-\pi}^{\pi} f^2 = \frac{a_0^2}{2} + \sum(a_n^2+b_n^2)$ |
| 纯正弦（$[0,\pi]$ 奇延拓） | $\frac{2}{\pi}\int_0^{\pi} f^2 = \sum b_n^2$ |
| 纯余弦（$[0,\pi]$ 偶延拓） | $\frac{2}{\pi}\int_0^{\pi} f^2 = \frac{a_0^2}{2} + \sum a_n^2$ |

---

## 一句话总结

> **Parseval 等式 = Fourier 世界里能量守恒。左边是函数本身的"能量"（积分），右边是所有频率分量的"能量"（系数平方和）之和，两者必须相等。考试中用来从已知 Fourier 系数反推级数的和。**
