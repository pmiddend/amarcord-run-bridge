# JsonReadRunsBulkInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beamtime_id** | **int** |  | 
**external_run_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.json_read_runs_bulk_input import JsonReadRunsBulkInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadRunsBulkInput from a JSON string
json_read_runs_bulk_input_instance = JsonReadRunsBulkInput.from_json(json)
# print the JSON string representation of the object
print(JsonReadRunsBulkInput.to_json())

# convert the object into a dict
json_read_runs_bulk_input_dict = json_read_runs_bulk_input_instance.to_dict()
# create an instance of JsonReadRunsBulkInput from a dict
json_read_runs_bulk_input_from_dict = JsonReadRunsBulkInput.from_dict(json_read_runs_bulk_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


