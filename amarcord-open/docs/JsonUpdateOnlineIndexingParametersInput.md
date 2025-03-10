# JsonUpdateOnlineIndexingParametersInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_line** | **str** |  | 
**geometry_file** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from openapi_client.models.json_update_online_indexing_parameters_input import JsonUpdateOnlineIndexingParametersInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUpdateOnlineIndexingParametersInput from a JSON string
json_update_online_indexing_parameters_input_instance = JsonUpdateOnlineIndexingParametersInput.from_json(json)
# print the JSON string representation of the object
print(JsonUpdateOnlineIndexingParametersInput.to_json())

# convert the object into a dict
json_update_online_indexing_parameters_input_dict = json_update_online_indexing_parameters_input_instance.to_dict()
# create an instance of JsonUpdateOnlineIndexingParametersInput from a dict
json_update_online_indexing_parameters_input_from_dict = JsonUpdateOnlineIndexingParametersInput.from_dict(json_update_online_indexing_parameters_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


