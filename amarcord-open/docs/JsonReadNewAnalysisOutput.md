# JsonReadNewAnalysisOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**searchable_attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**attributi** | [**List[JsonAttributo]**](JsonAttributo.md) |  | 
**chemical_id_to_name** | [**List[JsonChemicalIdAndName]**](JsonChemicalIdAndName.md) |  | 
**experiment_types** | [**List[JsonExperimentTypeWithBeamtimeInformation]**](JsonExperimentTypeWithBeamtimeInformation.md) |  | 
**filtered_data_sets** | [**List[JsonDataSet]**](JsonDataSet.md) |  | 
**data_set_statistics** | [**List[JsonDataSetStatistics]**](JsonDataSetStatistics.md) |  | 
**attributi_values** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 

## Example

```python
from openapi_client.models.json_read_new_analysis_output import JsonReadNewAnalysisOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadNewAnalysisOutput from a JSON string
json_read_new_analysis_output_instance = JsonReadNewAnalysisOutput.from_json(json)
# print the JSON string representation of the object
print(JsonReadNewAnalysisOutput.to_json())

# convert the object into a dict
json_read_new_analysis_output_dict = json_read_new_analysis_output_instance.to_dict()
# create an instance of JsonReadNewAnalysisOutput from a dict
json_read_new_analysis_output_from_dict = JsonReadNewAnalysisOutput.from_dict(json_read_new_analysis_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


