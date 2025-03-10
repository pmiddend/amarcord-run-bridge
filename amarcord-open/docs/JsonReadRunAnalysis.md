# JsonReadRunAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chemicals** | [**List[JsonChemical]**](JsonChemical.md) |  | 
**attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**run** | [**JsonAnalysisRun**](JsonAnalysisRun.md) |  | [optional] 
**run_ids** | [**List[JsonRunId]**](JsonRunId.md) |  | 
**indexing_results** | [**List[JsonRunAnalysisIndexingResult]**](JsonRunAnalysisIndexingResult.md) |  | 

## Example

```python
from openapi_client.models.json_read_run_analysis import JsonReadRunAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadRunAnalysis from a JSON string
json_read_run_analysis_instance = JsonReadRunAnalysis.from_json(json)
# print the JSON string representation of the object
print(JsonReadRunAnalysis.to_json())

# convert the object into a dict
json_read_run_analysis_dict = json_read_run_analysis_instance.to_dict()
# create an instance of JsonReadRunAnalysis from a dict
json_read_run_analysis_from_dict = JsonReadRunAnalysis.from_dict(json_read_run_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


