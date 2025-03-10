# JsonMergeResultStateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started** | **int** |  | 
**stopped** | **int** |  | 
**error** | **str** |  | 
**latest_log** | **str** |  | 

## Example

```python
from openapi_client.models.json_merge_result_state_error import JsonMergeResultStateError

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeResultStateError from a JSON string
json_merge_result_state_error_instance = JsonMergeResultStateError.from_json(json)
# print the JSON string representation of the object
print(JsonMergeResultStateError.to_json())

# convert the object into a dict
json_merge_result_state_error_dict = json_merge_result_state_error_instance.to_dict()
# create an instance of JsonMergeResultStateError from a dict
json_merge_result_state_error_from_dict = JsonMergeResultStateError.from_dict(json_merge_result_state_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


