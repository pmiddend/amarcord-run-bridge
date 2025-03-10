# openapi_client.ConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_get**](ConfigApi.md#read_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_get) | **GET** /api/user-config/{beamtimeId}/online-indexing-parameters | Read Indexing Parameters
[**read_user_configuration_single_api_user_config_beamtime_id_key_get**](ConfigApi.md#read_user_configuration_single_api_user_config_beamtime_id_key_get) | **GET** /api/user-config/{beamtimeId}/{key} | Read User Configuration Single
[**update_online_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_patch**](ConfigApi.md#update_online_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_patch) | **PATCH** /api/user-config/{beamtimeId}/online-indexing-parameters | Update Online Indexing Parameters
[**update_user_configuration_single_api_user_config_beamtime_id_key_value_patch**](ConfigApi.md#update_user_configuration_single_api_user_config_beamtime_id_key_value_patch) | **PATCH** /api/user-config/{beamtimeId}/{key}/{value} | Update User Configuration Single


# **read_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_get**
> JsonIndexingParameters read_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_get(beamtime_id)

Read Indexing Parameters

### Example


```python
import openapi_client
from openapi_client.models.json_indexing_parameters import JsonIndexingParameters
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
    api_instance = openapi_client.ConfigApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Read Indexing Parameters
        api_response = await api_instance.read_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_get(beamtime_id)
        print("The response of ConfigApi->read_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->read_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonIndexingParameters**](JsonIndexingParameters.md)

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

# **read_user_configuration_single_api_user_config_beamtime_id_key_get**
> JsonUserConfigurationSingleOutput read_user_configuration_single_api_user_config_beamtime_id_key_get(beamtime_id, key)

Read User Configuration Single

### Example


```python
import openapi_client
from openapi_client.models.json_user_configuration_single_output import JsonUserConfigurationSingleOutput
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
    api_instance = openapi_client.ConfigApi(api_client)
    beamtime_id = 56 # int | 
    key = 'key_example' # str | 

    try:
        # Read User Configuration Single
        api_response = await api_instance.read_user_configuration_single_api_user_config_beamtime_id_key_get(beamtime_id, key)
        print("The response of ConfigApi->read_user_configuration_single_api_user_config_beamtime_id_key_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->read_user_configuration_single_api_user_config_beamtime_id_key_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **key** | **str**|  | 

### Return type

[**JsonUserConfigurationSingleOutput**](JsonUserConfigurationSingleOutput.md)

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

# **update_online_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_patch**
> JsonUpdateOnlineIndexingParametersOutput update_online_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_patch(beamtime_id, json_update_online_indexing_parameters_input)

Update Online Indexing Parameters

### Example


```python
import openapi_client
from openapi_client.models.json_update_online_indexing_parameters_input import JsonUpdateOnlineIndexingParametersInput
from openapi_client.models.json_update_online_indexing_parameters_output import JsonUpdateOnlineIndexingParametersOutput
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
    api_instance = openapi_client.ConfigApi(api_client)
    beamtime_id = 56 # int | 
    json_update_online_indexing_parameters_input = openapi_client.JsonUpdateOnlineIndexingParametersInput() # JsonUpdateOnlineIndexingParametersInput | 

    try:
        # Update Online Indexing Parameters
        api_response = await api_instance.update_online_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_patch(beamtime_id, json_update_online_indexing_parameters_input)
        print("The response of ConfigApi->update_online_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->update_online_indexing_parameters_api_user_config_beamtime_id_online_indexing_parameters_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **json_update_online_indexing_parameters_input** | [**JsonUpdateOnlineIndexingParametersInput**](JsonUpdateOnlineIndexingParametersInput.md)|  | 

### Return type

[**JsonUpdateOnlineIndexingParametersOutput**](JsonUpdateOnlineIndexingParametersOutput.md)

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

# **update_user_configuration_single_api_user_config_beamtime_id_key_value_patch**
> JsonUserConfigurationSingleOutput update_user_configuration_single_api_user_config_beamtime_id_key_value_patch(beamtime_id, key, value)

Update User Configuration Single

### Example


```python
import openapi_client
from openapi_client.models.json_user_configuration_single_output import JsonUserConfigurationSingleOutput
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
    api_instance = openapi_client.ConfigApi(api_client)
    beamtime_id = 56 # int | 
    key = 'key_example' # str | 
    value = 'value_example' # str | 

    try:
        # Update User Configuration Single
        api_response = await api_instance.update_user_configuration_single_api_user_config_beamtime_id_key_value_patch(beamtime_id, key, value)
        print("The response of ConfigApi->update_user_configuration_single_api_user_config_beamtime_id_key_value_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->update_user_configuration_single_api_user_config_beamtime_id_key_value_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **key** | **str**|  | 
 **value** | **str**|  | 

### Return type

[**JsonUserConfigurationSingleOutput**](JsonUserConfigurationSingleOutput.md)

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

