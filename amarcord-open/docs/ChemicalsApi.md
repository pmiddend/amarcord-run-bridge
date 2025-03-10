# openapi_client.ChemicalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_chemical_api_copy_chemical_post**](ChemicalsApi.md#copy_chemical_api_copy_chemical_post) | **POST** /api/copy-chemical | Copy Chemical
[**create_chemical_api_chemicals_post**](ChemicalsApi.md#create_chemical_api_chemicals_post) | **POST** /api/chemicals | Create Chemical
[**delete_chemical_api_chemicals_delete**](ChemicalsApi.md#delete_chemical_api_chemicals_delete) | **DELETE** /api/chemicals | Delete Chemical
[**read_all_chemicals_api_all_chemicals_get**](ChemicalsApi.md#read_all_chemicals_api_all_chemicals_get) | **GET** /api/all-chemicals | Read All Chemicals
[**read_chemicals_api_chemicals_beamtime_id_get**](ChemicalsApi.md#read_chemicals_api_chemicals_beamtime_id_get) | **GET** /api/chemicals/{beamtimeId} | Read Chemicals
[**update_chemical_api_chemicals_patch**](ChemicalsApi.md#update_chemical_api_chemicals_patch) | **PATCH** /api/chemicals | Update Chemical


# **copy_chemical_api_copy_chemical_post**
> JsonCopyChemicalOutput copy_chemical_api_copy_chemical_post(json_copy_chemical_input)

Copy Chemical

### Example


```python
import openapi_client
from openapi_client.models.json_copy_chemical_input import JsonCopyChemicalInput
from openapi_client.models.json_copy_chemical_output import JsonCopyChemicalOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ChemicalsApi(api_client)
    json_copy_chemical_input = openapi_client.JsonCopyChemicalInput() # JsonCopyChemicalInput | 

    try:
        # Copy Chemical
        api_response = await api_instance.copy_chemical_api_copy_chemical_post(json_copy_chemical_input)
        print("The response of ChemicalsApi->copy_chemical_api_copy_chemical_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChemicalsApi->copy_chemical_api_copy_chemical_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_copy_chemical_input** | [**JsonCopyChemicalInput**](JsonCopyChemicalInput.md)|  | 

### Return type

[**JsonCopyChemicalOutput**](JsonCopyChemicalOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chemical_api_chemicals_post**
> JsonCreateChemicalOutput create_chemical_api_chemicals_post(json_chemical_without_id)

Create Chemical

### Example


```python
import openapi_client
from openapi_client.models.json_chemical_without_id import JsonChemicalWithoutId
from openapi_client.models.json_create_chemical_output import JsonCreateChemicalOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ChemicalsApi(api_client)
    json_chemical_without_id = openapi_client.JsonChemicalWithoutId() # JsonChemicalWithoutId | 

    try:
        # Create Chemical
        api_response = await api_instance.create_chemical_api_chemicals_post(json_chemical_without_id)
        print("The response of ChemicalsApi->create_chemical_api_chemicals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChemicalsApi->create_chemical_api_chemicals_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_chemical_without_id** | [**JsonChemicalWithoutId**](JsonChemicalWithoutId.md)|  | 

### Return type

[**JsonCreateChemicalOutput**](JsonCreateChemicalOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chemical_api_chemicals_delete**
> JsonDeleteChemicalOutput delete_chemical_api_chemicals_delete(json_delete_chemical_input)

Delete Chemical

### Example


```python
import openapi_client
from openapi_client.models.json_delete_chemical_input import JsonDeleteChemicalInput
from openapi_client.models.json_delete_chemical_output import JsonDeleteChemicalOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ChemicalsApi(api_client)
    json_delete_chemical_input = openapi_client.JsonDeleteChemicalInput() # JsonDeleteChemicalInput | 

    try:
        # Delete Chemical
        api_response = await api_instance.delete_chemical_api_chemicals_delete(json_delete_chemical_input)
        print("The response of ChemicalsApi->delete_chemical_api_chemicals_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChemicalsApi->delete_chemical_api_chemicals_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_delete_chemical_input** | [**JsonDeleteChemicalInput**](JsonDeleteChemicalInput.md)|  | 

### Return type

[**JsonDeleteChemicalOutput**](JsonDeleteChemicalOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_all_chemicals_api_all_chemicals_get**
> JsonReadAllChemicals read_all_chemicals_api_all_chemicals_get()

Read All Chemicals

### Example


```python
import openapi_client
from openapi_client.models.json_read_all_chemicals import JsonReadAllChemicals
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ChemicalsApi(api_client)

    try:
        # Read All Chemicals
        api_response = await api_instance.read_all_chemicals_api_all_chemicals_get()
        print("The response of ChemicalsApi->read_all_chemicals_api_all_chemicals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChemicalsApi->read_all_chemicals_api_all_chemicals_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**JsonReadAllChemicals**](JsonReadAllChemicals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_chemicals_api_chemicals_beamtime_id_get**
> JsonReadChemicals read_chemicals_api_chemicals_beamtime_id_get(beamtime_id)

Read Chemicals

### Example


```python
import openapi_client
from openapi_client.models.json_read_chemicals import JsonReadChemicals
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ChemicalsApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Read Chemicals
        api_response = await api_instance.read_chemicals_api_chemicals_beamtime_id_get(beamtime_id)
        print("The response of ChemicalsApi->read_chemicals_api_chemicals_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChemicalsApi->read_chemicals_api_chemicals_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonReadChemicals**](JsonReadChemicals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chemical_api_chemicals_patch**
> JsonCreateChemicalOutput update_chemical_api_chemicals_patch(json_chemical_with_id)

Update Chemical

### Example


```python
import openapi_client
from openapi_client.models.json_chemical_with_id import JsonChemicalWithId
from openapi_client.models.json_create_chemical_output import JsonCreateChemicalOutput
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ChemicalsApi(api_client)
    json_chemical_with_id = openapi_client.JsonChemicalWithId() # JsonChemicalWithId | 

    try:
        # Update Chemical
        api_response = await api_instance.update_chemical_api_chemicals_patch(json_chemical_with_id)
        print("The response of ChemicalsApi->update_chemical_api_chemicals_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChemicalsApi->update_chemical_api_chemicals_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_chemical_with_id** | [**JsonChemicalWithId**](JsonChemicalWithId.md)|  | 

### Return type

[**JsonCreateChemicalOutput**](JsonCreateChemicalOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

