# JsonDetectorShift


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_external_id** | **int** |  | 
**run_start** | **int** |  | 
**run_end** | **int** |  | [optional] 
**shift_x_mm** | **float** |  | 
**shift_y_mm** | **float** |  | 
**geometry_hash** | **str** |  | 

## Example

```python
from openapi_client.models.json_detector_shift import JsonDetectorShift

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDetectorShift from a JSON string
json_detector_shift_instance = JsonDetectorShift.from_json(json)
# print the JSON string representation of the object
print(JsonDetectorShift.to_json())

# convert the object into a dict
json_detector_shift_dict = json_detector_shift_instance.to_dict()
# create an instance of JsonDetectorShift from a dict
json_detector_shift_from_dict = JsonDetectorShift.from_dict(json_detector_shift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


