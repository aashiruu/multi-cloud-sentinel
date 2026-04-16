terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    oci = {
      source  = "oracle/oci"
      version = "~> 5.0"
    }
  }
}

# AWS Provider Configuration
provider "aws" {
  region = "us-east-1"
}

# OCI Provider Configuration
provider "oci" {
  tenancy_ocid     = "ocid1.tenancy.oc1..aaaaaaaaybnmkqe3vpwmlsu7vkxy2yc2dc4q3vwk2jlplb2uzgycvabwy5ba"
  user_ocid        = "ocid1.user.oc1..aaaaaaaahzc6lkqcxdvj7pjremwjywhhu2ma2ug5iweoptfsthsuw5hcxerq"
  fingerprint      = "2c:f2:ea:c8:f7:59:90:12:c4:58:8d:c3:ba:d1:76:97"
  private_key_path = "/home/famous/.oci/oci_api_key.pem"
  region           = "af-johannesburg-1"
}

data "aws_caller_identity" "current" {}

output "aws_account_id" {
  value = data.aws_caller_identity.current.account_id
}

resource "aws_instance" "expensive_server" {
  ami           = "ami-0c55b159cbfafe1f0" # Standard Amazon Linux 2
  instance_type = "m5.4xlarge"           # This costs ~$500/month

  tags = {
    Name = "BudgetBreaker"
  }
}
