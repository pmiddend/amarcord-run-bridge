# JsonIndexingResultFinishSuccessfully


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workload_manager_job_id** | **int** |  | 
**stream_file** | **str** |  | 
**program_version** | **str** |  | 
**frames** | **int** |  | 
**hits** | **int** |  | 
**indexed_frames** | **int** |  | 
**indexed_crystals** | **int** |  | 
**detector_shift_x_mm** | **float** |  | [optional] 
**detector_shift_y_mm** | **float** |  | [optional] 
**geometry_file** | **str** |  | 
**geometry_hash** | **str** |  | 
**generated_geometry_file** | **str** |  | 
**unit_cell_histograms_id** | **int** |  | [optional] 
**latest_log** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_indexing_result_finish_successfully import JsonIndexingResultFinishSuccessfully

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIndexingResultFinishSuccessfully from a JSON string
json_indexing_result_finish_successfully_instance = JsonIndexingResultFinishSuccessfully.from_json(json)
# print the JSON string representation of the object
print(JsonIndexingResultFinishSuccessfully.to_json())

# convert the object into a dict
json_indexing_result_finish_successfully_dict = json_indexing_result_finish_successfully_instance.to_dict()
# create an instance of JsonIndexingResultFinishSuccessfully from a dict
json_indexing_result_finish_successfully_from_dict = JsonIndexingResultFinishSuccessfully.from_dict(json_indexing_result_finish_successfully_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


