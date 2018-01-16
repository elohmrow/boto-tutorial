import boto.ec2

class Connection:
    def __init__(self):
        ''' Connection Instance '''
        self.region = 'eu-central-1'

    def ec2Connection(self):
        ''' Create an return an EC2 Connection '''
        conn = boto.ec2.connect_to_region(self.region)
        return conn
