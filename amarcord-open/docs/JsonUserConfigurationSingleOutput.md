# JsonUserConfigurationSingleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_bool** | **bool** |  | [optional] 
**value_int** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.json_user_configuration_single_output import JsonUserConfigurationSingleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUserConfigurationSingleOutput from a JSON string
json_user_configuration_single_output_instance = JsonUserConfigurationSingleOutput.from_json(json)
# print the JSON string representation of the object
print(JsonUserConfigurationSingleOutput.to_json())

# convert the object into a dict
json_user_configuration_single_output_dict = json_user_configuration_single_output_instance.to_dict()
# create an instance of JsonUserConfigurationSingleOutput from a dict
json_user_configuration_single_output_from_dict = JsonUserConfigurationSingleOutput.from_dict(json_user_configuration_single_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


