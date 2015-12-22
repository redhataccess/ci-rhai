#!/usr/bin/env bash
pip install -U -r requirements.txt nose PyVirtualDisplay

cp ${ROBOTTELO_CONFIG} ./robottelo.properties

sed -i "s/{server_hostname}/${SERVER_HOSTNAME}/" robottelo.properties

# Robottelo logging configuration
sed -i "s/'\(robottelo\).log'/'\1-rhai.log'/" logging.conf

make test-foreman-rhai

