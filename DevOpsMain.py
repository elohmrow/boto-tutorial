#!/usr/bin/env python

from aws import Connection
from aws import EC2Instance

connInst = Connection()
conn = connInst.ec2Connection()

ec2 = EC2Instance()
ec2.list_instances(conn)
