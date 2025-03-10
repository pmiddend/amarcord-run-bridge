# JsonCreateOrUpdateRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beamtime_id** | **int** |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 
**files** | [**List[JsonRunFile]**](JsonRunFile.md) |  | [optional] 
**started** | **int** |  | [optional] 
**stopped** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.json_create_or_update_run import JsonCreateOrUpdateRun

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCreateOrUpdateRun from a JSON string
json_create_or_update_run_instance = JsonCreateOrUpdateRun.from_json(json)
# print the JSON string representation of the object
print(JsonCreateOrUpdateRun.to_json())

# convert the object into a dict
json_create_or_update_run_dict = json_create_or_update_run_instance.to_dict()
# create an instance of JsonCreateOrUpdateRun from a dict
json_create_or_update_run_from_dict = JsonCreateOrUpdateRun.from_dict(json_create_or_update_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


