# JsonRunsBulkImportOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**simulated** | **bool** |  | 
**create_data_sets** | **bool** |  | 
**errors** | **List[str]** |  | 
**warnings** | **List[str]** |  | 
**number_of_runs** | **int** |  | 
**data_sets** | [**List[JsonDataSet]**](JsonDataSet.md) |  | 

## Example

```python
from openapi_client.models.json_runs_bulk_import_output import JsonRunsBulkImportOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRunsBulkImportOutput from a JSON string
json_runs_bulk_import_output_instance = JsonRunsBulkImportOutput.from_json(json)
# print the JSON string representation of the object
print(JsonRunsBulkImportOutput.to_json())

# convert the object into a dict
json_runs_bulk_import_output_dict = json_runs_bulk_import_output_instance.to_dict()
# create an instance of JsonRunsBulkImportOutput from a dict
json_runs_bulk_import_output_from_dict = JsonRunsBulkImportOutput.from_dict(json_runs_bulk_import_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


