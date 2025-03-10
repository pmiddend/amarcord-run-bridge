# openapi_client.ExperimenttypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_current_run_experiment_type_api_experiment_types_change_for_run_post**](ExperimenttypesApi.md#change_current_run_experiment_type_api_experiment_types_change_for_run_post) | **POST** /api/experiment-types/change-for-run | Change Current Run Experiment Type
[**copy_experiment_types_api_copy_experiment_types_post**](ExperimenttypesApi.md#copy_experiment_types_api_copy_experiment_types_post) | **POST** /api/copy-experiment-types | Copy Experiment Types
[**create_experiment_type_api_experiment_types_post**](ExperimenttypesApi.md#create_experiment_type_api_experiment_types_post) | **POST** /api/experiment-types | Create Experiment Type
[**delete_experiment_type_api_experiment_types_delete**](ExperimenttypesApi.md#delete_experiment_type_api_experiment_types_delete) | **DELETE** /api/experiment-types | Delete Experiment Type
[**read_experiment_types_api_experiment_types_beamtime_id_get**](ExperimenttypesApi.md#read_experiment_types_api_experiment_types_beamtime_id_get) | **GET** /api/experiment-types/{beamtimeId} | Read Experiment Types


# **change_current_run_experiment_type_api_experiment_types_change_for_run_post**
> JsonChangeRunExperimentTypeOutput change_current_run_experiment_type_api_experiment_types_change_for_run_post(json_change_run_experiment_type)

Change Current Run Experiment Type

### Example


```python
import openapi_client
from openapi_client.models.json_change_run_experiment_type import JsonChangeRunExperimentType
from openapi_client.models.json_change_run_experiment_type_output import JsonChangeRunExperimentTypeOutput
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
    api_instance = openapi_client.ExperimenttypesApi(api_client)
    json_change_run_experiment_type = openapi_client.JsonChangeRunExperimentType() # JsonChangeRunExperimentType | 

    try:
        # Change Current Run Experiment Type
        api_response = await api_instance.change_current_run_experiment_type_api_experiment_types_change_for_run_post(json_change_run_experiment_type)
        print("The response of ExperimenttypesApi->change_current_run_experiment_type_api_experiment_types_change_for_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimenttypesApi->change_current_run_experiment_type_api_experiment_types_change_for_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_change_run_experiment_type** | [**JsonChangeRunExperimentType**](JsonChangeRunExperimentType.md)|  | 

### Return type

[**JsonChangeRunExperimentTypeOutput**](JsonChangeRunExperimentTypeOutput.md)

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

# **copy_experiment_types_api_copy_experiment_types_post**
> JsonCopyExperimentTypesOutput copy_experiment_types_api_copy_experiment_types_post(json_copy_experiment_types_input)

Copy Experiment Types

### Example


```python
import openapi_client
from openapi_client.models.json_copy_experiment_types_input import JsonCopyExperimentTypesInput
from openapi_client.models.json_copy_experiment_types_output import JsonCopyExperimentTypesOutput
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
    api_instance = openapi_client.ExperimenttypesApi(api_client)
    json_copy_experiment_types_input = openapi_client.JsonCopyExperimentTypesInput() # JsonCopyExperimentTypesInput | 

    try:
        # Copy Experiment Types
        api_response = await api_instance.copy_experiment_types_api_copy_experiment_types_post(json_copy_experiment_types_input)
        print("The response of ExperimenttypesApi->copy_experiment_types_api_copy_experiment_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimenttypesApi->copy_experiment_types_api_copy_experiment_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_copy_experiment_types_input** | [**JsonCopyExperimentTypesInput**](JsonCopyExperimentTypesInput.md)|  | 

### Return type

[**JsonCopyExperimentTypesOutput**](JsonCopyExperimentTypesOutput.md)

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

# **create_experiment_type_api_experiment_types_post**
> JsonCreateExperimentTypeOutput create_experiment_type_api_experiment_types_post(json_create_experiment_type_input)

Create Experiment Type

### Example


```python
import openapi_client
from openapi_client.models.json_create_experiment_type_input import JsonCreateExperimentTypeInput
from openapi_client.models.json_create_experiment_type_output import JsonCreateExperimentTypeOutput
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
    api_instance = openapi_client.ExperimenttypesApi(api_client)
    json_create_experiment_type_input = openapi_client.JsonCreateExperimentTypeInput() # JsonCreateExperimentTypeInput | 

    try:
        # Create Experiment Type
        api_response = await api_instance.create_experiment_type_api_experiment_types_post(json_create_experiment_type_input)
        print("The response of ExperimenttypesApi->create_experiment_type_api_experiment_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimenttypesApi->create_experiment_type_api_experiment_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_create_experiment_type_input** | [**JsonCreateExperimentTypeInput**](JsonCreateExperimentTypeInput.md)|  | 

### Return type

[**JsonCreateExperimentTypeOutput**](JsonCreateExperimentTypeOutput.md)

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

# **delete_experiment_type_api_experiment_types_delete**
> JsonDeleteExperimentTypeOutput delete_experiment_type_api_experiment_types_delete(json_delete_experiment_type)

Delete Experiment Type

### Example


```python
import openapi_client
from openapi_client.models.json_delete_experiment_type import JsonDeleteExperimentType
from openapi_client.models.json_delete_experiment_type_output import JsonDeleteExperimentTypeOutput
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
    api_instance = openapi_client.ExperimenttypesApi(api_client)
    json_delete_experiment_type = openapi_client.JsonDeleteExperimentType() # JsonDeleteExperimentType | 

    try:
        # Delete Experiment Type
        api_response = await api_instance.delete_experiment_type_api_experiment_types_delete(json_delete_experiment_type)
        print("The response of ExperimenttypesApi->delete_experiment_type_api_experiment_types_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimenttypesApi->delete_experiment_type_api_experiment_types_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_delete_experiment_type** | [**JsonDeleteExperimentType**](JsonDeleteExperimentType.md)|  | 

### Return type

[**JsonDeleteExperimentTypeOutput**](JsonDeleteExperimentTypeOutput.md)

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

# **read_experiment_types_api_experiment_types_beamtime_id_get**
> JsonReadExperimentTypes read_experiment_types_api_experiment_types_beamtime_id_get(beamtime_id)

Read Experiment Types

### Example


```python
import openapi_client
from openapi_client.models.json_read_experiment_types import JsonReadExperimentTypes
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
    api_instance = openapi_client.ExperimenttypesApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Read Experiment Types
        api_response = await api_instance.read_experiment_types_api_experiment_types_beamtime_id_get(beamtime_id)
        print("The response of ExperimenttypesApi->read_experiment_types_api_experiment_types_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExperimenttypesApi->read_experiment_types_api_experiment_types_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonReadExperimentTypes**](JsonReadExperimentTypes.md)

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

