# JsonReadSingleDataSetResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**chemical_id_to_name** | [**List[JsonChemicalIdAndName]**](JsonChemicalIdAndName.md) |  | 
**experiment_type** | [**JsonExperimentType**](JsonExperimentType.md) |  | 
**data_set** | [**JsonDataSetWithIndexingResults**](JsonDataSetWithIndexingResults.md) |  | 

## Example

```python
from openapi_client.models.json_read_single_data_set_results import JsonReadSingleDataSetResults

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadSingleDataSetResults from a JSON string
json_read_single_data_set_results_instance = JsonReadSingleDataSetResults.from_json(json)
# print the JSON string representation of the object
print(JsonReadSingleDataSetResults.to_json())

# convert the object into a dict
json_read_single_data_set_results_dict = json_read_single_data_set_results_instance.to_dict()
# create an instance of JsonReadSingleDataSetResults from a dict
json_read_single_data_set_results_from_dict = JsonReadSingleDataSetResults.from_dict(json_read_single_data_set_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


