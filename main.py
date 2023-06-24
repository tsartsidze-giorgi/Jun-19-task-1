import argparse


parser = argparse.ArgumentParser(description="CLI script")
subparsers = parser.add_subparsers(title="Commands", dest="command")


bucket_parser = subparsers.add_parser("bucket", help="Organize files in a bucket")
bucket_parser.add_argument("name", help="Name of the storage")

rds_parser = subparsers.add_parser("rds", help="Update RDS DB password")
rds_parser.add_argument("-new_pass", required=True, help="New DB password")
rds_parser.add_argument("-dbInstanceId", required=True, help="DB Instance Identifier")


ec2_parser = subparsers.add_parser("ec2", help="Launch EC2 instance")


ec2_parser.add_argument("-launch_instance", action="store_true", help="Launch EC2 instance")
ec2_parser.add_argument("--memory", default="4GB", help="Memory size")
ec2_parser.add_argument("--memory_type", default="gp2", help="Memory type")
ec2_parser.add_argument("--instance_type", default="t2.micro", help="Instance type")
ec2_parser.add_argument("--ami", default="ami-053b0d53c279acc90", help="AMI ID")

args = parser.parse_args()


if args.command == "bucket":
    print(f"Organizing files in bucket: {args.name}")
   
elif args.command == "rds":
    print(f"Updating RDS DB password for DB Instance: {args.dbInstanceId}")
   
    if len(args.new_pass) >= 4:
        
        print("RDS password updated successfully.")
    else:
        print("New password must be at least 4 characters long.")


elif args.command == "ec2":
    if args.launch_instance:
        print("Launching EC2 instance...")
        print(f"Memory: {args.memory}")
        print(f"Memory type: {args.memory_type}")
        print(f"Instance type: {args.instance_type}")
        print(f"AMI ID: {args.ami}")
       
    else:
        print("No action specified for 'ec2' command.")


else:
    print("No command specified.")
