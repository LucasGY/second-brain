

# Web 网络请求全生命周期解析

该图解展示了一个标准的 HTTPS GET 请求从发起到页面更新的完整链路。

```mermaid
sequenceDiagram
    autonumber
    participant Client as 前端客户端 (Browser/React)
    participant DNS as DNS 服务器
    participant Gateway as 网关/路由层 (Router)
    participant Service as 业务逻辑层 (Backend Service)
    participant DB as 数据访问层 (Database)

    rect rgb(240, 248, 255)
        note right of Client: 阶段一：网络寻址与连接
        Client->>DNS: 查询目标域名 IP
        DNS-->>Client: 返回目标 IP 地址
        Client->>Gateway: TCP 三次握手建连
        Client->>Gateway: SSL/TLS 握手协商加密
    end

    rect rgb(255, 245, 238)
        note right of Client: 阶段二：请求发送与后端处理
        Client->>Gateway: 发送 HTTP 请求 (e.g., GET /api/v1/indices)
        Gateway->>Service: 校验 Token，将请求路由至对应服务控制器
        Service->>DB: 触发 ORM 发起 SQL 查询
        DB-->>Service: 提取并返回结构化数据
        Service->>Service: 执行业务逻辑运算 (如：计算指标百分位)
    end

    rect rgb(240, 255, 240)
        note right of Client: 阶段三：响应接收与前端渲染
        Service-->>Gateway: 将运算结果序列化为 JSON 格式返回
        Gateway-->>Client: 返回 HTTP 响应 (Status 200)
        Client->>Client: JavaScript 解析 JSON 数据
        Client->>Client: 触发 React 虚拟 DOM 比对与更新
        Client->>Client: 浏览器重绘 (Repaint) UI 界面展示数据
    end
    
    

