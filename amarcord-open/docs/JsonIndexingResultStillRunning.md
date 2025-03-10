# JsonIndexingResultStillRunning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workload_manager_job_id** | **int** |  | 
**stream_file** | **str** |  | 
**frames** | **int** |  | 
**hits** | **int** |  | 
**indexed_frames** | **int** |  | 
**indexed_crystals** | **int** |  | 
**detector_shift_x_mm** | **float** |  | [optional] 
**detector_shift_y_mm** | **float** |  | [optional] 
**geometry_file** | **str** |  | 
**geometry_hash** | **str** |  | 
**job_started** | **int** |  | [optional] 
**latest_log** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_indexing_result_still_running import JsonIndexingResultStillRunning

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIndexingResultStillRunning from a JSON string
json_indexing_result_still_running_instance = JsonIndexingResultStillRunning.from_json(json)
# print the JSON string representation of the object
print(JsonIndexingResultStillRunning.to_json())

# convert the object into a dict
json_indexing_result_still_running_dict = json_indexing_result_still_running_instance.to_dict()
# create an instance of JsonIndexingResultStillRunning from a dict
json_indexing_result_still_running_from_dict = JsonIndexingResultStillRunning.from_dict(json_indexing_result_still_running_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


