# JSONSchemaInteger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**format** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_schema_integer import JSONSchemaInteger

# TODO update the JSON string below
json = "{}"
# create an instance of JSONSchemaInteger from a JSON string
json_schema_integer_instance = JSONSchemaInteger.from_json(json)
# print the JSON string representation of the object
print(JSONSchemaInteger.to_json())

# convert the object into a dict
json_schema_integer_dict = json_schema_integer_instance.to_dict()
# create an instance of JSONSchemaInteger from a dict
json_schema_integer_from_dict = JSONSchemaInteger.from_dict(json_schema_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


