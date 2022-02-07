from azureml.core import Workspace
from azureml.core.compute import AmlCompute, ComputeTarget
from azureml.core.compute_target import ComputeTargetException

cluster_name = "gpu-cluster"
max_nodes = 2

ws = Workspace.from_config()

try:

    # Check for existing compute target
    cluster = ComputeTarget(workspace=ws, name=cluster_name)
    print("Cluster already exist")

except ComputeTargetException:

    # If it doesn't already exist, create it
    try:
        compute_config = AmlCompute.provisioning_configuration(
            vm_size="Standard_NC6_Promo", max_nodes=max_nodes
        )
        cluster = ComputeTarget.create(ws, cluster_name, compute_config)
        cluster.wait_for_completion(show_output=True)
    except Exception as ex:
        print(ex)
