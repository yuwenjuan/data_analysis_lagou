# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName = Field()        # 职位名称
    month_salary= Field()         # 薪资水平
    companyName = Field()         # 公司名称
    companyField=Field()          # 公司服务领域
    companySize=Field()           #公司规模
    city = Field()                # 工作地点
    experience=Field()            #经验要求
    qualification=Field()         #学历要求
    full_or_parttime=Field()      #全职/兼职
    detailLink=Field()           #职位详情页连接




