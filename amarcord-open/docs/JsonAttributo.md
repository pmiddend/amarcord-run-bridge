# JsonAttributo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**group** | **str** |  | 
**associated_table** | [**AssociatedTable**](AssociatedTable.md) |  | 
**attributo_type_integer** | [**JSONSchemaInteger**](JSONSchemaInteger.md) |  | [optional] 
**attributo_type_number** | [**JSONSchemaNumber**](JSONSchemaNumber.md) |  | [optional] 
**attributo_type_string** | [**JSONSchemaString**](JSONSchemaString.md) |  | [optional] 
**attributo_type_array** | [**JSONSchemaArray**](JSONSchemaArray.md) |  | [optional] 
**attributo_type_boolean** | [**JSONSchemaBoolean**](JSONSchemaBoolean.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_attributo import JsonAttributo

# TODO update the JSON string below
json = "{}"
# create an instance of JsonAttributo from a JSON string
json_attributo_instance = JsonAttributo.from_json(json)
# print the JSON string representation of the object
print(JsonAttributo.to_json())

# convert the object into a dict
json_attributo_dict = json_attributo_instance.to_dict()
# create an instance of JsonAttributo from a dict
json_attributo_from_dict = JsonAttributo.from_dict(json_attributo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


