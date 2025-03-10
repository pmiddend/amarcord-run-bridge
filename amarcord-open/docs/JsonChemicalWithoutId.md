# JsonChemicalWithoutId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beamtime_id** | **int** |  | 
**name** | **str** |  | 
**responsible_person** | **str** |  | 
**chemical_type** | [**ChemicalType**](ChemicalType.md) |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 
**file_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.json_chemical_without_id import JsonChemicalWithoutId

# TODO update the JSON string below
json = "{}"
# create an instance of JsonChemicalWithoutId from a JSON string
json_chemical_without_id_instance = JsonChemicalWithoutId.from_json(json)
# print the JSON string representation of the object
print(JsonChemicalWithoutId.to_json())

# convert the object into a dict
json_chemical_without_id_dict = json_chemical_without_id_instance.to_dict()
# create an instance of JsonChemicalWithoutId from a dict
json_chemical_without_id_from_dict = JsonChemicalWithoutId.from_dict(json_chemical_without_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


