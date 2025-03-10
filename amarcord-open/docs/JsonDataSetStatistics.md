# JsonDataSetStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set_id** | **int** |  | 
**run_count** | **int** |  | 
**merge_results_count** | **int** |  | 
**indexed_frames** | **int** |  | 
**merge_or_indexing_jobs_running** | **bool** |  | 

## Example

```python
from openapi_client.models.json_data_set_statistics import JsonDataSetStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataSetStatistics from a JSON string
json_data_set_statistics_instance = JsonDataSetStatistics.from_json(json)
# print the JSON string representation of the object
print(JsonDataSetStatistics.to_json())

# convert the object into a dict
json_data_set_statistics_dict = json_data_set_statistics_instance.to_dict()
# create an instance of JsonDataSetStatistics from a dict
json_data_set_statistics_from_dict = JsonDataSetStatistics.from_dict(json_data_set_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


