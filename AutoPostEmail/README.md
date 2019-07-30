# 实现自动发送邮件

- 从数据库中查询数据
- 保存到excel文件
- 读取excel文件，添加到附件
- 邮件正文以表格形式展示出来整体情况
#### 邮件正文及附件如下图：
![图片](https://github.com/ElsaQf/LearningDataScienceIntern/blob/master/AutoPostEmail/%E8%87%AA%E5%8A%A8%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E6%A0%BC%E5%BC%8F.png)

## html-td后拼接字符串，需要getdata()返回数值型结果Decimal/int
- 若结果为None,返回0
    + if result is None: return 0
- getdata()返回数值，html拼接字符串，转成'''+str(result+result1)+'''计算后拼接
![图片](https://github.com/ElsaQf/LearningDataScienceIntern/blob/master/AutoPostEmail/%E9%82%AE%E4%BB%B6%E6%AD%A3%E6%96%87%E8%AE%A1%E7%AE%97%E5%90%8E%E6%98%BE%E7%A4%BA%E8%A1%A8%E6%A0%BC.png)
