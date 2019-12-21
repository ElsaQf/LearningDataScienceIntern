# LearningDataScienceIntern
数据分析实习中学到的知识，记录一下^_^

        - k-means 聚类
        - matplotlib 折线图，bar
        - excel画折线图
        - 用户画像，对每个用户分析，用户群分析，行为模式分析
        - 微信小程序
        - 做一个公众号
        - 八爪鱼
        - 用python写爬虫
        - Echarts 在线作图工具
        - vlookup
        - Tabuleau
        - ElasticSearch
        - html设计表格
        - 定时发送邮件（邮件正文和附件是数据库查询结果）
        - 用户画像（登录城市，年龄，性别，统计分布）
        - 风险评估
        - 用户预流失模型预测
        - 微信聊天定时发送（定时提醒早晚安，吃饭，生日，天气）
        - 企业微信机器人推送消息（数据告警，打卡、天气提醒）
        - 企业微信群发功能（接收人列表，不是群机器人）
        

## 数据科学部 DS
        1. 司机招募
        2. 模板
        3. hive 分区查询（每日全量，每日增量）
        4. 双班&经租司机现状——分析双班制的可行性
        5. 用户画像
        6. 用研需求分析数据支持
### 具体的case
1. 合规车型
                活跃司机车型命中所在城市车型库，为合规，全国不合规比例约为29%，为安全部门清除车辆/车型库城市下探——提供数据支撑
                全国订单topN的车型，采购更新车型库照片
2. 双班司机&经租司机现状
                出租车、快车、优享、专车 9月活跃司机中，分业务线、全兼职、区域、带车/无车来看，司机的规模、占比、月在线时长、月收入等
                双班司机约占40%，人均日在线时长低但IPH（每小时收入）高于非双班司机，说明双班制的可行性。向非双班司机做调查，反馈结果表明：非双班司机中3成不了解双班制，对于不愿意实行双班制的原因主要有：收入、兼职司机本身有工作、时间自由灵活、健康、爱惜自己的车、合作伙伴的责任划分
                经租10%
3. 经租司机双班制可行性研究分析
                近30天活跃司机中——分城市、经租非双班/经租双班/大盘（非经租）、在线时长分类（0-50-100-200-h），查看活跃司机数，在线时长、收入、tph、iph、分时段的iph
4. 女性司机分析
                活跃司机中，女性司机11w（约占3.4%），全职比例略低于男性（-4pp）
                留存率更低（71%，-7pp）
                平均年龄更大（38.3，大2岁，集中在30~45，男性集中在25~40）
                TPH更高（+3%），IPH更低（-4%）——平台派单规则：女性司机订单数多（+11pp）,短单多（+2pp）——订单多，每单时间短
                夜间时段订单高（65%>35%）
                夜间（18：00~5：00）出车意愿低——在线率低（-10pp）
                取消率低（0.8%，-0.2pp）
                服务分低（比男性司机，服务分-1.5分，差评率+0.08pp, 投诉率+0.08pp）——路不熟/绕路、服务态度恶劣、打电话玩手机、司机投诉乘客
                对平台满意度更高——NPS
5. 用研分析数据：留存-沉默-流失
                定义中长期留存司机、流失司机、近期注册沉默司机中的全兼职类型，提供司机的个人信息及在线时长、完单量、收入流水数据等
6. 线上视频面试
                预约面试-进入面试-完成面试-面试成功（失败原因，人均预约面试时长，人均面试时长）-激活-在线-首单-人均日TSH
                截止当前转化率、审核通过7/14/21/28日转化率、日流速数据、面试失败人数
7. 感恩节活动——乘转司
                招募过程流转统计




## 实习经历
![实习经历01](https://github.com/ElsaQf/LearningDataScienceIntern/blob/master/PicturesUsing/%E5%AE%9E%E4%B9%A0%E7%BB%8F%E5%8E%8601.JPG)
#### 实习内容
        - 日常数据查询和分析工作：产品、运营、开发对接
                + 询问需求（最近收入下降了，原因？）
                + 分析（放贷政策，大环境，资金周转问题，骗贷）
                + 数据支撑（结果数据，tableau可视化，图表展示）
                + 结论和建议
        - 数据爬取和清洗
                + 工具：BeautifulSoup, DataFrame, 八爪鱼
        - 用户画像
                + 针对某一段时间内的用户，统计年龄、性别、登录城市的分布
        - 分析用户行为
                + 场景1：例如产品到期，需要展期，会根据原始订单金额确定展期费用，查看用户是否完成整个行为事件？中止在哪一步？
                + 中止在付款页——手续费定价高——产品定价策略
                + 中止在选择页——有可能是不会操作——运营、客服指导
                + 当天终止订单且无后续操作——换平台——运营及时干预
                + 场景2：产品展期的金额、时间分布
                + 结果：大部分用户选择在到期当天展期，针对即将到期的用户发送展期提醒
        - 自动发送邮件周报，包含每周的统计数据（每周新增用户数，活跃用户数，收入总额，环比增幅），减少部门工作量
        - 开发告警机器人，企业微信群机器人和授权应用，实时监测
