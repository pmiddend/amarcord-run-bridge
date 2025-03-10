# JsonReadIndexingParametersOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_set_id** | **int** |  | 
**cell_description** | **str** |  | 
**sources** | **List[str]** |  | 

## Example

```python
from openapi_client.models.json_read_indexing_parameters_output import JsonReadIndexingParametersOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadIndexingParametersOutput from a JSON string
json_read_indexing_parameters_output_instance = JsonReadIndexingParametersOutput.from_json(json)
# print the JSON string representation of the object
print(JsonReadIndexingParametersOutput.to_json())

# convert the object into a dict
json_read_indexing_parameters_output_dict = json_read_indexing_parameters_output_instance.to_dict()
# create an instance of JsonReadIndexingParametersOutput from a dict
json_read_indexing_parameters_output_from_dict = JsonReadIndexingParametersOutput.from_dict(json_read_indexing_parameters_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


