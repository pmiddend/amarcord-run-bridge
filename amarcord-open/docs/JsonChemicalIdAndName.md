# JsonChemicalIdAndName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chemical_id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.json_chemical_id_and_name import JsonChemicalIdAndName

# TODO update the JSON string below
json = "{}"
# create an instance of JsonChemicalIdAndName from a JSON string
json_chemical_id_and_name_instance = JsonChemicalIdAndName.from_json(json)
# print the JSON string representation of the object
print(JsonChemicalIdAndName.to_json())

# convert the object into a dict
json_chemical_id_and_name_dict = json_chemical_id_and_name_instance.to_dict()
# create an instance of JsonChemicalIdAndName from a dict
json_chemical_id_and_name_from_dict = JsonChemicalIdAndName.from_dict(json_chemical_id_and_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


