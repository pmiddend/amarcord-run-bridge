# JsonEventInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**text** | **str** |  | 
**level** | **str** |  | 
**file_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.json_event_input import JsonEventInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonEventInput from a JSON string
json_event_input_instance = JsonEventInput.from_json(json)
# print the JSON string representation of the object
print(JsonEventInput.to_json())

# convert the object into a dict
json_event_input_dict = json_event_input_instance.to_dict()
# create an instance of JsonEventInput from a dict
json_event_input_from_dict = JsonEventInput.from_dict(json_event_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


