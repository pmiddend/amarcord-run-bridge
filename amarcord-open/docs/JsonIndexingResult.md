# JsonIndexingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created** | **int** |  | 
**started** | **int** |  | [optional] 
**stopped** | **int** |  | [optional] 
**parameters** | [**JsonIndexingParameters**](JsonIndexingParameters.md) |  | 
**program_version** | **str** |  | 
**run_internal_id** | **int** |  | 
**run_external_id** | **int** |  | 
**frames** | **int** |  | 
**hits** | **int** |  | 
**indexed_frames** | **int** |  | 
**indexed_crystals** | **int** |  | 
**status** | [**DBJobStatus**](DBJobStatus.md) |  | 
**detector_shift_x_mm** | **float** |  | [optional] 
**detector_shift_y_mm** | **float** |  | [optional] 
**geometry_file** | **str** |  | 
**geometry_hash** | **str** |  | 
**generated_geometry_file** | **str** |  | 
**unit_cell_histograms_file_id** | **int** |  | [optional] 
**has_error** | **bool** |  | 

## Example

```python
from openapi_client.models.json_indexing_result import JsonIndexingResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIndexingResult from a JSON string
json_indexing_result_instance = JsonIndexingResult.from_json(json)
# print the JSON string representation of the object
print(JsonIndexingResult.to_json())

# convert the object into a dict
json_indexing_result_dict = json_indexing_result_instance.to_dict()
# create an instance of JsonIndexingResult from a dict
json_indexing_result_from_dict = JsonIndexingResult.from_dict(json_indexing_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


