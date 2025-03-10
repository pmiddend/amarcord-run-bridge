# JsonBeamtimeSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**List[JsonBeamtimeScheduleRow]**](JsonBeamtimeScheduleRow.md) |  | 

## Example

```python
from openapi_client.models.json_beamtime_schedule import JsonBeamtimeSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of JsonBeamtimeSchedule from a JSON string
json_beamtime_schedule_instance = JsonBeamtimeSchedule.from_json(json)
# print the JSON string representation of the object
print(JsonBeamtimeSchedule.to_json())

# convert the object into a dict
json_beamtime_schedule_dict = json_beamtime_schedule_instance.to_dict()
# create an instance of JsonBeamtimeSchedule from a dict
json_beamtime_schedule_from_dict = JsonBeamtimeSchedule.from_dict(json_beamtime_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


