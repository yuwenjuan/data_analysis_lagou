# -*- coding: utf-8 -*-
import scrapy
import json
from Lagou.items import LagouItem
class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/']

    def start_requests(self):
        #关于ajax真实的url分析，参考博文：https://blog.csdn.net/dta0502/article/details/82083391
        url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        #构造请求头
        my_header={'Host':'www.lagou.com',
                    'Origin':'https://www.lagou.com',
                    'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=',
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                    }
        full_url=[]
        #range是查询的页码范围，构造翻页的url
        for i in range (1,31):
            #提交的表单
            my_formdata={'first':'false','pn':str(i),'kd':'数据分析'}
            req=scrapy.FormRequest(url,headers=my_header,formdata=my_formdata,callback=self.parse)
            full_url.append(req)
        return full_url


    def parse(self, response):
        #json.loads()将字符串转换成字典.然后通过键找到对应的值
        jsonBody=json.loads(response.body.decode())
        #jsonBody为：{'':'' , '':'' , '':'' , '':{'':'',  ......}}这样的格式
        results=jsonBody['content']['positionResult']['result']
        items=[]
        for result in results:
            item=LagouItem()
            item['positionName'] = result['positionName']        # 职位名称
            item['month_salary']= result['salary']              # 薪资水平
            item['companyName'] =result['companyFullName']         # 公司名称
            item['companyField']=result['industryField']          # 公司所属行业
            item['companySize']=result['companySize']           #公司规模
            item['city'] = result['city']                        # 工作地点
            item['experience']=result['workYear']             #经验要求
            item['qualification']=result['education']          #学历要求
            item['full_or_parttime']=result['jobNature']       #全职/兼职
            item['detailLink']="https://www.lagou.com/jobs/"+str(result['positionId'])+".html"    #职位详情页连接               #职位描述
            items.append(item)
        return items
