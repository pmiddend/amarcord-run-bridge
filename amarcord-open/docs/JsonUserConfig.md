# JsonUserConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online_crystfel** | **bool** |  | 
**auto_pilot** | **bool** |  | 
**current_experiment_type_id** | **int** |  | [optional] 
**current_online_indexing_parameters_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.json_user_config import JsonUserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUserConfig from a JSON string
json_user_config_instance = JsonUserConfig.from_json(json)
# print the JSON string representation of the object
print(JsonUserConfig.to_json())

# convert the object into a dict
json_user_config_dict = json_user_config_instance.to_dict()
# create an instance of JsonUserConfig from a dict
json_user_config_from_dict = JsonUserConfig.from_dict(json_user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


