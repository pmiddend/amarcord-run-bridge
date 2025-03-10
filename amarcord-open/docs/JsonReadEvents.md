# JsonReadEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[JsonEvent]**](JsonEvent.md) |  | 

## Example

```python
from openapi_client.models.json_read_events import JsonReadEvents

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadEvents from a JSON string
json_read_events_instance = JsonReadEvents.from_json(json)
# print the JSON string representation of the object
print(JsonReadEvents.to_json())

# convert the object into a dict
json_read_events_dict = json_read_events_instance.to_dict()
# create an instance of JsonReadEvents from a dict
json_read_events_from_dict = JsonReadEvents.from_dict(json_read_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


