# JsonUpdateRunsBulkInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beamtime_id** | **int** |  | 
**external_run_ids** | **List[int]** |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 
**new_experiment_type_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.json_update_runs_bulk_input import JsonUpdateRunsBulkInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUpdateRunsBulkInput from a JSON string
json_update_runs_bulk_input_instance = JsonUpdateRunsBulkInput.from_json(json)
# print the JSON string representation of the object
print(JsonUpdateRunsBulkInput.to_json())

# convert the object into a dict
json_update_runs_bulk_input_dict = json_update_runs_bulk_input_instance.to_dict()
# create an instance of JsonUpdateRunsBulkInput from a dict
json_update_runs_bulk_input_from_dict = JsonUpdateRunsBulkInput.from_dict(json_update_runs_bulk_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


