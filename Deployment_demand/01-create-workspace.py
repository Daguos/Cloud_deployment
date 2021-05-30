from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace

interactive_auth = InteractiveLoginAuthentication(tenant_id='a1b3008e-5732-4f15-8292-cf478f19c818')
ws = Workspace.create(
    name='azure-ml-demand',
    subscription_id='d916feb2-5bfe-41e6-9c49-b315b78d95c0',
    resource_group='demand_machine_learning',
    create_resource_group=True,
    location='eastus2',
    auth=interactive_auth
)

ws.write_config(path='.azureml')