# JsonIndexingParametersWithResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**JsonIndexingParameters**](JsonIndexingParameters.md) |  | 
**indexing_results** | [**List[JsonIndexingResult]**](JsonIndexingResult.md) |  | 
**merge_results** | [**List[JsonMergeResult]**](JsonMergeResult.md) |  | 

## Example

```python
from openapi_client.models.json_indexing_parameters_with_results import JsonIndexingParametersWithResults

# TODO update the JSON string below
json = "{}"
# create an instance of JsonIndexingParametersWithResults from a JSON string
json_indexing_parameters_with_results_instance = JsonIndexingParametersWithResults.from_json(json)
# print the JSON string representation of the object
print(JsonIndexingParametersWithResults.to_json())

# convert the object into a dict
json_indexing_parameters_with_results_dict = json_indexing_parameters_with_results_instance.to_dict()
# create an instance of JsonIndexingParametersWithResults from a dict
json_indexing_parameters_with_results_from_dict = JsonIndexingParametersWithResults.from_dict(json_indexing_parameters_with_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


