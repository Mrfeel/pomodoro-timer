---
name: comsol-api-reference
description: COMSOL 6.3 Java API 正确语法速查表（从反复试错中得出）
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3ee9f191-2dc6-4cd9-ba37-ee1141d260b4
---

# COMSOL 6.3 Java API 速查表

> 来源：QClaw在2026-05-29经过大量试错后验证的正确API语法

## 正确 vs 错误对照表

| 功能 | ❌ 错误写法 | ✅ 正确写法 |
|------|-----------|-----------|
| 物理接口 | `"GlobalODEsAndDAEs"` | `"GlobalEquations"` |
| 方程属性 | `set("f", ...)` | `set("equation", ...)` |
| 角度初值 | `set("InitialValueU", ...)` | `set("initialValueU", ...)` |
| 角速度初值 | `set("InitialValueUt", ...)` | `set("initialValueUt", ...)` |
| Study类型 | `"TimeDependent"` | `"Transient"` |
| 求解方式 | `model.sol().runAll()` | `model.study("std1").run()` |
| 时间导数 | `utt1`, `ut1` | `u1tt`, `u1t` (后缀式) |

## 核心代码模板

```java
import com.comsol.model.*;
import com.comsol.model.util.*;

public class MyModel {
    public static void main(String[] args) throws Exception {
        Model model = ModelUtil.create("ModelName");
        
        // 组件
        model.component().create("comp1", true);
        
        // 参数
        model.param().set("KAPPA", "0.04", "Coupling strength");
        model.param().set("F0", "1.0[Hz]", "Natural frequency");
        
        // GlobalEquations
        model.component("comp1").physics().create("ge", "GlobalEquations", "geom1");
        
        // 添加ODE
        model.component("comp1").physics("ge").create("ode1", "GlobalEquations");
        model.component("comp1").physics("ge").feature("ode1")
            .set("name", "u1");  // 显式设置因变量名！
        model.component("comp1").physics("ge").feature("ode1")
            .set("equation", "u1tt + omega0^2*u1 + eps1*u1^3 + gamma*u1t + omegac2*(u1-u2)");
        model.component("comp1").physics("ge").feature("ode1")
            .set("initialValueU", "0.08");
        model.component("comp1").physics("ge").feature("ode1")
            .set("initialValueUt", "0");
        
        // 时域研究
        model.study().create("std1");
        model.study("std1").feature().create("time", "Transient");
        model.study("std1").feature("time").set("tlist", "range(0,0.005,500)");
        
        // 求解
        model.study("std1").run();
        
        // 保存
        model.save("output.mph");
        System.out.println("Done");
    }
}
```

## 编译运行命令

```powershell
$bin = "D:\COMSOL\comsol\COMSOL63\Multiphysics\bin\win64"
# 编译 (必须用cmd /c包装)
cmd /c "$bin\comsolcompile.exe" MyModel.java
# 运行 (-inputfile 用 .class 文件)
cmd /c "$bin\comsolbatch.exe" -inputfile MyModel.class -outputfile result.mph -batchlog log.txt
```

**注意**: comsolcompile使用COMSOL自带的JDK (`\java\win64`)，无需额外配置。

## 关键注意事项

1. API属性名**区分大小写**，使用小写驼峰命名
2. `create()` 返回值需赋给变量否则创建失败
3. 时间导数命名**必须是后缀式**: 因变量名+t / 因变量名+tt
4. `model.save()` 文件名硬编码在Java中，`-outputfile` 参数对.class输入可能不生效
5. 勿用 `evalGlobal()` — COMSOL 6.3中不存在此API
6. CSV导出建议在GUI中手动操作 (Results → Export → Data)
