# JsonMergeResultStateDone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started** | **int** |  | 
**stopped** | **int** |  | 
**result** | [**JsonMergeResultInternal**](JsonMergeResultInternal.md) |  | 

## Example

```python
from openapi_client.models.json_merge_result_state_done import JsonMergeResultStateDone

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeResultStateDone from a JSON string
json_merge_result_state_done_instance = JsonMergeResultStateDone.from_json(json)
# print the JSON string representation of the object
print(JsonMergeResultStateDone.to_json())

# convert the object into a dict
json_merge_result_state_done_dict = json_merge_result_state_done_instance.to_dict()
# create an instance of JsonMergeResultStateDone from a dict
json_merge_result_state_done_from_dict = JsonMergeResultStateDone.from_dict(json_merge_result_state_done_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


