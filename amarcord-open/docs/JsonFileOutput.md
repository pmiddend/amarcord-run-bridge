# JsonFileOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**description** | **str** |  | 
**type_** | **str** |  | 
**original_path** | **str** |  | [optional] 
**file_name** | **str** |  | 
**size_in_bytes** | **int** |  | 

## Example

```python
from openapi_client.models.json_file_output import JsonFileOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonFileOutput from a JSON string
json_file_output_instance = JsonFileOutput.from_json(json)
# print the JSON string representation of the object
print(JsonFileOutput.to_json())

# convert the object into a dict
json_file_output_dict = json_file_output_instance.to_dict()
# create an instance of JsonFileOutput from a dict
json_file_output_from_dict = JsonFileOutput.from_dict(json_file_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


