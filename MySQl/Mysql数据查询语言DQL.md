# 数据查询语言(DQL) 重点
    - 完整语法格式：
        select 表达式1|字段，。。。
        [from 表名 where 条件]
        [group by 列名]
        [having 条件]
        [order by 列名[asc|desc]]
        [limit 位置，数量]
    1. 普通查询
        select 查询表达式；//最简单的sql语句，是一个函数
        select database（）；select version（）； select now（）
        
    2. 条件查询
        where 条件表达式 ， 支持运算符和函数
        mysql支持的运算符：
            = ，！= ，> , < ,>=,<=
            and , not , or
            is null ,is not null
            between... and...（区间查询）
            in(set)
            like 通配符和占位符：% _
            % : 表示0个或者多个字符
            _ : 表示占位一个      
        -- 查询所有的老师信息
select * from teacher;

-- 查询id大于2的老师信息
    select * from teacher where id>2;

-- 查询姓名为空的老师信息          在数据库中null永远的不等于null，那么怎么去判断null值呢？ 通过is null、is not null
    select * from teacher where name is not null

-- 查询id为1 并且 姓名是“xiaosi”的老师信息
    select * from teacher where id=1 and name ='xiaosi';

-- 查询id为1 或者 姓名是“xiaosi”的老师信息
    select * from teacher where id=1 or name ='xiaosi';

-- 查询薪水在2000到10000之间的老师信息
    select * from teacher where sal >=2000 and sal<=10000;
    select * from teacher where sal between 2000 and 10000; # 这种方式等同于上面这种方式

-- 查询姓名中有“拿”字的老师信息
    select * from teacher where name like '%拿%';

-- 查询姓名是三个字的
    select * from teacher where name like '___';

-- 查询姓“小”的老师信息
    select * from teacher where name like '小%';

-- 查询名字中含有下划线的老师
        select * from teacher where name like '%\_%';



<3>分组查询
        [group by 列名] [having 条件]
        一般情况分组查询结合聚合函数一起使用
        (max()、min()、sum()、avg()、count())


    -- 查询每个部门的平均薪资
        select dname,avg(sal) from teacher group by  dname

    -- 查询部门平均薪资大于5000的部门
        select dname,avg(sal) from teacher group by  dname having  avg(sal)>5000

        select dname,avg(sal) asal from teacher group by  dname having  asal>5000

    记住：分组的正确使用方式，group by 后面没有出现的列名不能出现在select 和from的中间，虽然不报错但是不是分组的正确使用方式。   聚合函数中出现的列名group by后面没有无所谓。


<4>排序查询
    语法格式：order by 列名   asc|desc   默认升序(asc)


    -- 查询老师信息，要求根据薪资从大到小进行排序

    select * from teacher order by sal desc  根据sal进行降序排序
    select * from teacher order by sal asc   根据sal进行升序排序
    select * from teacher order by sal       根据sal进行升序排序，利用默认排序



<5>限制结果集数量的查询(分页)

    编号      商品名称        商品价格        操作
    1       大拿娃娃        100.0       删除 修改
    2       吕吕娃娃        200.0       删除 修改
    3       丛浩娃娃        350.0       删除 修改
    .....................
    首页      上一页 1 2 3 4 5   下一页 尾页


    语法格式：
            limit n条数;  ------从第一条开始取n条数据。(了解)
    语法格式：
            limit start开始下标索引,count条数;  ---从起始位置start取count条数据(起始位置从0开始)        推荐使用



        分页(每页显示2条数据)
            第一页：    select * from teacher limit 0,2;
            第二页： select * from teacher limit 2,2;
            第三页： select * from teacher limit 4,2;
            第四页：    select * from teacher limit 6,2;
            第五页： select * from teacher limit 8,2;



        分页公式：
            开始下标索引(起始位置) = (当前页-1)*每页显示条数; 


扩展：
    别名

        select * from teacher; -- 查询表中所有字段记录

        select name,sal,dname from teacher;  -- 查询表中指定字段记录

        -- 给查询的字段设置别名   同时也可以给表设置别名  通过as 关键字实现别名

        select  name as '姓名',sal '薪资',dname '部门名称'  from teacher