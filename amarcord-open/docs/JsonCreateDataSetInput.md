# JsonCreateDataSetInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_type_id** | **int** |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 

## Example

```python
from openapi_client.models.json_create_data_set_input import JsonCreateDataSetInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCreateDataSetInput from a JSON string
json_create_data_set_input_instance = JsonCreateDataSetInput.from_json(json)
# print the JSON string representation of the object
print(JsonCreateDataSetInput.to_json())

# convert the object into a dict
json_create_data_set_input_dict = json_create_data_set_input_instance.to_dict()
# create an instance of JsonCreateDataSetInput from a dict
json_create_data_set_input_from_dict = JsonCreateDataSetInput.from_dict(json_create_data_set_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


