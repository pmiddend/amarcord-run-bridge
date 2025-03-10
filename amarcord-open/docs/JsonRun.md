# JsonRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**external_id** | **int** |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 
**started** | **int** |  | 
**stopped** | **int** |  | [optional] 
**files** | [**List[JsonRunFile]**](JsonRunFile.md) |  | 
**summary** | [**JsonIndexingFom**](JsonIndexingFom.md) |  | 
**experiment_type_id** | **int** |  | 

## Example

```python
from openapi_client.models.json_run import JsonRun

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRun from a JSON string
json_run_instance = JsonRun.from_json(json)
# print the JSON string representation of the object
print(JsonRun.to_json())

# convert the object into a dict
json_run_dict = json_run_instance.to_dict()
# create an instance of JsonRun from a dict
json_run_from_dict = JsonRun.from_dict(json_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


