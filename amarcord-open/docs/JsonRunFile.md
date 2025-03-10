# JsonRunFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**glob** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from openapi_client.models.json_run_file import JsonRunFile

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRunFile from a JSON string
json_run_file_instance = JsonRunFile.from_json(json)
# print the JSON string representation of the object
print(JsonRunFile.to_json())

# convert the object into a dict
json_run_file_dict = json_run_file_instance.to_dict()
# create an instance of JsonRunFile from a dict
json_run_file_from_dict = JsonRunFile.from_dict(json_run_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


