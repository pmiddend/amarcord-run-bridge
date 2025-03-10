# JsonChemical


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**beamtime_id** | **int** |  | 
**name** | **str** |  | 
**responsible_person** | **str** |  | 
**chemical_type** | [**ChemicalType**](ChemicalType.md) |  | 
**attributi** | [**List[JsonAttributoValue]**](JsonAttributoValue.md) |  | 
**files** | [**List[JsonFileOutput]**](JsonFileOutput.md) |  | 

## Example

```python
from openapi_client.models.json_chemical import JsonChemical

# TODO update the JSON string below
json = "{}"
# create an instance of JsonChemical from a JSON string
json_chemical_instance = JsonChemical.from_json(json)
# print the JSON string representation of the object
print(JsonChemical.to_json())

# convert the object into a dict
json_chemical_dict = json_chemical_instance.to_dict()
# create an instance of JsonChemical from a dict
json_chemical_from_dict = JsonChemical.from_dict(json_chemical_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


