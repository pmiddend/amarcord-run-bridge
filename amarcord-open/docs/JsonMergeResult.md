# JsonMergeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**created** | **int** |  | 
**runs** | **List[str]** |  | 
**indexing_result_ids** | **List[int]** |  | 
**state_queued** | [**JsonMergeResultStateQueued**](JsonMergeResultStateQueued.md) |  | [optional] 
**state_error** | [**JsonMergeResultStateError**](JsonMergeResultStateError.md) |  | [optional] 
**state_running** | [**JsonMergeResultStateRunning**](JsonMergeResultStateRunning.md) |  | [optional] 
**state_done** | [**JsonMergeResultStateDone**](JsonMergeResultStateDone.md) |  | [optional] 
**parameters** | [**JsonMergeParameters**](JsonMergeParameters.md) |  | 
**refinement_results** | [**List[JsonRefinementResult]**](JsonRefinementResult.md) |  | 

## Example

```python
from openapi_client.models.json_merge_result import JsonMergeResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeResult from a JSON string
json_merge_result_instance = JsonMergeResult.from_json(json)
# print the JSON string representation of the object
print(JsonMergeResult.to_json())

# convert the object into a dict
json_merge_result_dict = json_merge_result_instance.to_dict()
# create an instance of JsonMergeResult from a dict
json_merge_result_from_dict = JsonMergeResult.from_dict(json_merge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


