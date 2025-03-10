# JsonMergeJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**job_id** | **int** |  | [optional] 
**job_status** | [**DBJobStatus**](DBJobStatus.md) |  | 
**parameters** | [**JsonMergeParameters**](JsonMergeParameters.md) |  | 
**indexing_results** | [**List[JsonIndexingJob]**](JsonIndexingJob.md) |  | 
**files_from_indexing** | [**List[JsonFileOutput]**](JsonFileOutput.md) |  | 
**point_group** | **str** |  | 
**cell_description** | **str** |  | 

## Example

```python
from openapi_client.models.json_merge_job import JsonMergeJob

# TODO update the JSON string below
json = "{}"
# create an instance of JsonMergeJob from a JSON string
json_merge_job_instance = JsonMergeJob.from_json(json)
# print the JSON string representation of the object
print(JsonMergeJob.to_json())

# convert the object into a dict
json_merge_job_dict = json_merge_job_instance.to_dict()
# create an instance of JsonMergeJob from a dict
json_merge_job_from_dict = JsonMergeJob.from_dict(json_merge_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


