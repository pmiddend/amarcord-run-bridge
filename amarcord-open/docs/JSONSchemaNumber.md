# JSONSchemaNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**minimum** | **float** |  | [optional] 
**maximum** | **float** |  | [optional] 
**exclusive_minimum** | **float** |  | [optional] 
**exclusive_maximum** | **float** |  | [optional] 
**suffix** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**tolerance** | **float** |  | [optional] 
**tolerance_is_absolute** | **bool** |  | [optional] [default to False]

## Example

```python
from openapi_client.models.json_schema_number import JSONSchemaNumber

# TODO update the JSON string below
json = "{}"
# create an instance of JSONSchemaNumber from a JSON string
json_schema_number_instance = JSONSchemaNumber.from_json(json)
# print the JSON string representation of the object
print(JSONSchemaNumber.to_json())

# convert the object into a dict
json_schema_number_dict = json_schema_number_instance.to_dict()
# create an instance of JSONSchemaNumber from a dict
json_schema_number_from_dict = JSONSchemaNumber.from_dict(json_schema_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


