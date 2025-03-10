# JsonUpdateRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**experiment_type_id** | **int** |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 
**files** | [**List[JsonRunFile]**](JsonRunFile.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_update_run import JsonUpdateRun

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUpdateRun from a JSON string
json_update_run_instance = JsonUpdateRun.from_json(json)
# print the JSON string representation of the object
print(JsonUpdateRun.to_json())

# convert the object into a dict
json_update_run_dict = json_update_run_instance.to_dict()
# create an instance of JsonUpdateRun from a dict
json_update_run_from_dict = JsonUpdateRun.from_dict(json_update_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


