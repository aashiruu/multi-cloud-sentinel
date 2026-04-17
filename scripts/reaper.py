import boto3
import oci
import sys

def audit_aws():
    print("--- 🔍 Auditing AWS (us-east-1) ---")
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for instance in instances:
        tags = instance.tags or []
        has_project_tag = any(t['Key'] == 'Project' for t in tags)

        if not has_project_tag:
            print(f"⚠️  ZOMBIE FOUND: AWS Instance {instance.id} is missing a 'Project' tag!")
            fix_zombie_aws(instance)
        else:
            print(f"✅ Instance {instance.id} is compliant.")

def audit_oci():
    print("\n--- 🔍 Auditing OCI (af-johannesburg-1) ---")
    config = oci.config.from_file()
    compute_client = oci.core.ComputeClient(config)

    compartment_id = config['tenancy']
    list_instances = compute_client.list_instances(compartment_id).data

    for instance in list_instances:
        if instance.lifecycle_state == "RUNNING":
            tags = instance.freeform_tags or {}

            if 'Project' not in tags:
                print(f"⚠️  ZOMBIE FOUND: OCI Instance {instance.display_name} is missing a 'Project' tag!")
                fix_zombie_oci(compute_client, instance)
            else:
                print(f"✅ Instance {instance.display_name} is compliant.")

def fix_zombie_oci(compute_client, instance):
    print(f"🔧 Fixing {instance.display_name}...")
    new_tags = instance.freeform_tags or {}
    new_tags['Project'] = 'Auto-Reaped'
    new_tags['Status'] = 'Non-Compliant-Fixed'

    compute_client.update_instance(
        instance_id=instance.id,
        update_instance_details=oci.core.models.UpdateInstanceDetails(
            freeform_tags=new_tags
        )
    )
    print(f"✅ {instance.display_name} has been tagged and secured.")

def fix_zombie_aws(instance):
    print(f"🔧 Tagging AWS Instance {instance.id}...")
    instance.create_tags(Tags=[
        {'Key': 'Project', 'Value': 'Auto-Reaped'},
        {'Key': 'Status', 'Value': 'Non-Compliant-Fixed'}
    ])
    print(f"✅ AWS Instance {instance.id} secured.")

if __name__ == "__main__":
    try:
        audit_aws()
        audit_oci()
    except Exception as e:
        print(f"❌ Error: {e}")
