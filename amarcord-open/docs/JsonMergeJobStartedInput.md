# JsonMergeJobStartedInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** |  | 
**time** | **int** |  | 

## Example

```python
from openapi_client.models.json_merge_job_started_input import JsonMergeJobStartedInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeJobStartedInput from a JSON string
json_merge_job_started_input_instance = JsonMergeJobStartedInput.from_json(json)
# print the JSON string representation of the object
print(JsonMergeJobStartedInput.to_json())

# convert the object into a dict
json_merge_job_started_input_dict = json_merge_job_started_input_instance.to_dict()
# create an instance of JsonMergeJobStartedInput from a dict
json_merge_job_started_input_from_dict = JsonMergeJobStartedInput.from_dict(json_merge_job_started_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


