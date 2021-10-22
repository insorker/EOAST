# EOAST官网项目

[![standard-readme compliant](https://camo.githubusercontent.com/f116695412df39ab3c98d8291befdb93af123f56aecc79fff4b20c410a5b54c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f726561646d652532307374796c652d7374616e646172642d627269676874677265656e2e7376673f7374796c653d666c61742d737175617265)](https://github.com/insorker/EOAST)

本项目是EOAST电光微院科协计算机部主持的网站项目。

本仓库包含以下内容：

1. 项目背景
2. 如何部署到自己的开发环境
3. 开发说明

## 内容列表

- [背景](#背景)
- [部署](#部署)
  - [安装依赖](#安装依赖)
  - [修改SECRET_KEY](#修改SECRET_KEY)
  - [迁移数据库](#迁移数据库)
  - [运行项目](#运行项目)
- [开发说明](#开发说明)
- [官网](#官网)
- [维护者](#维护者)
- [如何贡献](#如何贡献)
- [使用许可](#使用许可)

## 背景

为了科协能有自己的网站。

## 部署

### 安装依赖

这个项目使用 [django](https://www.djangoproject.com/) 和 [materializecss](https://materializecss.com/)。

请确保你本地的Python版本大于Python 3.8.8，并通过以下命令安装依赖

```sh
$ pip install -r requirements.txt
```

materializecss的相关组件可以在官网下载，具体使用参考[base.html](https://github.com/insorker/EOAST/blob/master/EOAST_Project/blog/templates/base.html)

### 修改SECRET_KEY

你可以选择已有项目，或新建一个Django项目，复制其**SECRET_KEY**至本项目**EOAST_Project/settings.py**文件中**SECRET_KEY**位置

### 迁移数据库

在含有manage.py的目录下，运行以下命令

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### 运行项目

在含有manage.py的目录下，运行以下命令

```sh
$ python manage.py runserver
```

然后浏览器输入http://127.0.0.1:8000/，可以查看项目是否配置成功

## 开发说明

这只是开发项目，实际部署至网站的工作请另外修改文件并部署。

## 官网

http://47.110.126.229/

## 维护者

[@insorker](https://github.com/insorker)。

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/RichardLitt/standard-readme/issues/new) 或者提交一个 Pull Request。

### 贡献者

感谢以下参与项目的人： [![img](https://avatars.githubusercontent.com/u/55915168?s=40&v=4)]()

## 使用许可

[MIT](https://github.com/RichardLitt/standard-readme/blob/master/LICENSE)