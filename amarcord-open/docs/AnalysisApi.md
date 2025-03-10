# openapi_client.AnalysisApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_analysis_results_api_analysis_analysis_results_post**](AnalysisApi.md#read_analysis_results_api_analysis_analysis_results_post) | **POST** /api/analysis/analysis-results | Read Analysis Results
[**read_beamtime_geometry_details_api_run_analysis_beamtime_id_geometry_get**](AnalysisApi.md#read_beamtime_geometry_details_api_run_analysis_beamtime_id_geometry_get) | **GET** /api/run-analysis/{beamtimeId}/geometry | Read Beamtime Geometry Details
[**read_run_analysis_api_run_analysis_beamtime_id_get**](AnalysisApi.md#read_run_analysis_api_run_analysis_beamtime_id_get) | **GET** /api/run-analysis/{beamtimeId} | Read Run Analysis
[**read_single_data_set_results_api_analysis_single_data_set_beamtime_id_data_set_id_get**](AnalysisApi.md#read_single_data_set_results_api_analysis_single_data_set_beamtime_id_data_set_id_get) | **GET** /api/analysis/single-data-set/{beamtimeId}/{dataSetId} | Read Single Data Set Results
[**read_single_merge_result_api_analysis_merge_result_beamtime_id_experiment_type_id_merge_result_id_get**](AnalysisApi.md#read_single_merge_result_api_analysis_merge_result_beamtime_id_experiment_type_id_merge_result_id_get) | **GET** /api/analysis/merge-result/{beamtimeId}/{experimentTypeId}/{mergeResultId} | Read Single Merge Result


# **read_analysis_results_api_analysis_analysis_results_post**
> JsonReadNewAnalysisOutput read_analysis_results_api_analysis_analysis_results_post(json_read_new_analysis_input)

Read Analysis Results

### Example


```python
import openapi_client
from openapi_client.models.json_read_new_analysis_input import JsonReadNewAnalysisInput
from openapi_client.models.json_read_new_analysis_output import JsonReadNewAnalysisOutput
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
    api_instance = openapi_client.AnalysisApi(api_client)
    json_read_new_analysis_input = openapi_client.JsonReadNewAnalysisInput() # JsonReadNewAnalysisInput | 

    try:
        # Read Analysis Results
        api_response = await api_instance.read_analysis_results_api_analysis_analysis_results_post(json_read_new_analysis_input)
        print("The response of AnalysisApi->read_analysis_results_api_analysis_analysis_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->read_analysis_results_api_analysis_analysis_results_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_read_new_analysis_input** | [**JsonReadNewAnalysisInput**](JsonReadNewAnalysisInput.md)|  | 

### Return type

[**JsonReadNewAnalysisOutput**](JsonReadNewAnalysisOutput.md)

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

# **read_beamtime_geometry_details_api_run_analysis_beamtime_id_geometry_get**
> JsonReadBeamtimeGeometryDetails read_beamtime_geometry_details_api_run_analysis_beamtime_id_geometry_get(beamtime_id)

Read Beamtime Geometry Details

### Example


```python
import openapi_client
from openapi_client.models.json_read_beamtime_geometry_details import JsonReadBeamtimeGeometryDetails
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
    api_instance = openapi_client.AnalysisApi(api_client)
    beamtime_id = 56 # int | 

    try:
        # Read Beamtime Geometry Details
        api_response = await api_instance.read_beamtime_geometry_details_api_run_analysis_beamtime_id_geometry_get(beamtime_id)
        print("The response of AnalysisApi->read_beamtime_geometry_details_api_run_analysis_beamtime_id_geometry_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->read_beamtime_geometry_details_api_run_analysis_beamtime_id_geometry_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 

### Return type

[**JsonReadBeamtimeGeometryDetails**](JsonReadBeamtimeGeometryDetails.md)

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

# **read_run_analysis_api_run_analysis_beamtime_id_get**
> JsonReadRunAnalysis read_run_analysis_api_run_analysis_beamtime_id_get(beamtime_id, run_id=run_id)

Read Run Analysis

### Example


```python
import openapi_client
from openapi_client.models.json_read_run_analysis import JsonReadRunAnalysis
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
    api_instance = openapi_client.AnalysisApi(api_client)
    beamtime_id = 56 # int | 
    run_id = 56 # int |  (optional)

    try:
        # Read Run Analysis
        api_response = await api_instance.read_run_analysis_api_run_analysis_beamtime_id_get(beamtime_id, run_id=run_id)
        print("The response of AnalysisApi->read_run_analysis_api_run_analysis_beamtime_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->read_run_analysis_api_run_analysis_beamtime_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **run_id** | **int**|  | [optional] 

### Return type

[**JsonReadRunAnalysis**](JsonReadRunAnalysis.md)

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

# **read_single_data_set_results_api_analysis_single_data_set_beamtime_id_data_set_id_get**
> JsonReadSingleDataSetResults read_single_data_set_results_api_analysis_single_data_set_beamtime_id_data_set_id_get(beamtime_id, data_set_id)

Read Single Data Set Results

### Example


```python
import openapi_client
from openapi_client.models.json_read_single_data_set_results import JsonReadSingleDataSetResults
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
    api_instance = openapi_client.AnalysisApi(api_client)
    beamtime_id = 56 # int | 
    data_set_id = 56 # int | 

    try:
        # Read Single Data Set Results
        api_response = await api_instance.read_single_data_set_results_api_analysis_single_data_set_beamtime_id_data_set_id_get(beamtime_id, data_set_id)
        print("The response of AnalysisApi->read_single_data_set_results_api_analysis_single_data_set_beamtime_id_data_set_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->read_single_data_set_results_api_analysis_single_data_set_beamtime_id_data_set_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **data_set_id** | **int**|  | 

### Return type

[**JsonReadSingleDataSetResults**](JsonReadSingleDataSetResults.md)

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

# **read_single_merge_result_api_analysis_merge_result_beamtime_id_experiment_type_id_merge_result_id_get**
> JsonReadSingleMergeResult read_single_merge_result_api_analysis_merge_result_beamtime_id_experiment_type_id_merge_result_id_get(beamtime_id, experiment_type_id, merge_result_id)

Read Single Merge Result

### Example


```python
import openapi_client
from openapi_client.models.json_read_single_merge_result import JsonReadSingleMergeResult
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
    api_instance = openapi_client.AnalysisApi(api_client)
    beamtime_id = 56 # int | 
    experiment_type_id = 56 # int | 
    merge_result_id = 56 # int | 

    try:
        # Read Single Merge Result
        api_response = await api_instance.read_single_merge_result_api_analysis_merge_result_beamtime_id_experiment_type_id_merge_result_id_get(beamtime_id, experiment_type_id, merge_result_id)
        print("The response of AnalysisApi->read_single_merge_result_api_analysis_merge_result_beamtime_id_experiment_type_id_merge_result_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->read_single_merge_result_api_analysis_merge_result_beamtime_id_experiment_type_id_merge_result_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beamtime_id** | **int**|  | 
 **experiment_type_id** | **int**|  | 
 **merge_result_id** | **int**|  | 

### Return type

[**JsonReadSingleMergeResult**](JsonReadSingleMergeResult.md)

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

