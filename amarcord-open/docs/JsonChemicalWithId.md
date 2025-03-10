# JsonChemicalWithId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**beamtime_id** | **int** |  | 
**name** | **str** |  | 
**responsible_person** | **str** |  | 
**chemical_type** | [**ChemicalType**](ChemicalType.md) |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 
**file_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.json_chemical_with_id import JsonChemicalWithId

# TODO update the JSON string below
json = "{}"
# create an instance of JsonChemicalWithId from a JSON string
json_chemical_with_id_instance = JsonChemicalWithId.from_json(json)
# print the JSON string representation of the object
print(JsonChemicalWithId.to_json())

# convert the object into a dict
json_chemical_with_id_dict = json_chemical_with_id_instance.to_dict()
# create an instance of JsonChemicalWithId from a dict
json_chemical_with_id_from_dict = JsonChemicalWithId.from_dict(json_chemical_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


