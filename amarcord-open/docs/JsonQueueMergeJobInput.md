# JsonQueueMergeJobInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strict_mode** | **bool** |  | 
**indexing_parameters_id** | **int** |  | 
**data_set_id** | **int** |  | 
**merge_parameters** | [**JsonMergeParameters**](JsonMergeParameters.md) |  | 

## Example

```python
from openapi_client.models.json_queue_merge_job_input import JsonQueueMergeJobInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonQueueMergeJobInput from a JSON string
json_queue_merge_job_input_instance = JsonQueueMergeJobInput.from_json(json)
# print the JSON string representation of the object
print(JsonQueueMergeJobInput.to_json())

# convert the object into a dict
json_queue_merge_job_input_dict = json_queue_merge_job_input_instance.to_dict()
# create an instance of JsonQueueMergeJobInput from a dict
json_queue_merge_job_input_from_dict = JsonQueueMergeJobInput.from_dict(json_queue_merge_job_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


