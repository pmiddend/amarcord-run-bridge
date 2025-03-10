# openapi_client.RunsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_import_api_run_bulk_import_beamtime_id_post**](RunsApi.md#bulk_import_api_run_bulk_import_beamtime_id_post) | **POST** /api/run-bulk-import/{beamtimeId} | Bulk Import
[**bulk_import_info_api_run_bulk_import_beamtime_id_get**](RunsApi.md#bulk_import_info_api_run_bulk_import_beamtime_id_get) | **GET** /api/run-bulk-import/{beamtimeId} | Bulk Import Info
[**create_or_update_run_api_runs_run_external_id_post**](RunsApi.md#create_or_update_run_api_runs_run_external_id_post) | **POST** /api/runs/{runExternalId} | Create Or Update Run
[**delete_run_api_runs_beamtime_id_run_id_delete**](RunsApi.md#delete_run_api_runs_beamtime_id_run_id_delete) | **DELETE** /api/runs/{beamtimeId}/{runId} | Delete Run
[**read_runs_api_runs_beamtime_id_get**](RunsApi.md#read_runs_api_runs_beamtime_id_get) | **GET** /api/runs/{beamtimeId} | Read Runs
[**read_runs_bulk_api_runs_bulk_post**](RunsApi.md#read_runs_bulk_api_runs_bulk_post) | **POST** /api/runs-bulk | Read Runs Bulk
[**read_runs_overview_api_runs_overview_beamtime_id_get**](RunsApi.md#read_runs_overview_api_runs_overview_beamtime_id_get) | **GET** /api/runs-overview/{beamtimeId} | Read Runs Overview
[**start_run_api_runs_run_external_id_start_beamtime_id_get**](RunsApi.md#start_run_api_runs_run_external_id_start_beamtime_id_get) | **GET** /api/runs/{runExternalId}/start/{beamtimeId} | Start Run
[**stop_latest_run_api_runs_stop_latest_beamtime_id_get**](RunsApi.md#stop_latest_run_api_runs_stop_latest_beamtime_id_get) | **GET** /api/runs/stop-latest/{beamtimeId} | Stop Latest Run
[**update_run_api_runs_patch**](RunsApi.md#update_run_api_runs_patch) | **PATCH** /api/runs | Update Run
[**update_runs_bulk_api_runs_bulk_patch**](RunsApi.md#update_runs_bulk_api_runs_bulk_patch) | **PATCH** /api/runs-bulk | Update Runs Bulk


# **bulk_import_api_run_bulk_import_beamtime_id_post**
> JsonRunsBulkImportOutput bulk_import_api_run_bulk_import_beamtime_id_post(beamtime_id, simulate, create_data_sets, file)

Bulk Import

### Example


```python
import openapi_client
from openapi_client.models.json_runs_bulk_import_output import JsonRunsBulkImportOutput
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
    api_instance = openapi_client.RunsApi(api_client)
    beamtime_id = 56 # int | 
    simulate = True # bool | 
    create_data_sets = True # bool | 
    file = None # bytearray | 

    try:
        # Bulk Import
        api_response = await api_instance.bulk_import_api_run_bulk_import_beamtime_id_post(beamtime_id, simulate, create_data_sets, file)
        print("The response of RunsApi->bulk_import_api_run_bulk_import_beamtime_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->bulk_import_api_run_bulk_import_beamtime_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **simulate** | **bool**|  | 
 **create_data_sets** | **bool**|  | 
 **file** | **bytearray**|  | 

### Return type

[**JsonRunsBulkImportOutput**](JsonRunsBulkImportOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_import_info_api_run_bulk_import_beamtime_id_get**
> JsonRunsBulkImportInfo bulk_import_info_api_run_bulk_import_beamtime_id_get(beamtime_id)

Bulk Import Info

### Example


```python
import openapi_client
from openapi_client.models.json_runs_bulk_import_info import JsonRunsBulkImportInfo
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
    api_instance = openapi_client.RunsApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Bulk Import Info
        api_response = await api_instance.bulk_import_info_api_run_bulk_import_beamtime_id_get(beamtime_id)
        print("The response of RunsApi->bulk_import_info_api_run_bulk_import_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->bulk_import_info_api_run_bulk_import_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonRunsBulkImportInfo**](JsonRunsBulkImportInfo.md)

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

# **create_or_update_run_api_runs_run_external_id_post**
> JsonCreateOrUpdateRunOutput create_or_update_run_api_runs_run_external_id_post(run_external_id, json_create_or_update_run)

Create Or Update Run

### Example


```python
import openapi_client
from openapi_client.models.json_create_or_update_run import JsonCreateOrUpdateRun
from openapi_client.models.json_create_or_update_run_output import JsonCreateOrUpdateRunOutput
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
    api_instance = openapi_client.RunsApi(api_client)
    run_external_id = 56 # int | 
    json_create_or_update_run = openapi_client.JsonCreateOrUpdateRun() # JsonCreateOrUpdateRun | 

    try:
        # Create Or Update Run
        api_response = await api_instance.create_or_update_run_api_runs_run_external_id_post(run_external_id, json_create_or_update_run)
        print("The response of RunsApi->create_or_update_run_api_runs_run_external_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->create_or_update_run_api_runs_run_external_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_external_id** | **int**|  | 
 **json_create_or_update_run** | [**JsonCreateOrUpdateRun**](JsonCreateOrUpdateRun.md)|  | 

### Return type

[**JsonCreateOrUpdateRunOutput**](JsonCreateOrUpdateRunOutput.md)

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

# **delete_run_api_runs_beamtime_id_run_id_delete**
> JsonDeleteRunOutput delete_run_api_runs_beamtime_id_run_id_delete(beamtime_id, run_id)

Delete Run

### Example


```python
import openapi_client
from openapi_client.models.json_delete_run_output import JsonDeleteRunOutput
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
    api_instance = openapi_client.RunsApi(api_client)
    beamtime_id = 56 # int | 
    run_id = 56 # int | 

    try:
        # Delete Run
        api_response = await api_instance.delete_run_api_runs_beamtime_id_run_id_delete(beamtime_id, run_id)
        print("The response of RunsApi->delete_run_api_runs_beamtime_id_run_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->delete_run_api_runs_beamtime_id_run_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **run_id** | **int**|  | 

### Return type

[**JsonDeleteRunOutput**](JsonDeleteRunOutput.md)

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

# **read_runs_api_runs_beamtime_id_get**
> JsonReadRuns read_runs_api_runs_beamtime_id_get(beamtime_id, var_date=var_date, filter=filter, run_ranges=run_ranges)

Read Runs

### Example


```python
import openapi_client
from openapi_client.models.json_read_runs import JsonReadRuns
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
    api_instance = openapi_client.RunsApi(api_client)
    beamtime_id = 56 # int | 
    var_date = 'var_date_example' # str |  (optional)
    filter = 'filter_example' # str |  (optional)
    run_ranges = 'run_ranges_example' # str |  (optional)

    try:
        # Read Runs
        api_response = await api_instance.read_runs_api_runs_beamtime_id_get(beamtime_id, var_date=var_date, filter=filter, run_ranges=run_ranges)
        print("The response of RunsApi->read_runs_api_runs_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->read_runs_api_runs_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **var_date** | **str**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **run_ranges** | **str**|  | [optional] 

### Return type

[**JsonReadRuns**](JsonReadRuns.md)

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

# **read_runs_bulk_api_runs_bulk_post**
> JsonReadRunsBulkOutput read_runs_bulk_api_runs_bulk_post(json_read_runs_bulk_input)

Read Runs Bulk

### Example


```python
import openapi_client
from openapi_client.models.json_read_runs_bulk_input import JsonReadRunsBulkInput
from openapi_client.models.json_read_runs_bulk_output import JsonReadRunsBulkOutput
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
    api_instance = openapi_client.RunsApi(api_client)
    json_read_runs_bulk_input = openapi_client.JsonReadRunsBulkInput() # JsonReadRunsBulkInput | 

    try:
        # Read Runs Bulk
        api_response = await api_instance.read_runs_bulk_api_runs_bulk_post(json_read_runs_bulk_input)
        print("The response of RunsApi->read_runs_bulk_api_runs_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->read_runs_bulk_api_runs_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_read_runs_bulk_input** | [**JsonReadRunsBulkInput**](JsonReadRunsBulkInput.md)|  | 

### Return type

[**JsonReadRunsBulkOutput**](JsonReadRunsBulkOutput.md)

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

# **read_runs_overview_api_runs_overview_beamtime_id_get**
> JsonReadRunsOverview read_runs_overview_api_runs_overview_beamtime_id_get(beamtime_id)

Read Runs Overview

### Example


```python
import openapi_client
from openapi_client.models.json_read_runs_overview import JsonReadRunsOverview
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
    api_instance = openapi_client.RunsApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Read Runs Overview
        api_response = await api_instance.read_runs_overview_api_runs_overview_beamtime_id_get(beamtime_id)
        print("The response of RunsApi->read_runs_overview_api_runs_overview_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->read_runs_overview_api_runs_overview_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonReadRunsOverview**](JsonReadRunsOverview.md)

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

# **start_run_api_runs_run_external_id_start_beamtime_id_get**
> JsonStartRunOutput start_run_api_runs_run_external_id_start_beamtime_id_get(run_external_id, beamtime_id)

Start Run

### Example


```python
import openapi_client
from openapi_client.models.json_start_run_output import JsonStartRunOutput
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
    api_instance = openapi_client.RunsApi(api_client)
    run_external_id = 56 # int | 
    beamtime_id = 56 # int | 

    try:
        # Start Run
        api_response = await api_instance.start_run_api_runs_run_external_id_start_beamtime_id_get(run_external_id, beamtime_id)
        print("The response of RunsApi->start_run_api_runs_run_external_id_start_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->start_run_api_runs_run_external_id_start_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_external_id** | **int**|  | 
 **beamtime_id** | **int**|  | 

### Return type

[**JsonStartRunOutput**](JsonStartRunOutput.md)

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

# **stop_latest_run_api_runs_stop_latest_beamtime_id_get**
> JsonStopRunOutput stop_latest_run_api_runs_stop_latest_beamtime_id_get(beamtime_id)

Stop Latest Run

### Example


```python
import openapi_client
from openapi_client.models.json_stop_run_output import JsonStopRunOutput
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
    api_instance = openapi_client.RunsApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Stop Latest Run
        api_response = await api_instance.stop_latest_run_api_runs_stop_latest_beamtime_id_get(beamtime_id)
        print("The response of RunsApi->stop_latest_run_api_runs_stop_latest_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->stop_latest_run_api_runs_stop_latest_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonStopRunOutput**](JsonStopRunOutput.md)

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

# **update_run_api_runs_patch**
> JsonUpdateRunOutput update_run_api_runs_patch(json_update_run)

Update Run

### Example


```python
import openapi_client
from openapi_client.models.json_update_run import JsonUpdateRun
from openapi_client.models.json_update_run_output import JsonUpdateRunOutput
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
    api_instance = openapi_client.RunsApi(api_client)
    json_update_run = openapi_client.JsonUpdateRun() # JsonUpdateRun | 

    try:
        # Update Run
        api_response = await api_instance.update_run_api_runs_patch(json_update_run)
        print("The response of RunsApi->update_run_api_runs_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->update_run_api_runs_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_update_run** | [**JsonUpdateRun**](JsonUpdateRun.md)|  | 

### Return type

[**JsonUpdateRunOutput**](JsonUpdateRunOutput.md)

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

# **update_runs_bulk_api_runs_bulk_patch**
> JsonUpdateRunsBulkOutput update_runs_bulk_api_runs_bulk_patch(json_update_runs_bulk_input)

Update Runs Bulk

### Example


```python
import openapi_client
from openapi_client.models.json_update_runs_bulk_input import JsonUpdateRunsBulkInput
from openapi_client.models.json_update_runs_bulk_output import JsonUpdateRunsBulkOutput
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
    api_instance = openapi_client.RunsApi(api_client)
    json_update_runs_bulk_input = openapi_client.JsonUpdateRunsBulkInput() # JsonUpdateRunsBulkInput | 

    try:
        # Update Runs Bulk
        api_response = await api_instance.update_runs_bulk_api_runs_bulk_patch(json_update_runs_bulk_input)
        print("The response of RunsApi->update_runs_bulk_api_runs_bulk_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RunsApi->update_runs_bulk_api_runs_bulk_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_update_runs_bulk_input** | [**JsonUpdateRunsBulkInput**](JsonUpdateRunsBulkInput.md)|  | 

### Return type

[**JsonUpdateRunsBulkOutput**](JsonUpdateRunsBulkOutput.md)

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

