# JsonReadMergeResultsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_jobs** | [**List[JsonMergeJob]**](JsonMergeJob.md) |  | 

## Example

```python
from openapi_client.models.json_read_merge_results_output import JsonReadMergeResultsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadMergeResultsOutput from a JSON string
json_read_merge_results_output_instance = JsonReadMergeResultsOutput.from_json(json)
# print the JSON string representation of the object
print(JsonReadMergeResultsOutput.to_json())

# convert the object into a dict
json_read_merge_results_output_dict = json_read_merge_results_output_instance.to_dict()
# create an instance of JsonReadMergeResultsOutput from a dict
json_read_merge_results_output_from_dict = JsonReadMergeResultsOutput.from_dict(json_read_merge_results_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


