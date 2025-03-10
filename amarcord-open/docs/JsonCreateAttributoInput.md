# JsonCreateAttributoInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beamtime_id** | **int** |  | 
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
from openapi_client.models.json_create_attributo_input import JsonCreateAttributoInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCreateAttributoInput from a JSON string
json_create_attributo_input_instance = JsonCreateAttributoInput.from_json(json)
# print the JSON string representation of the object
print(JsonCreateAttributoInput.to_json())

# convert the object into a dict
json_create_attributo_input_dict = json_create_attributo_input_instance.to_dict()
# create an instance of JsonCreateAttributoInput from a dict
json_create_attributo_input_from_dict = JsonCreateAttributoInput.from_dict(json_create_attributo_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


