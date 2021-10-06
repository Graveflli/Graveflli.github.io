 

## muduo

### 目录结构

muduo: 静态连接的C++程序库. 

muduo包括base和net. 

base是基础库: 日志,原子操作,进程信息,线程安全的singleton,线程对象等

net: 网络库, muduo基于Reactor模式. 核心是时间循环EventLoop,用于响应计时器和IO事件.

使用muduo只用掌握Buffer,EventLoop,TcpConnection,TcpClient,TcpServer类.

#### Reactor模式

