# JsonCreateIndexingForDataSetInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set_id** | **int** |  | 
**is_online** | **bool** |  | 
**cell_description** | **str** |  | 
**geometry_file** | **str** |  | 
**command_line** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from openapi_client.models.json_create_indexing_for_data_set_input import JsonCreateIndexingForDataSetInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCreateIndexingForDataSetInput from a JSON string
json_create_indexing_for_data_set_input_instance = JsonCreateIndexingForDataSetInput.from_json(json)
# print the JSON string representation of the object
print(JsonCreateIndexingForDataSetInput.to_json())

# convert the object into a dict
json_create_indexing_for_data_set_input_dict = json_create_indexing_for_data_set_input_instance.to_dict()
# create an instance of JsonCreateIndexingForDataSetInput from a dict
json_create_indexing_for_data_set_input_from_dict = JsonCreateIndexingForDataSetInput.from_dict(json_create_indexing_for_data_set_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


