import pulumi
import pulumi_aws as aws
import yaml

with open("inputs.yaml") as yamlfile:
  input_data = yaml.load(yamlfile, Loader=yaml.FullLoader)


main_vpc_1 = aws.ec2.Vpc(
    "main-vpc-1",
    cidr_block=input_data["config"]["primary_cidr"],
    instance_tenancy="default",
    enable_dns_hostnames=True,
    enable_dns_support=True,
    tags={
        "Name": input_data["config"]["name"]
          }
    )

for each_subnet in input_data["config"]["subnet_data"]:
  subnets = aws.ec2.Subnet(
      each_subnet["name"],
      vpc_id=main_vpc_1.id,
      cidr_block=each_subnet["cidr"],
      availability_zone_id = each_subnet["az_id"],
      tags={
          "Name": each_subnet["name"]
          }
    )
