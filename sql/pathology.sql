use MData;

grant select, insert, update, delete on MData.* to 'fanjin'@'localhost' identified by 'fmvKL0UlQ558lKWG';

create table pathology (
    `patient_id`  varchar(12) default '',
    `patho_diagnosis`  varchar(12) default '',
    `lym_vas_invasion`  varchar(12) default '',
    `tot_lymph_node`  varchar(12) default '',
    `deep`  varchar(12) default '',
    `pni`  varchar(12) default '',
    `pos_lymph_node`  varchar(12) default '',
    primary key(patient_id)
) engine=innodb         default charset=utf8;
