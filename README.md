# Graduation Project

这事Ant的毕业设计，基于Web的Linux服务器状态监控.

## 为什么要做这个

* 毕设想做Web项目
* 服务器上的监控器太臃肿了
* 想沉下心做点什么

综合多方面考虑，自拟了这个题目.

~~这事我最后的波纹了，JOJO！~~

## 下载

已于Pypi发布构建，可直接下载安装

```bash
$ pip install ant-net-monitor
```

如果需要尝鲜，可指定预发布版本（智将

## 部署

参照[Flask Docs](https://dormousehole.readthedocs.io/en/latest/deploying/wsgi-standalone.html)，可使用`Gunicorn`进行部署，即：

```bash
$ gunicorn -b 127.0.0.1:5000 "ant_net_monitor:create_app(ENABLE_SNMP)"
```

通过设置`ENABLE_SNMP`为`True`或`False`控制数据采集方式.

玩得愉快！

ps:建议先把它放进虚拟环境里运行，因为我还没有想好把数据库放在哪.
