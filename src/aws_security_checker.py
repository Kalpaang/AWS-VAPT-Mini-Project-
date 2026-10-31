import boto3
from botocore.exceptions import ClientError, NoCredentialsError


def check_ec2_security_groups(ec2):
    """Check EC2 security groups for potentially risky inbound rules."""

    print("\n=== EC2 Security Group Assessment ===")

    try:
        response = ec2.describe_security_groups()

        for group in response["SecurityGroups"]:
            group_id = group["GroupId"]
            group_name = group["GroupName"]

            print(f"\nSecurity Group: {group_name} ({group_id})")

            risky_rule_found = False

            for permission in group.get("IpPermissions", []):
                protocol = permission.get("IpProtocol", "")
                from_port = permission.get("FromPort")
                to_port = permission.get("ToPort")

                for ip_range in permission.get("IpRanges", []):
                    cidr = ip_range.get("CidrIp")

                    if cidr == "0.0.0.0/0":
                        if protocol == "-1":
                            print(
                                "[WARNING] All protocols are allowed "
                                "from the internet."
                            )
                            risky_rule_found = True

                        elif from_port == 22:
                            print(
                                "[WARNING] SSH (port 22) is open "
                                "to the internet."
                            )
                            risky_rule_found = True

                        elif from_port == 3389:
                            print(
                                "[WARNING] RDP (port 3389) is open "
                                "to the internet."
                            )
                            risky_rule_found = True

                        elif protocol == "tcp" and from_port == 0:
                            print(
                                "[WARNING] A TCP rule starting at "
                                "port 0 is open to the internet."
                            )
                            risky_rule_found = True

            if not risky_rule_found:
                print(
                    "No checked high-risk inbound rules were detected. "
                    "This is not a complete security audit."
                )

    except ClientError as error:
        print(f"[ERROR] Could not assess EC2: {error}")


def check_s3_buckets(s3):
    """Review S3 bucket public-access protection."""

    print("\n=== S3 Bucket Assessment ===")

    try:
        response = s3.list_buckets()

        for bucket in response.get("Buckets", []):
            bucket_name = bucket["Name"]
            print(f"\nBucket: {bucket_name}")

            try:
                result = s3.get_public_access_block(
                    Bucket=bucket_name
                )

                settings = result["PublicAccessBlockConfiguration"]

                if all(settings.values()):
                    print(
                        "[OK] All four S3 Block Public Access "
                        "settings are enabled."
                    )
                else:
                    print(
                        "[WARNING] One or more Block Public Access "
                        "settings are disabled."
                    )

            except ClientError as error:
                code = error.response.get("Error", {}).get("Code", "")

                if code in (
                    "NoSuchPublicAccessBlockConfiguration",
                    "NoSuchConfiguration"
                ):
                    print(
                        "[WARNING] Bucket-level Block Public Access "
                        "configuration was not found. Check account-level "
                        "settings and bucket policies before assessing risk."
                    )
                else:
                    print(
                        "[ERROR] Could not inspect public-access settings: "
                        f"{error}"
                    )

    except ClientError as error:
        print(f"[ERROR] Could not list S3 buckets: {error}")


def main():
    print("AWS VAPT Mini Project")
    print("Read-only configuration assessment")
    print("Region: us-east-1")
    print("Only assess AWS accounts you are authorized to inspect.")

    try:
        session = boto3.Session(region_name="us-east-1")
        ec2 = session.client("ec2")
        s3 = session.client("s3")

        check_ec2_security_groups(ec2)
        check_s3_buckets(s3)

    except NoCredentialsError:
        print(
            "\n[ERROR] AWS credentials were not found. "
            "Configure credentials securely before running the checker."
        )
    except Exception as error:
        print(f"\n[ERROR] Assessment could not be completed: {error}")


if __name__ == "__main__":
    main()
