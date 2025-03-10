# openapi_client.AttributiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attributi_from_schema_api_attributi_schema_post**](AttributiApi.md#create_attributi_from_schema_api_attributi_schema_post) | **POST** /api/attributi/schema | Create Attributi From Schema
[**create_attributo_api_attributi_post**](AttributiApi.md#create_attributo_api_attributi_post) | **POST** /api/attributi | Create Attributo
[**delete_attributo_api_attributi_delete**](AttributiApi.md#delete_attributo_api_attributi_delete) | **DELETE** /api/attributi | Delete Attributo
[**read_attributi_api_attributi_beamtime_id_get**](AttributiApi.md#read_attributi_api_attributi_beamtime_id_get) | **GET** /api/attributi/{beamtimeId} | Read Attributi
[**update_attributo_api_attributi_patch**](AttributiApi.md#update_attributo_api_attributi_patch) | **PATCH** /api/attributi | Update Attributo


# **create_attributi_from_schema_api_attributi_schema_post**
> JsonCreateAttributiFromSchemaOutput create_attributi_from_schema_api_attributi_schema_post(json_create_attributi_from_schema_input)

Create Attributi From Schema

### Example


```python
import openapi_client
from openapi_client.models.json_create_attributi_from_schema_input import JsonCreateAttributiFromSchemaInput
from openapi_client.models.json_create_attributi_from_schema_output import JsonCreateAttributiFromSchemaOutput
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
    api_instance = openapi_client.AttributiApi(api_client)
    json_create_attributi_from_schema_input = openapi_client.JsonCreateAttributiFromSchemaInput() # JsonCreateAttributiFromSchemaInput | 

    try:
        # Create Attributi From Schema
        api_response = await api_instance.create_attributi_from_schema_api_attributi_schema_post(json_create_attributi_from_schema_input)
        print("The response of AttributiApi->create_attributi_from_schema_api_attributi_schema_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributiApi->create_attributi_from_schema_api_attributi_schema_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_create_attributi_from_schema_input** | [**JsonCreateAttributiFromSchemaInput**](JsonCreateAttributiFromSchemaInput.md)|  | 

### Return type

[**JsonCreateAttributiFromSchemaOutput**](JsonCreateAttributiFromSchemaOutput.md)

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

# **create_attributo_api_attributi_post**
> JsonCreateAttributoOutput create_attributo_api_attributi_post(json_create_attributo_input)

Create Attributo

### Example


```python
import openapi_client
from openapi_client.models.json_create_attributo_input import JsonCreateAttributoInput
from openapi_client.models.json_create_attributo_output import JsonCreateAttributoOutput
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
    api_instance = openapi_client.AttributiApi(api_client)
    json_create_attributo_input = openapi_client.JsonCreateAttributoInput() # JsonCreateAttributoInput | 

    try:
        # Create Attributo
        api_response = await api_instance.create_attributo_api_attributi_post(json_create_attributo_input)
        print("The response of AttributiApi->create_attributo_api_attributi_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributiApi->create_attributo_api_attributi_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_create_attributo_input** | [**JsonCreateAttributoInput**](JsonCreateAttributoInput.md)|  | 

### Return type

[**JsonCreateAttributoOutput**](JsonCreateAttributoOutput.md)

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

# **delete_attributo_api_attributi_delete**
> JsonDeleteAttributoOutput delete_attributo_api_attributi_delete(json_delete_attributo_input)

Delete Attributo

### Example


```python
import openapi_client
from openapi_client.models.json_delete_attributo_input import JsonDeleteAttributoInput
from openapi_client.models.json_delete_attributo_output import JsonDeleteAttributoOutput
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
    api_instance = openapi_client.AttributiApi(api_client)
    json_delete_attributo_input = openapi_client.JsonDeleteAttributoInput() # JsonDeleteAttributoInput | 

    try:
        # Delete Attributo
        api_response = await api_instance.delete_attributo_api_attributi_delete(json_delete_attributo_input)
        print("The response of AttributiApi->delete_attributo_api_attributi_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributiApi->delete_attributo_api_attributi_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_delete_attributo_input** | [**JsonDeleteAttributoInput**](JsonDeleteAttributoInput.md)|  | 

### Return type

[**JsonDeleteAttributoOutput**](JsonDeleteAttributoOutput.md)

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

# **read_attributi_api_attributi_beamtime_id_get**
> JsonReadAttributi read_attributi_api_attributi_beamtime_id_get(beamtime_id)

Read Attributi

### Example


```python
import openapi_client
from openapi_client.models.json_read_attributi import JsonReadAttributi
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
    api_instance = openapi_client.AttributiApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Read Attributi
        api_response = await api_instance.read_attributi_api_attributi_beamtime_id_get(beamtime_id)
        print("The response of AttributiApi->read_attributi_api_attributi_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributiApi->read_attributi_api_attributi_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonReadAttributi**](JsonReadAttributi.md)

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

# **update_attributo_api_attributi_patch**
> JsonUpdateAttributoOutput update_attributo_api_attributi_patch(json_update_attributo_input)

Update Attributo

### Example


```python
import openapi_client
from openapi_client.models.json_update_attributo_input import JsonUpdateAttributoInput
from openapi_client.models.json_update_attributo_output import JsonUpdateAttributoOutput
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
    api_instance = openapi_client.AttributiApi(api_client)
    json_update_attributo_input = openapi_client.JsonUpdateAttributoInput() # JsonUpdateAttributoInput | 

    try:
        # Update Attributo
        api_response = await api_instance.update_attributo_api_attributi_patch(json_update_attributo_input)
        print("The response of AttributiApi->update_attributo_api_attributi_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributiApi->update_attributo_api_attributi_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_update_attributo_input** | [**JsonUpdateAttributoInput**](JsonUpdateAttributoInput.md)|  | 

### Return type

[**JsonUpdateAttributoOutput**](JsonUpdateAttributoOutput.md)

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

