# performer
## 介绍
Performer框架是一个全自动的全栈式Web框架（或者说网站构建工具），本质是一套代码生成器，可以产生大量的表单式网页html和对应的后端Python代码。Performer这个名字有两层含义：1. 执行者，数据库系统的执行者； 2. per-form-er，每个表单的构建者。对应发布的软件，被命名为Performer平台。

使用这个工具之前，需要编辑一个主配置文件"configuration.json"和一系列子配置文件"config_xx.json"。根据这些配置文件，运行code_generator.py程序即可产生所需的HTML, Javascript, Python 及 SQL代码。用户不需要编写任何代码。

Performer平台的简单示例，可参考: [科研数据库系统](http://123.206.137.251:85/list)

考虑到编写子配置文件（"config_xx.json"）比较困难，本平台还提供了一个Hello界面用来生成子配置文件，用户在浏览器中打开Hello.html即可进行配置。

## Hello界面的使用说明
一个页面包含一个或多个模块。同一个页面上不同类型的信息分别放在不同的模块中，比如基本信息界面同时包含人口学基本信息和疾病基本信息，那么这两大块可以放置在不同模块中。我们需要先确定当前页面共有几个模块（填写模块个数）。当一个页面仅包含一个模块时，模块名和对应的拼音名可以不填。

每个模块包含一个或多个元素。所谓元素，就是页面上的每个信息单元，比如姓名、年龄等，都是一个元素。元素有5种类型：文字、数字、时间、选项、表格。每个元素需要填写元素名称和对应的拼音名。元素名称将呈现在最终构建的用户操作界面中，而元素拼音将实际存储在数据库中。**元素拼音由连续的字母连接构成，不能带有空格；元素拼音可以是元素名称的拼音，也可以是英文翻译。** 举个例子：对于“姓名”这个信息，可以将元素名称填写为“姓名”，将元素拼音填写为“xingming”或"name"，但切勿写成“xing ming”。**注意：填写一次Hello页面时，不能有相同的元素拼音！** 比如，不能同时在两个元素的元素拼音中都填写“xingming”，如果预计会出现重复的情况，请加上数字后缀进行区分或采取其他区分策略，如：“xingming1”、“xingming2”等。当然，同一个项目的两次不同Hello页面中，可以出现元素拼音的重复。

如果元素类型为数字，若该信息有单位，则应填写单位名称。

如果元素类型为选项，那么需要进一步填写选项的个数和对应各个选项的值。**如果需要添加“其他”选型且需要预留出一个输入框，则应在最后一个选型的“选项拼音”里填写“`*other`”。**

如果元素类型为表格，那么需要进一步填写表格的字段个数（表格列数）和表格行数，而表格注释可以选填。表格的每个字段（每列）可以是这4种类型：文字、数字、时间、选项。

## 需安装的软件
启动Web服务器之前，需要安装如下软件和工具包：
* Python 和相应的工具包: tornado, MySQLdb
* MySQL
* Nginx

## License
Apache License 2.0
