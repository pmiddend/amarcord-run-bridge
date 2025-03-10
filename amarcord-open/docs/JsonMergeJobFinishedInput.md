# JsonMergeJobFinishedInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_log** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**result** | [**JsonMergeResultInternal**](JsonMergeResultInternal.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_merge_job_finished_input import JsonMergeJobFinishedInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeJobFinishedInput from a JSON string
json_merge_job_finished_input_instance = JsonMergeJobFinishedInput.from_json(json)
# print the JSON string representation of the object
print(JsonMergeJobFinishedInput.to_json())

# convert the object into a dict
json_merge_job_finished_input_dict = json_merge_job_finished_input_instance.to_dict()
# create an instance of JsonMergeJobFinishedInput from a dict
json_merge_job_finished_input_from_dict = JsonMergeJobFinishedInput.from_dict(json_merge_job_finished_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


