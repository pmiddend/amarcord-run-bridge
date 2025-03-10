# JsonUpdateBeamtimeScheduleInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beamtime_id** | **int** |  | 
**schedule** | [**List[JsonBeamtimeScheduleRow]**](JsonBeamtimeScheduleRow.md) |  | 

## Example

```python
from openapi_client.models.json_update_beamtime_schedule_input import JsonUpdateBeamtimeScheduleInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonUpdateBeamtimeScheduleInput from a JSON string
json_update_beamtime_schedule_input_instance = JsonUpdateBeamtimeScheduleInput.from_json(json)
# print the JSON string representation of the object
print(JsonUpdateBeamtimeScheduleInput.to_json())

# convert the object into a dict
json_update_beamtime_schedule_input_dict = json_update_beamtime_schedule_input_instance.to_dict()
# create an instance of JsonUpdateBeamtimeScheduleInput from a dict
json_update_beamtime_schedule_input_from_dict = JsonUpdateBeamtimeScheduleInput.from_dict(json_update_beamtime_schedule_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


