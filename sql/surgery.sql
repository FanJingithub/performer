use MData;

grant select, insert, update, delete on MData.* to 'fanjin'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table surgery (
    `patient_id`  varchar(12) default '',
    `resection_way`  varchar(12) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
