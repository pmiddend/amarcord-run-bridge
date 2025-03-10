# JSONSchemaString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**enum** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.json_schema_string import JSONSchemaString

# TODO update the JSON string below
json = "{}"
# create an instance of JSONSchemaString from a JSON string
json_schema_string_instance = JSONSchemaString.from_json(json)
# print the JSON string representation of the object
print(JSONSchemaString.to_json())

# convert the object into a dict
json_schema_string_dict = json_schema_string_instance.to_dict()
# create an instance of JSONSchemaString from a dict
json_schema_string_from_dict = JSONSchemaString.from_dict(json_schema_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


