# JsonAnalysisRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**external_id** | **int** |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 
**file_paths** | [**List[JsonRunFile]**](JsonRunFile.md) |  | 

## Example

```python
from openapi_client.models.json_analysis_run import JsonAnalysisRun

# TODO update the JSON string below
json = "{}"
# create an instance of JsonAnalysisRun from a JSON string
json_analysis_run_instance = JsonAnalysisRun.from_json(json)
# print the JSON string representation of the object
print(JsonAnalysisRun.to_json())

# convert the object into a dict
json_analysis_run_dict = json_analysis_run_instance.to_dict()
# create an instance of JsonAnalysisRun from a dict
json_analysis_run_from_dict = JsonAnalysisRun.from_dict(json_analysis_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


