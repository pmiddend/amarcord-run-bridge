# JsonCheckStandardUnitOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** |  | 
**error** | **str** |  | [optional] 
**normalized** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_check_standard_unit_output import JsonCheckStandardUnitOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCheckStandardUnitOutput from a JSON string
json_check_standard_unit_output_instance = JsonCheckStandardUnitOutput.from_json(json)
# print the JSON string representation of the object
print(JsonCheckStandardUnitOutput.to_json())

# convert the object into a dict
json_check_standard_unit_output_dict = json_check_standard_unit_output_instance.to_dict()
# create an instance of JsonCheckStandardUnitOutput from a dict
json_check_standard_unit_output_from_dict = JsonCheckStandardUnitOutput.from_dict(json_check_standard_unit_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


