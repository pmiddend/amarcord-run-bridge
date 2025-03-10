# JsonBeamtimeScheduleOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule** | [**List[JsonBeamtimeScheduleRow]**](JsonBeamtimeScheduleRow.md) |  | 

## Example

```python
from openapi_client.models.json_beamtime_schedule_output import JsonBeamtimeScheduleOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonBeamtimeScheduleOutput from a JSON string
json_beamtime_schedule_output_instance = JsonBeamtimeScheduleOutput.from_json(json)
# print the JSON string representation of the object
print(JsonBeamtimeScheduleOutput.to_json())

# convert the object into a dict
json_beamtime_schedule_output_dict = json_beamtime_schedule_output_instance.to_dict()
# create an instance of JsonBeamtimeScheduleOutput from a dict
json_beamtime_schedule_output_from_dict = JsonBeamtimeScheduleOutput.from_dict(json_beamtime_schedule_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


