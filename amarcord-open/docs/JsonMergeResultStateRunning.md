# JsonMergeResultStateRunning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started** | **int** |  | 
**job_id** | **int** |  | 
**latest_log** | **str** |  | 

## Example

```python
from openapi_client.models.json_merge_result_state_running import JsonMergeResultStateRunning

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeResultStateRunning from a JSON string
json_merge_result_state_running_instance = JsonMergeResultStateRunning.from_json(json)
# print the JSON string representation of the object
print(JsonMergeResultStateRunning.to_json())

# convert the object into a dict
json_merge_result_state_running_dict = json_merge_result_state_running_instance.to_dict()
# create an instance of JsonMergeResultStateRunning from a dict
json_merge_result_state_running_from_dict = JsonMergeResultStateRunning.from_dict(json_merge_result_state_running_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


