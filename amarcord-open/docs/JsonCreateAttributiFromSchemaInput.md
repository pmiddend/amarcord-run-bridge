# JsonCreateAttributiFromSchemaInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributi_schema** | [**List[JsonCreateAttributiFromSchemaSingleAttributo]**](JsonCreateAttributiFromSchemaSingleAttributo.md) |  | 
**beamtime_id** | **int** |  | 

## Example

```python
from openapi_client.models.json_create_attributi_from_schema_input import JsonCreateAttributiFromSchemaInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCreateAttributiFromSchemaInput from a JSON string
json_create_attributi_from_schema_input_instance = JsonCreateAttributiFromSchemaInput.from_json(json)
# print the JSON string representation of the object
print(JsonCreateAttributiFromSchemaInput.to_json())

# convert the object into a dict
json_create_attributi_from_schema_input_dict = json_create_attributi_from_schema_input_instance.to_dict()
# create an instance of JsonCreateAttributiFromSchemaInput from a dict
json_create_attributi_from_schema_input_from_dict = JsonCreateAttributiFromSchemaInput.from_dict(json_create_attributi_from_schema_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


