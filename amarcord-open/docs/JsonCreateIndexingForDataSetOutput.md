# JsonCreateIndexingForDataSetOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs_started_run_external_ids** | **List[int]** |  | 
**indexing_result_id** | **int** |  | 
**data_set_id** | **int** |  | 
**indexing_parameters_id** | **int** |  | 

## Example

```python
from openapi_client.models.json_create_indexing_for_data_set_output import JsonCreateIndexingForDataSetOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCreateIndexingForDataSetOutput from a JSON string
json_create_indexing_for_data_set_output_instance = JsonCreateIndexingForDataSetOutput.from_json(json)
# print the JSON string representation of the object
print(JsonCreateIndexingForDataSetOutput.to_json())

# convert the object into a dict
json_create_indexing_for_data_set_output_dict = json_create_indexing_for_data_set_output_instance.to_dict()
# create an instance of JsonCreateIndexingForDataSetOutput from a dict
json_create_indexing_for_data_set_output_from_dict = JsonCreateIndexingForDataSetOutput.from_dict(json_create_indexing_for_data_set_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


