# openapi_client.DatasetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_set_api_data_sets_post**](DatasetsApi.md#create_data_set_api_data_sets_post) | **POST** /api/data-sets | Create Data Set
[**create_data_set_from_run_api_data_sets_from_run_post**](DatasetsApi.md#create_data_set_from_run_api_data_sets_from_run_post) | **POST** /api/data-sets/from-run | Create Data Set From Run
[**delete_data_set_api_data_sets_delete**](DatasetsApi.md#delete_data_set_api_data_sets_delete) | **DELETE** /api/data-sets | Delete Data Set
[**read_data_sets_api_data_sets_beamtime_id_get**](DatasetsApi.md#read_data_sets_api_data_sets_beamtime_id_get) | **GET** /api/data-sets/{beamtimeId} | Read Data Sets


# **create_data_set_api_data_sets_post**
> JsonCreateDataSetOutput create_data_set_api_data_sets_post(json_create_data_set_input)

Create Data Set

### Example


```python
import openapi_client
from openapi_client.models.json_create_data_set_input import JsonCreateDataSetInput
from openapi_client.models.json_create_data_set_output import JsonCreateDataSetOutput
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
    api_instance = openapi_client.DatasetsApi(api_client)
    json_create_data_set_input = openapi_client.JsonCreateDataSetInput() # JsonCreateDataSetInput | 

    try:
        # Create Data Set
        api_response = await api_instance.create_data_set_api_data_sets_post(json_create_data_set_input)
        print("The response of DatasetsApi->create_data_set_api_data_sets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->create_data_set_api_data_sets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_create_data_set_input** | [**JsonCreateDataSetInput**](JsonCreateDataSetInput.md)|  | 

### Return type

[**JsonCreateDataSetOutput**](JsonCreateDataSetOutput.md)

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

# **create_data_set_from_run_api_data_sets_from_run_post**
> JsonCreateDataSetFromRunOutput create_data_set_from_run_api_data_sets_from_run_post(json_create_data_set_from_run)

Create Data Set From Run

### Example


```python
import openapi_client
from openapi_client.models.json_create_data_set_from_run import JsonCreateDataSetFromRun
from openapi_client.models.json_create_data_set_from_run_output import JsonCreateDataSetFromRunOutput
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
    api_instance = openapi_client.DatasetsApi(api_client)
    json_create_data_set_from_run = openapi_client.JsonCreateDataSetFromRun() # JsonCreateDataSetFromRun | 

    try:
        # Create Data Set From Run
        api_response = await api_instance.create_data_set_from_run_api_data_sets_from_run_post(json_create_data_set_from_run)
        print("The response of DatasetsApi->create_data_set_from_run_api_data_sets_from_run_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->create_data_set_from_run_api_data_sets_from_run_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_create_data_set_from_run** | [**JsonCreateDataSetFromRun**](JsonCreateDataSetFromRun.md)|  | 

### Return type

[**JsonCreateDataSetFromRunOutput**](JsonCreateDataSetFromRunOutput.md)

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

# **delete_data_set_api_data_sets_delete**
> JsonDeleteDataSetOutput delete_data_set_api_data_sets_delete(json_delete_data_set_input)

Delete Data Set

### Example


```python
import openapi_client
from openapi_client.models.json_delete_data_set_input import JsonDeleteDataSetInput
from openapi_client.models.json_delete_data_set_output import JsonDeleteDataSetOutput
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
    api_instance = openapi_client.DatasetsApi(api_client)
    json_delete_data_set_input = openapi_client.JsonDeleteDataSetInput() # JsonDeleteDataSetInput | 

    try:
        # Delete Data Set
        api_response = await api_instance.delete_data_set_api_data_sets_delete(json_delete_data_set_input)
        print("The response of DatasetsApi->delete_data_set_api_data_sets_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->delete_data_set_api_data_sets_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_delete_data_set_input** | [**JsonDeleteDataSetInput**](JsonDeleteDataSetInput.md)|  | 

### Return type

[**JsonDeleteDataSetOutput**](JsonDeleteDataSetOutput.md)

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

# **read_data_sets_api_data_sets_beamtime_id_get**
> JsonReadDataSets read_data_sets_api_data_sets_beamtime_id_get(beamtime_id)

Read Data Sets

### Example


```python
import openapi_client
from openapi_client.models.json_read_data_sets import JsonReadDataSets
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
    api_instance = openapi_client.DatasetsApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Read Data Sets
        api_response = await api_instance.read_data_sets_api_data_sets_beamtime_id_get(beamtime_id)
        print("The response of DatasetsApi->read_data_sets_api_data_sets_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->read_data_sets_api_data_sets_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonReadDataSets**](JsonReadDataSets.md)

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

