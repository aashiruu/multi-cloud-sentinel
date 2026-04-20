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

## Project Structure
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

## Observability: The Single Pane of Glass
The dashboard provides a correlated view of regional performance. By standardizing on Ubuntu and utilizing native cloud exporters, we achieve sub-5-minute latency in global metric visualization.
