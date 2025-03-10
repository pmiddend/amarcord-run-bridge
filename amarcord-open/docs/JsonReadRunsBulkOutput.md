# JsonReadRunsBulkOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chemicals** | [**List[JsonChemical]**](JsonChemical.md) |  | 
**attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**attributi_values** | [**List[JsonAttributoBulkValue]**](JsonAttributoBulkValue.md) |  | 
**experiment_types** | [**List[JsonExperimentType]**](JsonExperimentType.md) |  | 
**experiment_type_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.json_read_runs_bulk_output import JsonReadRunsBulkOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadRunsBulkOutput from a JSON string
json_read_runs_bulk_output_instance = JsonReadRunsBulkOutput.from_json(json)
# print the JSON string representation of the object
print(JsonReadRunsBulkOutput.to_json())

# convert the object into a dict
json_read_runs_bulk_output_dict = json_read_runs_bulk_output_instance.to_dict()
# create an instance of JsonReadRunsBulkOutput from a dict
json_read_runs_bulk_output_from_dict = JsonReadRunsBulkOutput.from_dict(json_read_runs_bulk_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


