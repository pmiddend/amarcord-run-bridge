# JsonAttributoBulkValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributo_id** | **int** |  | 
**values** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 

## Example

```python
from openapi_client.models.json_attributo_bulk_value import JsonAttributoBulkValue

# TODO update the JSON string below
json = "{}"
# create an instance of JsonAttributoBulkValue from a JSON string
json_attributo_bulk_value_instance = JsonAttributoBulkValue.from_json(json)
# print the JSON string representation of the object
print(JsonAttributoBulkValue.to_json())

# convert the object into a dict
json_attributo_bulk_value_dict = json_attributo_bulk_value_instance.to_dict()
# create an instance of JsonAttributoBulkValue from a dict
json_attributo_bulk_value_from_dict = JsonAttributoBulkValue.from_dict(json_attributo_bulk_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


