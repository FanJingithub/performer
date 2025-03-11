#!/bin/bash
    sudo -S cp ../nginx/CRF /etc/nginx/sites-enabled/ << EOF
cvm@fj123
EOF

sudo -S mkdir /srv/MData_all/CRF/log << EOF
cvm@fj123
EOF

sudo -S /etc/init.d/nginx reload << EOF
cvm@fj123
EOF
    