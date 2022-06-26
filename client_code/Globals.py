import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from dataclasses import dataclass

number_of_clicks = 0

onbordings = [
{
  "app_code": "abc1",
  "app_name": "abc1",
  "cloud_provider": "azure",
  "created_at": "Wed, 15 Jun 2022 22:53:26 GMT",
  "environments": [],
  "id": 10,
  "portfolio": "ccoe",
  "request": "{\"cloud_provider\": \"azure\", \"app_name\": \"abc1\", \"portfolio\": \"ccoe\", \"transit_code\": \"0001\", \"state\": \"received\", \"tfe\": \"nonp-dev\", \"environments\": [{\"name\": \"dev\", \"tfe_agent_vm_sku\": \"Standard_B4ms\", \"agents_enabled\": \"true\", \"tfe_agents_count\": \"1\", \"tfe_agent_version\": \"1.1.0\", \"soe_image_version\": \"0.1.9\", \"resources\": [{\"name\": \"e0042\", \"type\": \"subscription\", \"id\": \"e4d170ca-1efa-48fd-9c6d-e5ab911525cd\"}]}, {\"name\": \"qat\", \"tfe_agent_vm_sku\": \"Standard_B4ms\", \"agents_enabled\": \"false\", \"tfe_agents_count\": \"1\", \"tfe_agent_version\": \"1.1.8\", \"soe_image_version\": \"0.1.19\", \"resources\": [{\"name\": \"n0004ss\", \"type\": \"subscription\", \"id\": \"3823da9a-f968-433c-aa9c-1b623a79c44e\"}]}, {\"name\": \"uat\", \"tfe_agent_vm_sku\": \"Standard_B1s\", \"agents_enabled\": \"false\", \"tfe_agents_count\": \"1\", \"tfe_agent_version\": \"1.1.5\", \"soe_image_version\": \"0.1.19\", \"resources\": null}, {\"name\": \"prod\", \"tfe_agent_vm_sku\": \"Standard_B1s\", \"agents_enabled\": \"false\", \"tfe_agents_count\": \"1\", \"tfe_agent_version\": \"1.1.5\", \"soe_image_version\": \"0.1.19\", \"resources\": null}], \"tier\": \"nonp\", \"request\": null, \"tf_onboarding_module_version\": \"0.4.7\", \"app_code\": \"abc1\"}",
  "state": "received",
  "tf_onboarding_module_version": "",
  "tfe": 1,
  "tier": "nonp",
  "transit_code": "0001",
  "updated_at": "Wed, 15 Jun 2022 22:53:26 GMT"
} 
]