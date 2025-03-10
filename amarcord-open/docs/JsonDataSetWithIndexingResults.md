# JsonDataSetWithIndexingResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set** | [**JsonDataSet**](JsonDataSet.md) |  | 
**internal_run_ids** | **List[int]** |  | 
**runs** | [**List[JsonRunRange]**](JsonRunRange.md) |  | 
**point_group** | **str** |  | 
**space_group** | **str** |  | 
**cell_description** | **str** |  | 
**indexing_results** | [**List[JsonIndexingParametersWithResults]**](JsonIndexingParametersWithResults.md) |  | 

## Example

```python
from openapi_client.models.json_data_set_with_indexing_results import JsonDataSetWithIndexingResults

# TODO update the JSON string below
json = "{}"
# create an instance of JsonDataSetWithIndexingResults from a JSON string
json_data_set_with_indexing_results_instance = JsonDataSetWithIndexingResults.from_json(json)
# print the JSON string representation of the object
print(JsonDataSetWithIndexingResults.to_json())

# convert the object into a dict
json_data_set_with_indexing_results_dict = json_data_set_with_indexing_results_instance.to_dict()
# create an instance of JsonDataSetWithIndexingResults from a dict
json_data_set_with_indexing_results_from_dict = JsonDataSetWithIndexingResults.from_dict(json_data_set_with_indexing_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


