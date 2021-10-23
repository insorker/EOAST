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
  - [项目结构](项目结构)
  - [前端模板](#前端模板)
  - [后端](#后端)
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

> 建议先创建好python虚拟环境，在虚拟环境中安装相关依赖
>
> ```sh
> $ python -m venv ./venv
> $ source ./venv/bin/activate
> ```

```sh
$ pip install -r requirements.txt
```

materializecss的相关组件可以在官网下载，具体使用参考[base.html](https://github.com/insorker/EOAST/blob/master/EOAST_Project/blog/templates/base.html)

### 修改SECRET_KEY

你可以选择已有项目，或新建一个Django项目，复制其**SECRET_KEY**至本项目**EOAST_Project/settings.sample.py**文件中**SECRET_KEY**位置，并将**settings.sample.py**文件重命名为**settings.py**

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

> 这只是开发项目，实际部署至网站的工作请另外修改文件并部署。

### 项目结构

```sh
.
├── EOAST_Project
│   ├── EOAST_Project
│   │   ├── EOAST_Project.ini
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── settings.sample.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── blog
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── static
│   │   ├── templates
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   └── media
│       └── article
├── README.md
└── requirements.txt
```

[EOAST_Project/EOAST_Project](https://github.com/insorker/EOAST/tree/master/EOAST_Project/EOAST_Project)目录由startproject创建

[EOAST_Project/blog](https://github.com/insorker/EOAST/tree/master/EOAST_Project/blog)目录由startapp创建

### 前端模板

- 所有**html**模板文件均放置于对应应用目录下templates文件夹中

- **css/js**文件均放置于对应应用目录下static文件夹中

- 用户上传的图片存放于static/media文件夹中，通过Post类生成变量的picture属性调用
- 如果上传网页相关图片（固定不需要被修改），请将图片放置在static/img文件夹下，并通过{% load static %} {% static 'img/...' %}调用

### 后端

后端实现均基于Django，目前主要开发blog应用中。

## 官网

http://47.110.126.229/

## 维护者

[@insorker](https://github.com/insorker)

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/insorker/EOAST/issues/new) 或者提交一个[Pull Request](https://github.com/insorker/EOAST/pulls)。

### 贡献者

感谢以下参与项目的人： [![img](https://avatars.githubusercontent.com/u/55915168?s=40&v=4)]()

## 使用许可

[MIT](https://github.com/RichardLitt/standard-readme/blob/master/LICENSE)