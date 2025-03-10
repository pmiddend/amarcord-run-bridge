# JsonCreateOrUpdateRunOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_created** | **bool** |  | 
**indexing_result_id** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**run_internal_id** | **int** |  | [optional] 
**files** | [**List[JsonRunFile]**](JsonRunFile.md) |  | 

## Example

```python
from openapi_client.models.json_create_or_update_run_output import JsonCreateOrUpdateRunOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCreateOrUpdateRunOutput from a JSON string
json_create_or_update_run_output_instance = JsonCreateOrUpdateRunOutput.from_json(json)
# print the JSON string representation of the object
print(JsonCreateOrUpdateRunOutput.to_json())

# convert the object into a dict
json_create_or_update_run_output_dict = json_create_or_update_run_output_instance.to_dict()
# create an instance of JsonCreateOrUpdateRunOutput from a dict
json_create_or_update_run_output_from_dict = JsonCreateOrUpdateRunOutput.from_dict(json_create_or_update_run_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


