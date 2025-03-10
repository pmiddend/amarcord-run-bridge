# JsonReadIndexingResultsOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexing_jobs** | [**List[JsonIndexingJob]**](JsonIndexingJob.md) |  | 

## Example

```python
from openapi_client.models.json_read_indexing_results_output import JsonReadIndexingResultsOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadIndexingResultsOutput from a JSON string
json_read_indexing_results_output_instance = JsonReadIndexingResultsOutput.from_json(json)
# print the JSON string representation of the object
print(JsonReadIndexingResultsOutput.to_json())

# convert the object into a dict
json_read_indexing_results_output_dict = json_read_indexing_results_output_instance.to_dict()
# create an instance of JsonReadIndexingResultsOutput from a dict
json_read_indexing_results_output_from_dict = JsonReadIndexingResultsOutput.from_dict(json_read_indexing_results_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


