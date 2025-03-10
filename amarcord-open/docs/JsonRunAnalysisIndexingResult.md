# JsonRunAnalysisIndexingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** |  | 
**foms** | [**JsonIndexingFom**](JsonIndexingFom.md) |  | 
**indexing_statistics** | [**List[JsonIndexingStatistic]**](JsonIndexingStatistic.md) |  | 
**running** | **bool** |  | 
**frames** | **int** |  | [optional] 
**total_frames** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.json_run_analysis_indexing_result import JsonRunAnalysisIndexingResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRunAnalysisIndexingResult from a JSON string
json_run_analysis_indexing_result_instance = JsonRunAnalysisIndexingResult.from_json(json)
# print the JSON string representation of the object
print(JsonRunAnalysisIndexingResult.to_json())

# convert the object into a dict
json_run_analysis_indexing_result_dict = json_run_analysis_indexing_result_instance.to_dict()
# create an instance of JsonRunAnalysisIndexingResult from a dict
json_run_analysis_indexing_result_from_dict = JsonRunAnalysisIndexingResult.from_dict(json_run_analysis_indexing_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


