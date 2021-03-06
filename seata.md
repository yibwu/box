### Seata分布式事务框架实现原理？

Seata有三个组成部分：事务协调器TC：协调者、事务管理器TM：发起方、资源管理器RM：参与方

1. 发起方会向协调者申请一个全局事务id，并保存到ThreadLocal中（为什么要保存到ThreadLocal中？弱引用，线程之间不会发生数据冲突）
2. Seata数据源代理发起方和参与方的数据源，将前置镜像和后置镜像写入到undo_log表中，方便后期回滚使用
3. 发起方获取全局事务id，通过改写Feign客户端请求头传入全局事务id。
4. 参与方从请求头中获取全局事务id保存到ThreadLocal中，并把该分支注册到SeataServer中。
5. 如果没有出现异常，发起方会通知协调者，协调者通知所有分支，通过全局事务id和本地事务id删除undo_log数据，如果出现异常，通过undo_log逆向生成sql语句并执行，然后删除undo_log语句。如果处理业务逻辑代码超时，也会回滚。
