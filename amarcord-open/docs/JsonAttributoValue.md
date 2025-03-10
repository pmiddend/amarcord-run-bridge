# JsonAttributoValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributo_id** | **int** |  | 
**attributo_value_str** | **str** |  | [optional] 
**attributo_value_int** | **int** |  | [optional] 
**attributo_value_chemical** | **int** |  | [optional] 
**attributo_value_datetime** | **int** |  | [optional] 
**attributo_value_float** | **float** |  | [optional] 
**attributo_value_bool** | **bool** |  | [optional] 
**attributo_value_list_str** | **List[str]** |  | [optional] 
**attributo_value_list_float** | **List[float]** |  | [optional] 
**attributo_value_list_bool** | **List[bool]** |  | [optional] 

## Example

```python
from openapi_client.models.json_attributo_value import JsonAttributoValue

# TODO update the JSON string below
json = "{}"
# create an instance of JsonAttributoValue from a JSON string
json_attributo_value_instance = JsonAttributoValue.from_json(json)
# print the JSON string representation of the object
print(JsonAttributoValue.to_json())

# convert the object into a dict
json_attributo_value_dict = json_attributo_value_instance.to_dict()
# create an instance of JsonAttributoValue from a dict
json_attributo_value_from_dict = JsonAttributoValue.from_dict(json_attributo_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


