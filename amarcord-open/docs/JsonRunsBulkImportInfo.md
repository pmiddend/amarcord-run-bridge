# JsonRunsBulkImportInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**experiment_types** | **List[str]** |  | 
**chemicals** | [**List[JsonChemical]**](JsonChemical.md) |  | 

## Example

```python
from openapi_client.models.json_runs_bulk_import_info import JsonRunsBulkImportInfo

# TODO update the JSON string below
json = "{}"
# create an instance of JsonRunsBulkImportInfo from a JSON string
json_runs_bulk_import_info_instance = JsonRunsBulkImportInfo.from_json(json)
# print the JSON string representation of the object
print(JsonRunsBulkImportInfo.to_json())

# convert the object into a dict
json_runs_bulk_import_info_dict = json_runs_bulk_import_info_instance.to_dict()
# create an instance of JsonRunsBulkImportInfo from a dict
json_runs_bulk_import_info_from_dict = JsonRunsBulkImportInfo.from_dict(json_runs_bulk_import_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


