# JsonEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source** | **str** |  | 
**text** | **str** |  | 
**created** | **int** |  | 
**level** | **str** |  | 
**files** | [**List[JsonFileOutput]**](JsonFileOutput.md) |  | 

## Example

```python
from openapi_client.models.json_event import JsonEvent

# TODO update the JSON string below
json = "{}"
# create an instance of JsonEvent from a JSON string
json_event_instance = JsonEvent.from_json(json)
# print the JSON string representation of the object
print(JsonEvent.to_json())

# convert the object into a dict
json_event_dict = json_event_instance.to_dict()
# create an instance of JsonEvent from a dict
json_event_from_dict = JsonEvent.from_dict(json_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


