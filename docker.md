#### Docker的优势


##### 传统虚拟化
![image](https://yeasy.gitbooks.io/docker_practice/introduction/_images/virtualization.png)

##### Docker
![image](https://yeasy.gitbooks.io/docker_practice/introduction/_images/docker.png)
- 更高效的利用系统资源（相比较虚拟机技术）
- 一致的运行环境
- 持续交付和部署


#### Docker基本概念
- Docker镜像，Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。
  - 分层存储 ![image](https://coolshell.cn/wp-content/uploads/2015/04/docker-filesystems-multilayer.png) 
- Docker容器，镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的 类 和 实例 一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。


#### Docker架构
采用C/S运行模式
![image](https://docs.docker.com/engine/images/architecture.svg)
- Docker守护进程，接收客户端的请求，管理镜像、容器、网络或数据卷
- Docker客户端，通过Docker api或Restful api发送请求
- Docker Registry，用来保存发布的镜像，类似github的概念


#### Docker基础技术
- Namespaces 对环境进行隔离，因此容器可以拥有自己的 root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。
  - [https://coolshell.cn/articles/17010.html](https://coolshell.cn/articles/17010.html)
  - [https://coolshell.cn/articles/17029.html](https://coolshell.cn/articles/17029.html)
- Control groups 对cpu memory i/o等资源进行精细化的控制达到资源限制的目的
  - [https://coolshell.cn/articles/17049.html](https://coolshell.cn/articles/17049.html)
- Union file systems 构建镜像， 把多个目录合并成一个目录，并可以为每个需要合并的目录指定相应的权限，达到镜像的增量修改和维护的目的
  - [https://coolshell.cn/articles/17061.html](https://coolshell.cn/articles/17061.html)


#### 使用Docker
- 获取Docker镜像
   - ```docker pull [OPTIONS] NAME[:TAG|@DIGEST]```
- 启动
  - ```docker run [OPTIONS] IMAGE [COMMAND] [ARG...]```
  

#### Docker容器的数据卷
- ![image](https://note.youdao.com/yws/api/personal/file/WEBbb13094649c4d48d1d706dd5ffb04eeb?method=download&shareKey=660f84df123e02a75060bf8ed7c099ba)
- 数据卷（Data Volume）是经过特殊设计的目录，可以绕过联合文件系统（UFS），为一个或多个容器提供访问
- 数据卷设计的目的，在于数据的持久化，它完全独立于容器的生存周期，因此，Docker不会在容器的删除时删除其挂载的数据卷，也不会存在类似垃圾收集机制，对容器引用的数据卷进行处理
- ```docker run -v src_volume:dest_volume:ro IMAGE_NAME```
- Dockerfile指定匿名数据卷```VOLUME ["<路径1>", "<路径2>"...]```


#### Docker数据卷容器
  - ![image](https://note.youdao.com/yws/api/personal/file/WEBa630461b20a92be667971f740fe63df4?method=download&shareKey=37bdab4ee774db6fe1ad8a22f630037b)
  - ```docker run --volumes-from container_name IMAGE```


#### Docker容器的网络连接
- 容器间的互联
  - Docker守护进程的启动选项```--icc=true``` 
  - ```docker run --link=container_name:alias IMAGE```
- 拒绝所有容器间互联
  - Docker守护进程的启动选项```--icc=false```
 - 允许容器间的特定端口的连接
   - Docker守护进程的启动选项```--icc=false``` 
   - Docker守护进程的启动选项```--iptables=true```
   - ```--link```访问容器的开放端口


#### 使用Dockerfile定制镜像
通过把每一层的修改、安装、构建、操作的命令写到到Dockerfile来定制镜像
- FROM 指定基础镜像，必须是第一条指令
- RUN执行命令
  - shell格式 ```RUN <命令>```
  - exec格式 ```RUN ["可执行文件", "参数1", "参数2"]```
- COPY 将从==构建上下文==目录中 <源路径> 的文件/目录复制到新的一层的镜像内的 <目标路径> 位置
  - ```COPY <源路径>... <目标路径>```
  - ```COPY ["<源路径1>",... "<目标路径>"]```
- ADD 高级的COPY命令，与COPY命令区别如下
  - <源路径>可以是url
  - <源路径> 为一个 tar 压缩文件的话，ADD支持自动解压
- CMD 容器启动命令 
  - shell 格式：```CMD <命令>```
  - exec 格式：```CMD ["可执行文件", "参数1", "参数2"...]```
- WORKDIR 指定工作目录
  - ```WORKDIR <工作目录路径>```
- EXPOSE 声明端口
  - ```EXPOSE <端口1> [<端口2>...]```
- VOLUME 定义匿名卷
  - ```VOLUME ["<路径1>", "<路径2>"...]```
  - ```VOLUME <路径>```
