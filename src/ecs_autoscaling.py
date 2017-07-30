import sys, os
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')
sys.path.append(vendor_dir)

import logging, datetime, json
import boto3

# Configure logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(os.environ.get('LOG_LEVEL','INFO'))
def format_json(data):
  return json.dumps(data, default=lambda d: d.isoformat() if isinstance(d, datetime.datetime) else str(d))

ECS_CLUSTER_ARN = os.environ.get('ECS_CLUSTER_ARN')
AUTOSCALING_GROUP = os.environ.get('AUTOSCALING_GROUP')
CONTAINER_MAX_MEMORY = os.environ.get('CONTAINER_MAX_MEMORY')
CONTAINER_MAX_CPU = os.environ.get('CONTAINER_MAX_CPU')
TCP_PORT_RESOURCES = os.environ.get('TCP_PORT_RESOURCES')
UDP_PORT_RESOURCES = os.environ.get('UDP_PORT_RESOURCES')

# Lambda handler function
def handler(event, context):

  # This is the event we will be processing
  {
    "account": "543279062384", "region": "us-west-2", 
    "detail": {
      "status": "ACTIVE", 
      "registeredAt": "2017-07-30T02:36:50.591Z", 
      "registeredResources": [
        {"type": "INTEGER", "name": "CPU", "integerValue": 1024}, 
        {"type": "INTEGER", "name": "MEMORY", "integerValue": 993}, 
        {"stringSetValue": ["22", "2376", "2375", "51678", "51679"], "type": "STRINGSET", "name": "PORTS"}, 
        {"stringSetValue": [], "type": "STRINGSET", "name": "PORTS_UDP"}
      ], 
      "ec2InstanceId": "i-06cb96155228d49d6", 
      "agentConnected": true, 
      "containerInstanceArn": "arn:aws:ecs:us-west-2:543279062384:container-instance/0606dc43-fd6a-4837-a4f1-0a5ec2f2d6fe", 
      "remainingResources": [
        {"type": "INTEGER", "name": "CPU", "integerValue": 1024}, 
        {"type": "INTEGER", "name": "MEMORY", "integerValue": 993}, 
        {"stringSetValue": ["22", "2376", "2375", "51678", "51679"], "type": "STRINGSET", "name": "PORTS"}, 
        {"stringSetValue": [], "type": "STRINGSET", "name": "PORTS_UDP"}
      ], 
      "version": 2, 
      "clusterArn": "arn:aws:ecs:us-west-2:543279062384:cluster/microtrader-development-ApplicationCluster-1WI6BZ50YXJS4", 
      "updatedAt": "2017-07-30T02:36:50.629Z", 
      "attributes": [], 
      "versionInfo": {"agentVersion": "1.14.3", "agentHash": "15de319", "dockerVersion": "DockerVersion: 17.03.1-ce"}
    }, 
    "detail-type": "ECS Container Instance State Change", 
    "source": "aws.ecs", 
    "version": "0",
    "time": "2017-07-30T02:36:50Z", 
    "id": "d5c8131c-b7c1-44dd-8ab4-d2cf4dc0b736", 
    "resources": ["arn:aws:ecs:us-west-2:543279062384:container-instance/0606dc43-fd6a-4837-a4f1-0a5ec2f2d6fe"]
  }

  # Check detail-type = "ECS Container Instance State Change"
  # Check detail['clusterArn'] matches configure ECS_CLUSTER_ARN environment variable
  # Check agentConnect 


  log.info("Received event: %s" % format_json(event))