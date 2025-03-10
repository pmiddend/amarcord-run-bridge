# JsonReadAllChemicals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chemicals** | [**List[JsonChemical]**](JsonChemical.md) |  | 
**beamtimes** | [**List[JsonBeamtime]**](JsonBeamtime.md) |  | 
**attributi_names** | [**List[JsonAttributoWithName]**](JsonAttributoWithName.md) |  | 

## Example

```python
from openapi_client.models.json_read_all_chemicals import JsonReadAllChemicals

# TODO update the JSON string below
json = "{}"
# create an instance of JsonReadAllChemicals from a JSON string
json_read_all_chemicals_instance = JsonReadAllChemicals.from_json(json)
# print the JSON string representation of the object
print(JsonReadAllChemicals.to_json())

# convert the object into a dict
json_read_all_chemicals_dict = json_read_all_chemicals_instance.to_dict()
# create an instance of JsonReadAllChemicals from a dict
json_read_all_chemicals_from_dict = JsonReadAllChemicals.from_dict(json_read_all_chemicals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


