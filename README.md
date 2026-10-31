# AWS VAPT Mini Project

A mini project on Vulnerability Assessment and Penetration Testing (VAPT) concepts using Amazon Web Services (AWS), focusing on EC2 instances, S3 storage, and cloud security configurations.

## Project Overview

This project explores basic AWS infrastructure and security practices. It covers the configuration of EC2 instances, S3 buckets, access control mechanisms, and common cloud security risks.

The objective is to understand how AWS resources can be configured securely and how misconfigurations may expose cloud infrastructure to potential threats.

## Objectives

- Understand Amazon EC2 instances and their configurations.
- Learn about EC2 instance types and key-pair authentication.
- Understand Security Groups and Network Access Control Lists (NACLs).
- Explore Amazon S3 buckets and object storage.
- Understand IAM policies and S3 bucket policies.
- Identify common AWS security misconfigurations.
- Document practical exercises and security observations.

## Technologies Used

- Amazon Web Services (AWS)
- Amazon EC2
- Amazon S3
- AWS Identity and Access Management (IAM)
- GitHub
- Markdown

## 1. Amazon EC2

Amazon Elastic Compute Cloud (EC2) provides virtual servers for running applications in the AWS cloud.

### Concepts Covered

- EC2 instance creation and configuration
- Instance types and their purposes
- Key-pair authentication
- Security Groups and inbound/outbound traffic rules
- Connecting to and managing instances

### Security Considerations

- Allow only necessary inbound traffic.
- Avoid exposing administrative services to the entire internet.
- Protect private key files used for authentication.
- Stop or terminate unused instances when appropriate.
- Review security rules regularly.

## 2. Amazon S3

Amazon Simple Storage Service (S3) is an object storage service used for storing and retrieving data.

### Concepts Covered

- S3 bucket creation
- Uploading and managing objects
- Bucket permissions
- IAM policies and bucket policies
- Public access configuration

### Security Considerations

- Keep Block Public Access enabled unless public access is specifically required.
- Apply least-privilege permissions.
- Avoid storing confidential information in publicly accessible buckets.
- Review bucket policies and access permissions.
- Enable versioning when appropriate for data recovery.

## 3. AWS Security Concepts

### Security Groups

Security Groups act as stateful virtual firewalls associated with AWS resources such as EC2 instances. They control permitted inbound and outbound traffic.

### Network Access Control Lists (NACLs)

NACLs operate at the subnet level and are stateless. They support both allow and deny rules.

### IAM Policies

IAM policies define which actions identities can perform on AWS resources.

### S3 Bucket Policies

Bucket policies are resource-based policies attached to S3 buckets. They specify which principals can access the bucket and what actions they may perform.

## 4. Vulnerability Assessment Approach

The project follows a basic security review process:

1. Identify the AWS resources included in the assessment.
2. Review EC2 instance configurations and network exposure.
3. Examine Security Group rules and relevant network controls.
4. Review S3 bucket permissions and public access settings.
5. Identify potential security misconfigurations.
6. Record evidence using screenshots with sensitive information removed.
7. Document findings and recommend corrective actions.

All assessment activities should be performed only on AWS resources you own or are explicitly authorized to assess.

## 5. Findings and Recommendations

Record actual findings from your practical assessment in the following format.

| Finding | Risk | Recommendation |
|---|---|---|
| Unnecessary inbound ports | Increased attack surface | Restrict access to required ports and trusted sources |
| Unintended public S3 access | Potential data exposure | Enable Block Public Access and review bucket policies |
| Excessive IAM permissions | Unauthorized actions may become possible | Apply least-privilege permissions |
| Exposed private key | Unauthorized access risk | Keep private keys secure and never commit them to GitHub |

These are example risks to investigate, not confirmed vulnerabilities in the assessed environment.

## 6. Evidence and Screenshots

Add screenshots of your actual practical work to the relevant folders.

Suggested evidence includes:

- EC2 instance configuration
- Security Group inbound rules
- S3 bucket configuration
- S3 Block Public Access settings
- Relevant policy configurations
- Findings and remediation evidence

Remove passwords, private keys, access tokens, and other sensitive information before uploading screenshots.

## 7. Conclusion

This project provides practical exposure to AWS cloud infrastructure and fundamental cloud security concepts. It demonstrates the importance of reviewing access controls, network exposure, storage permissions, and security configurations.

The assessment findings should be based on actual observations from the AWS environment, supported by appropriate evidence and remediation recommendations.

## References

- [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)
- [AWS Identity and Access Management Documentation](https://docs.aws.amazon.com/iam/)
- [AWS Security Documentation](https://docs.aws.amazon.com/security/)

---

**Note:** This repository documents a learning project. Actual assessment results, screenshots, and remediation outcomes should be added as the practical work is completed.
