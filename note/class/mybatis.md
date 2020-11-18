# mybatis框架
	- 共4天
	- 第一天
		- mybatis入门
		- mybatis概述
		- mybatis环境搭建
		- mybatis自定义框架
	- 第二天
		- mybatis基本使用
		- mybatis单表CRUD操作
		- mybatis参数和返回值
		- mybatis的DAO编写
		- mybatis配置细节 几个标签的使用
	- 第三天
		- mybatis深入 多表
		- mybatis连接池
		- mybatis事务控制 设计方法
		- mybatis多表查询 一对多 多对多
	- 第四天
		- mybatis缓存和注解开发
		- mybatis加载时机（查询的时机）
		- mybatis中的一级缓存和二级缓存
		- mybatis注解开发 单表CRUD 多表查询 

1. 什么是框架
	- 它是软件开发中的一套解决方案 不同的框架解决不同的问题 框架是一个半成品
	- 好处： 封装很多细节 使开发者可以使用极简的方式实现功能 提高开发效率
	
2. 三层架构
	- 表现层： 用于展示数据
	- 业务层： 处理业务需求
	- 持久层： 和数据库进行交互
	
3. 持久层技术解决方案
		- JDBC技术： Connection PreparedStatement ResultSet
		- Spring的JdbcTemplate： Spring中对JDBC的简单封装
		- Apache的DBUtils： 也是对JDBC的简单封装
	但是这些都不是框架： 
		JDBC是规范 Spring的Spring的JdbcTemplate和Apache的DBUtils只是工具类
	
4. mybatis的概述
      -   mybatis是一个持久层框架 用java进行编写
      -   封装了JDBC操作的很多细节 使开发者只需要关注SQL语句本身无需关注注册驱动等复杂过程
      -   使用ORM思想实现结果集的封装
        -   ORM: 对象关系映射 把数据库表和实体类及其属性对应起来 可以通过操作实体类来操作数据库表
        -   需要做到实体类中的属性和数据库表的字段名保持一致
      
5. mybatis入门
      -   mybatis的环境搭建
        -   第一步 创建maven工程并导入坐标
        -   第二步 创建实体类dao的接口
        -   第三步 创建mybatis的主配置文件
        -   第四步 创建映射配置文件
        -   注意事项:
          -   创建文件名一致是为了和之前知识接轨 其实UserDao.xml和UserMapper一致
          -   创建目录和创建包是不一样的 创建目录时候需要分步进行创建
          -   配置映射文件和文件放在同层级结构下
          -   映射配置文件的mapper标签的namespace必须是dao接口的全限定类名
          -   映射配置文件的操作配置select id属性取值必须是dao接口的方法名
          -   按照规范可以使开发更加快
      -   mybatis的入门案例
            -   第一步 读取配置文件
            -   第二步 创建SqlSessionFactory工厂
            -   第三步 创建SqlSession
            -   第四步 创建DAO的代理对象
            -   第五步 执行DAO中的方法
            -   第六步 释放资源
            -   注意事项:
                  -   不要忘记在映射文件中高速mybatis要封装到哪个实体类中的配置方式 指定实体类全限定类名
            -   基于注解的mybatis入门案例
                  -   把UserDao.xml文件移除,接口上使用@Select进行注解并指定SQL语句
                  -   同时需要在SqlMapperConfig.xml中的mapper配置使用class属性 指定DAO接口的全限定
            -   明确: 
                  -   实际开发中 越简便越好,所以都是采用不写DAO实现类的方式 
                  -   不管使用xml配置还是使用注解方式 但是mybatis支持写实现类 出问题了但是一般不写

  6.  自定义mybatis的分析

        -   mybatis在使用代理DAO的方式实现增删改查时做什么事

              -   创建代理对象
              -   在代理对象中调用selectList方法

        -   读取配置文件: 用到的技术就是解析xml文件的技术 此处是Dom4j的xml技术

              -   使用selectList方法

              1.  根据配置文件的信息创建Connection对象
              2.  获取预处理对象 PrepareStatement 此时需要SQL语句(conn.prepareStatement(sql))
              3.  执行查询 (preparedStatement.executeQuery()) 返回一个结果集(resultSet)
              4.  遍历结果集 用于封装 定义对象:(E)Class.forName(配置的全限定类名).newInstance(0)
                    1.  实体类属性和表中的列一一对应 可以将表列名看成实体类属性名称 使用反射方式根据每个属性进行赋值
              5.  返回集合
                    -   方法执行需要提供信息
                          -   连接信息
                          -   映射信息 (包含两部分) 定义成一个对象 Mapper 使用Map进行存储(String-mapper)
                                -   执行的sql语句
                                -   封装结果的实体类全限定类名

        -    自定义mybatis能通过案例看到的类

              -   Class resource
              -   Class SqlSessionFactoryBuilder
              -   Interface SqlSessionFactory
              -   interface SqlSession