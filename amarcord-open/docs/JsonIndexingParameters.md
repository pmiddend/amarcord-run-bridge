# JsonIndexingParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**cell_description** | **str** |  | [optional] 
**is_online** | **bool** |  | 
**command_line** | **str** |  | 
**geometry_file** | **str** |  | 

## Example

```python
from openapi_client.models.json_indexing_parameters import JsonIndexingParameters

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIndexingParameters from a JSON string
json_indexing_parameters_instance = JsonIndexingParameters.from_json(json)
# print the JSON string representation of the object
print(JsonIndexingParameters.to_json())

# convert the object into a dict
json_indexing_parameters_dict = json_indexing_parameters_instance.to_dict()
# create an instance of JsonIndexingParameters from a dict
json_indexing_parameters_from_dict = JsonIndexingParameters.from_dict(json_indexing_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


