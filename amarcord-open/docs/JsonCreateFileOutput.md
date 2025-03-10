# JsonCreateFileOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**file_name** | **str** |  | 
**description** | **str** |  | 
**type_** | **str** |  | 
**size_in_bytes** | **int** |  | 
**original_path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_create_file_output import JsonCreateFileOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCreateFileOutput from a JSON string
json_create_file_output_instance = JsonCreateFileOutput.from_json(json)
# print the JSON string representation of the object
print(JsonCreateFileOutput.to_json())

# convert the object into a dict
json_create_file_output_dict = json_create_file_output_instance.to_dict()
# create an instance of JsonCreateFileOutput from a dict
json_create_file_output_from_dict = JsonCreateFileOutput.from_dict(json_create_file_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


