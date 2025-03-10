# JsonBeamtimeScheduleRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **str** |  | 
**var_date** | **str** |  | 
**shift** | **str** |  | 
**comment** | **str** |  | 
**td_support** | **str** |  | 
**chemicals** | **List[int]** |  | 
**start_posix** | **int** |  | 
**stop_posix** | **int** |  | 

## Example

```python
from openapi_client.models.json_beamtime_schedule_row import JsonBeamtimeScheduleRow

# TODO update the JSON string below
json = "{}"
# create an instance of JsonBeamtimeScheduleRow from a JSON string
json_beamtime_schedule_row_instance = JsonBeamtimeScheduleRow.from_json(json)
# print the JSON string representation of the object
print(JsonBeamtimeScheduleRow.to_json())

# convert the object into a dict
json_beamtime_schedule_row_dict = json_beamtime_schedule_row_instance.to_dict()
# create an instance of JsonBeamtimeScheduleRow from a dict
json_beamtime_schedule_row_from_dict = JsonBeamtimeScheduleRow.from_dict(json_beamtime_schedule_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


