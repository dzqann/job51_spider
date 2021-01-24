# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql


class Job51Pipeline:

    def __init__(self):
        # 为整个类创建一个db连接
        self.con = pymysql.connect(host='localhost', user='root', password='root', database='job51')
        self.cursor = self.con.cursor()
        self.base_sql = "insert into job(job_name, salary, update_date, company_name, company_type, work_address, " \
                        "company_size, welfare, job_href, position_info, office_address, company_info) " \
                        "values('{job_name}', '{salary}', '{update_date}', '{company_name}', '{company_type}', " \
                        "'{work_address}', '{company_size}', '{welfare}', '{job_href}', '{position_info}', '{office_address}', '{company_info}');"

    def process_item(self, item, spider):
        try:
            sql = self.base_sql.format(
                job_name=item['job_name'],
                salary=item['salary'],
                update_date=item['update_date'],
                company_name=item['company_name'],
                company_type=item['company_type'],
                work_address=item['work_address'],
                company_size=item['company_size'],
                welfare=item['welfare'],
                job_href=item['job_href'],
                position_info=item['position_info'],
                office_address=item['office_address'],
                company_info=item['company_info']
            )
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            print(str(e))
        return item
