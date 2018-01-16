import boto.ec2

class EC2Instance:
    def __init__(self):
        ''' EC2Instance Constructor '''

    def list_instances(self,conn):
        ''' List EC2 Instances '''
        # get all instance reservations associated with this AWS account
        reservations = conn.get_all_reservations()

        # loop through reservations and extract instance information
        for r in reservations:
            #get all instances from the reservation
            instances = r.instances

            # loop through instances and print instance information
            for i in instances:
                # print i.__dict__ # <-- print everything about this instance
                # get instance name from the tags object
                tags = i.tags
                instancename = 'Default EC2 Instance Name'

                #check for Name property in tags object
                if 'Name' in tags:
                    instancename = tags['Name']

                #print instance information
                print 'Instance Name:', instancename, ' Instance Id:', i.id, ' State:', i.state
