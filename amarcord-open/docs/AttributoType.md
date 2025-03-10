# AttributoType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**format** | **str** |  | [optional] 
**minimum** | **float** |  | [optional] 
**maximum** | **float** |  | [optional] 
**exclusive_minimum** | **float** |  | [optional] 
**exclusive_maximum** | **float** |  | [optional] 
**suffix** | **str** |  | [optional] 
**tolerance** | **float** |  | [optional] 
**tolerance_is_absolute** | **bool** |  | [optional] [default to False]
**enum** | **List[str]** |  | [optional] 
**item_type** | [**JSONSchemaArraySubtype**](JSONSchemaArraySubtype.md) |  | 
**min_items** | **int** |  | [optional] 
**max_items** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.attributo_type import AttributoType

# TODO update the JSON string below
json = "{}"
# create an instance of AttributoType from a JSON string
attributo_type_instance = AttributoType.from_json(json)
# print the JSON string representation of the object
print(AttributoType.to_json())

# convert the object into a dict
attributo_type_dict = attributo_type_instance.to_dict()
# create an instance of AttributoType from a dict
attributo_type_from_dict = AttributoType.from_dict(attributo_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


