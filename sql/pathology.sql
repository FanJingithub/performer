use MData;

grant select, insert, update, delete on MData.* to 'debian-sys-maint'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table pathology (
    `patient_id`  varchar(20) default '',
    `patho_diagnosis`  varchar(20) default '',
    `lym_vas_invasion`  varchar(20) default '',
    `tot_lymph_node`  varchar(20) default '',
    `deep`  varchar(20) default '',
    `pni`  varchar(20) default '',
    `pos_lymph_node`  varchar(20) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
