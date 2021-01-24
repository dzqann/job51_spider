create table job
(
    id             bigint(20) auto_increment primary key,
    job_name       varchar(500)  default null,
    salary         varchar(100)  default null,
    update_date    varchar(100)  default null,
    company_name   varchar(100)  default null,
    company_type   varchar(100)  default null,
    work_address   varchar(500)  default null,
    company_size   varchar(100)  default null,
    welfare        text          default null,
    job_href       varchar(1000) default null,
    position_info  text          default null,
    office_address varchar(1000) default null,
    company_info   text          default null
);