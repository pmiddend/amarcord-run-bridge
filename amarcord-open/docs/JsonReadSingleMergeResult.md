# JsonReadSingleMergeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**experiment_type** | [**JsonExperimentType**](JsonExperimentType.md) |  | 
**result** | [**JsonMergeResult**](JsonMergeResult.md) |  | 

## Example

```python
from openapi_client.models.json_read_single_merge_result import JsonReadSingleMergeResult

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadSingleMergeResult from a JSON string
json_read_single_merge_result_instance = JsonReadSingleMergeResult.from_json(json)
# print the JSON string representation of the object
print(JsonReadSingleMergeResult.to_json())

# convert the object into a dict
json_read_single_merge_result_dict = json_read_single_merge_result_instance.to_dict()
# create an instance of JsonReadSingleMergeResult from a dict
json_read_single_merge_result_from_dict = JsonReadSingleMergeResult.from_dict(json_read_single_merge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


