#!/bin/bash


sudo -S rm -f -R /srv/MData_all/CRF << EOF
cvm@fj123
EOF

sudo -S mkdir /srv/MData_all/CRF << EOF
cvm@fj123
EOF

sudo -S cp -R /home/ubuntu/web//crf /srv/MData_all/CRF/www << EOF
cvm@fj123
EOF

sudo chmod 777 -R /srv/MData_all/CRF << EOF
cvm@fj123
EOF
    