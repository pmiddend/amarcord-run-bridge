# JsonIndexingJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**job_id** | **int** |  | [optional] 
**job_status** | [**DBJobStatus**](DBJobStatus.md) |  | 
**started** | **int** |  | [optional] 
**stopped** | **int** |  | [optional] 
**is_online** | **bool** |  | 
**stream_file** | **str** |  | [optional] 
**source** | **str** |  | 
**cell_description** | **str** |  | [optional] 
**geometry_file_input** | **str** |  | 
**geometry_file_output** | **str** |  | 
**command_line** | **str** |  | 
**run_internal_id** | **int** |  | 
**run_external_id** | **int** |  | 
**beamtime** | [**JsonBeamtime**](JsonBeamtime.md) |  | 
**input_file_globs** | **List[str]** |  | 

## Example

```python
from openapi_client.models.json_indexing_job import JsonIndexingJob

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIndexingJob from a JSON string
json_indexing_job_instance = JsonIndexingJob.from_json(json)
# print the JSON string representation of the object
print(JsonIndexingJob.to_json())

# convert the object into a dict
json_indexing_job_dict = json_indexing_job_instance.to_dict()
# create an instance of JsonIndexingJob from a dict
json_indexing_job_from_dict = JsonIndexingJob.from_dict(json_indexing_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


