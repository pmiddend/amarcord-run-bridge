# JsonIndexingResultFinishWithError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | 
**latest_log** | **str** |  | 
**workload_manager_job_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.json_indexing_result_finish_with_error import JsonIndexingResultFinishWithError

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIndexingResultFinishWithError from a JSON string
json_indexing_result_finish_with_error_instance = JsonIndexingResultFinishWithError.from_json(json)
# print the JSON string representation of the object
print(JsonIndexingResultFinishWithError.to_json())

# convert the object into a dict
json_indexing_result_finish_with_error_dict = json_indexing_result_finish_with_error_instance.to_dict()
# create an instance of JsonIndexingResultFinishWithError from a dict
json_indexing_result_finish_with_error_from_dict = JsonIndexingResultFinishWithError.from_dict(json_indexing_result_finish_with_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


