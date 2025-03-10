# JsonReadNewAnalysisInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributi_filter** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 
**beamtime_id** | **int** |  | [optional] 
**merge_status** | [**JsonMergeStatus**](JsonMergeStatus.md) |  | 

## Example

```python
from openapi_client.models.json_read_new_analysis_input import JsonReadNewAnalysisInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadNewAnalysisInput from a JSON string
json_read_new_analysis_input_instance = JsonReadNewAnalysisInput.from_json(json)
# print the JSON string representation of the object
print(JsonReadNewAnalysisInput.to_json())

# convert the object into a dict
json_read_new_analysis_input_dict = json_read_new_analysis_input_instance.to_dict()
# create an instance of JsonReadNewAnalysisInput from a dict
json_read_new_analysis_input_from_dict = JsonReadNewAnalysisInput.from_dict(json_read_new_analysis_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


