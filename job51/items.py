# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    job_name = scrapy.Field()      #工作名称
    salary = scrapy.Field()   #工资
    update_date = scrapy.Field()    #发布时间
    company_name = scrapy.Field()    #公司名称
    company_type = scrapy.Field() #公司类型
    work_address = scrapy.Field()    #工作地点
    company_size = scrapy.Field()   #公司人数
    welfare = scrapy.Field()            #公司待遇福利
    job_href = scrapy.Field()           #链接
    position_info = scrapy.Field()   # 包括岗位职责和任职要求
    office_address = scrapy.Field()  # 联系方式
    company_info = scrapy.Field()  # 公司信息
