# JsonCopyChemicalInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chemical_id** | **int** |  | 
**target_beamtime_id** | **int** |  | 
**create_attributi** | **bool** |  | 

## Example

```python
from openapi_client.models.json_copy_chemical_input import JsonCopyChemicalInput

# TODO update the JSON string below
json = "{}"
# create an instance of JsonCopyChemicalInput from a JSON string
json_copy_chemical_input_instance = JsonCopyChemicalInput.from_json(json)
# print the JSON string representation of the object
print(JsonCopyChemicalInput.to_json())

# convert the object into a dict
json_copy_chemical_input_dict = json_copy_chemical_input_instance.to_dict()
# create an instance of JsonCopyChemicalInput from a dict
json_copy_chemical_input_from_dict = JsonCopyChemicalInput.from_dict(json_copy_chemical_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


