# JsonEventTopLevelInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beamtime_id** | **int** |  | 
**event** | [**JsonEventInput**](JsonEventInput.md) |  | 
**with_live_stream** | **bool** |  | 

## Example

```python
from openapi_client.models.json_event_top_level_input import JsonEventTopLevelInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonEventTopLevelInput from a JSON string
json_event_top_level_input_instance = JsonEventTopLevelInput.from_json(json)
# print the JSON string representation of the object
print(JsonEventTopLevelInput.to_json())

# convert the object into a dict
json_event_top_level_input_dict = json_event_top_level_input_instance.to_dict()
# create an instance of JsonEventTopLevelInput from a dict
json_event_top_level_input_from_dict = JsonEventTopLevelInput.from_dict(json_event_top_level_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


