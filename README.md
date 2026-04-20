## Multi-Cloud Sentinel
Multi-Cloud Sentinel is a governance and observability framework designed to unify infrastructure management across AWS (us-east-1) and OCI (af-johannesburg-1). It bridges the gap between disparate cloud providers by enforcing a Standard Operating Environment (SOE) using Ubuntu 22.04 LTS and a "Single Pane of Glass" monitoring strategy.

### Core Features
Standardized IaC: Automated provisioning of Ubuntu nodes across AWS and OCI using Terraform.

FinOps Guardrails: Integrated Infracost in CI/CD to analyze cost impact on every Pull Request.

Automated Remediation: A Python-based "Zombie Reaper" that audits global resources via Boto3 and OCI-SDK to enforce mandatory tagging.

Unified Observability: Real-time CPU and health telemetry consolidated into a Grafana Cloud dashboard.

### Tech Stack
Cloud: AWS, Oracle Cloud Infrastructure (OCI)

OS: Ubuntu 22.04 LTS

IaC: Terraform

CI/CD: GitHub Actions

Automation: Python 3.10 (Boto3, OCI-SDK)

Monitoring: Grafana Cloud, CloudWatch, OCI Monitoring

### Project Structure
```
.
├── .github/workflows/       # CI/CD pipelines (Infracost & Governance)
├── scripts/
│   └── reaper.py            # Python automation for resource auditing
├── terraform/
│   ├── main.tf              # Multi-cloud provider & resource definitions
│   └── variables.tf         # Environment configuration
└── README.md
```

### Observability: The Single Pane of Glass
The dashboard provides a correlated view of regional performance. By standardizing on Ubuntu and utilizing native cloud exporters, we achieve sub-5-minute latency in global metric visualization.

### Getting Started
Clone the Repo:

```Bash
git clone https://github.com/aashiruu/multi-cloud-sentinel.git
```
Initialize Infrastructure:

```Bash
cd terraform
```
```
terraform init
```
```
terraform apply
```
Run Governance Audit:

```Bash
python3 scripts/reaper.py
```

## Screenshots
### The Brain (Infrastructure as Code)
<img width="985" height="633" alt="17767010078885222331689435319303" src="https://github.com/user-attachments/assets/29e8089a-351e-42ef-88dd-4154cf1c45e1" />
Defining a standardized multi-cloud environment using Terraform for consistent, repeatable deployments across AWS and OCI.

### The Guardrail (CI/CD & FinOps)
<img width="1337" height="655" alt="17767009244363797741423150154725" src="https://github.com/user-attachments/assets/3f3a4d2b-3f4f-4324-84ea-d0f68f909f01" />
Integrated FinOps guardrails using Infracost. Every pull request is automatically analyzed for cost impact, preventing 'cloud bill shock' before code is merged.

### Python Automation
<img width="623" height="328" alt="17767011333868064568927854225127" src="https://github.com/user-attachments/assets/d4cae8c9-c111-414b-8b49-4ee583048c95" />
Custom Python 'Zombie Reaper' utilizing Boto3 and OCI-SDK to automatically audit and remediate non-compliant resources missing mandatory project tags.

### Global Observability
<img width="1363" height="648" alt="17767012307474433083721045936350" src="https://github.com/user-attachments/assets/2b273f71-1600-4a65-9c0b-098d806c7ba6" />
A centralized Grafana 'Single Pane of Glass' visualizing real-time metrics from Virginia (AWS) and Johannesburg (OCI) simultaneously.
