### select

1. 内核态扫描一遍fd list，纪录所有状态为pending的描述符，若所有状态都为pending，则调用tsleep函数睡眠一段时间
2. 当有某个fd完成IO，进程wakeup，内核态再扫描一遍fd list找到该fd，标记状态为active
3. select返回到用户态，用户态再扫描一遍fd list，找到标记为active的fd
4. 针对3中找到的fd执行读写操作

**总结**：该方式总共会执行3遍扫描操作，fd list数量为n时，时间复杂度为O(n)
