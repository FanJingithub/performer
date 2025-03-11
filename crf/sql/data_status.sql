use CRF;


drop table if exists data_status;

create table data_status (
    `patient_id`  varchar(12)  default '',
    `base`  varchar(20) default "0",
    `physical_exam`  varchar(20) default "0",
    `lab`  varchar(20) default "0",
    `special_exam`  varchar(20) default "0",
    `before_evaluate`  varchar(20) default "0",
    `after_evaluate`  varchar(20) default "0"
) engine=innodb         default charset=utf8;
