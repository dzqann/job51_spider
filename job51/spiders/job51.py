import scrapy
from job51.items import Job51Item
from scrapy.http import Request  # 爬取一个网页
import re
import json


# 所有的导入都从核心目录开始导入

class Job51Spider(scrapy.Spider):
    name = 'job51'
    allowed_domains = ['51job.com']

    def start_requests(self):
        base_url = "https://search.51job.com/list/211200%252c010000,000000,0000,00,9,99,%25E7%25A1%25AC%25E4%25BB%25B6,2,{}.html?"
        for i in range(1, 155):
            yield Request(url=base_url.format(i), callback=self.parse)

    def parse(self, response):
        job_json = re.findall(r"window.__SEARCH_RESULT__ = ([\s\S]*?)</script", response.text, re.S)
        if len(job_json) <= 0:
            return
        job_json = json.loads(job_json[0])
        for each_job in job_json['engine_search_result']:
            item = Job51Item()
            item['job_name'] = each_job['job_name']
            item['salary'] = each_job['providesalary_text']
            item['update_date'] = each_job['updatedate']
            item['company_name'] = each_job['company_name']
            item['company_type'] = each_job['companyind_text']
            item['work_address'] = each_job['workarea_text']
            item['company_size'] = each_job['companytype_text']
            item['welfare'] = ";".join(each_job['jobwelf_list'])
            item['job_href'] = each_job['job_href']
            yield Request(url=each_job['job_href'], callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        position_information = ";".join(response.xpath("//div[@class='bmsg job_msg inbox']/p/text()").extract())
        office_address = ";".join(response.xpath("//div[@class='bmsg inbox']/p/text()").extract())
        company_information = ";".join(response.xpath("//div[@class='tmsg inbox']/text()").extract())
        item['position_info'] = position_information  # 包括岗位职责和任职要求
        item['office_address'] = office_address  # 联系方式
        item['company_info'] = company_information  # 公司信息
        return item
