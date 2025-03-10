# JSONSchemaArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**item_type** | [**JSONSchemaArraySubtype**](JSONSchemaArraySubtype.md) |  | 
**min_items** | **int** |  | [optional] 
**max_items** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.json_schema_array import JSONSchemaArray

# TODO update the JSON string below
json = "{}"
# create an instance of JSONSchemaArray from a JSON string
json_schema_array_instance = JSONSchemaArray.from_json(json)
# print the JSON string representation of the object
print(JSONSchemaArray.to_json())

# convert the object into a dict
json_schema_array_dict = json_schema_array_instance.to_dict()
# create an instance of JSONSchemaArray from a dict
json_schema_array_from_dict = JSONSchemaArray.from_dict(json_schema_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


