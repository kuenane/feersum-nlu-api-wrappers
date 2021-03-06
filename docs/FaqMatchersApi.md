# feersum_nlu.FaqMatchersApi

All URIs are relative to *https://nlu.feersum.io:443/nlu/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**faq_matcher_add_testing_samples**](FaqMatchersApi.md#faq_matcher_add_testing_samples) | **POST** /faq_matchers/{instance_name}/testing_samples | Add testing samples.
[**faq_matcher_add_training_samples**](FaqMatchersApi.md#faq_matcher_add_training_samples) | **POST** /faq_matchers/{instance_name}/training_samples | Add training samples.
[**faq_matcher_create**](FaqMatchersApi.md#faq_matcher_create) | **POST** /faq_matchers | Create an FAQ matcher.
[**faq_matcher_curate**](FaqMatchersApi.md#faq_matcher_curate) | **POST** /faq_matchers/{instance_name}/curate | Endpoint to aid in the curation of a model instance.
[**faq_matcher_del**](FaqMatchersApi.md#faq_matcher_del) | **DELETE** /faq_matchers/{instance_name} | Delete named instance.
[**faq_matcher_del_testing_samples**](FaqMatchersApi.md#faq_matcher_del_testing_samples) | **DELETE** /faq_matchers/{instance_name}/testing_samples | Delete testing samples.
[**faq_matcher_del_testing_samples_all**](FaqMatchersApi.md#faq_matcher_del_testing_samples_all) | **DELETE** /faq_matchers/{instance_name}/testing_samples_all | Delete all testing samples.
[**faq_matcher_del_training_samples**](FaqMatchersApi.md#faq_matcher_del_training_samples) | **DELETE** /faq_matchers/{instance_name}/training_samples | Delete training samples.
[**faq_matcher_del_training_samples_all**](FaqMatchersApi.md#faq_matcher_del_training_samples_all) | **DELETE** /faq_matchers/{instance_name}/training_samples_all | Delete all training samples.
[**faq_matcher_get_details**](FaqMatchersApi.md#faq_matcher_get_details) | **GET** /faq_matchers/{instance_name} | Get details of named instance.
[**faq_matcher_get_details_all**](FaqMatchersApi.md#faq_matcher_get_details_all) | **GET** /faq_matchers | Get list of loaded FAQ matchers.
[**faq_matcher_get_labels**](FaqMatchersApi.md#faq_matcher_get_labels) | **GET** /faq_matchers/{instance_name}/get_labels | Get list of possible labels.
[**faq_matcher_get_params**](FaqMatchersApi.md#faq_matcher_get_params) | **GET** /faq_matchers/{instance_name}/params | Get the editable model parameters of named FAQ matcher.
[**faq_matcher_get_testing_samples**](FaqMatchersApi.md#faq_matcher_get_testing_samples) | **GET** /faq_matchers/{instance_name}/testing_samples | Get testing samples.
[**faq_matcher_get_training_samples**](FaqMatchersApi.md#faq_matcher_get_training_samples) | **GET** /faq_matchers/{instance_name}/training_samples | Get training samples.
[**faq_matcher_online_training_samples**](FaqMatchersApi.md#faq_matcher_online_training_samples) | **POST** /faq_matchers/{instance_name}/online_training_samples | Train/update the classifier online with the samples provided.
[**faq_matcher_retrieve**](FaqMatchersApi.md#faq_matcher_retrieve) | **POST** /faq_matchers/{instance_name}/retrieve | Match retrieve and FAQ.
[**faq_matcher_set_params**](FaqMatchersApi.md#faq_matcher_set_params) | **POST** /faq_matchers/{instance_name}/params | Set the model parameters of named FAQ matcher.
[**faq_matcher_train**](FaqMatchersApi.md#faq_matcher_train) | **POST** /faq_matchers/{instance_name}/train | Train the named FAQ matcher.
[**faq_matcher_vaporise**](FaqMatchersApi.md#faq_matcher_vaporise) | **POST** /faq_matchers/{instance_name}/vaporise | Vaporise the named model.


# **faq_matcher_add_testing_samples**
> TotalSamples faq_matcher_add_testing_samples(instance_name, labelled_text_sample_list)

Add testing samples.

Add testing samples to named faq matcher. Returns the FAQ matcher's updated number of testing samples.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.

try:
    # Add testing samples.
    api_response = api_instance.faq_matcher_add_testing_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_add_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_add_training_samples**
> TotalSamples faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)

Add training samples.

Add training samples to named faq matcher. Returns the FAQ matcher's updated number of training samples.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.

try:
    # Add training samples.
    api_response = api_instance.faq_matcher_add_training_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_add_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_create**
> FaqMatcherInstanceDetail faq_matcher_create(create_details)

Create an FAQ matcher.

Create a new faq matcher or reload one from the trash. Returns the details of the new or loaded instance.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
create_details = feersum_nlu.FaqMatcherCreateDetails() # FaqMatcherCreateDetails | The details of the instance to create.

try:
    # Create an FAQ matcher.
    api_response = api_instance.faq_matcher_create(create_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_details** | [**FaqMatcherCreateDetails**](FaqMatcherCreateDetails.md)| The details of the instance to create. | 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_curate**
> list[LabelledTextSample] faq_matcher_curate(instance_name, label_pair)

Endpoint to aid in the curation of a model instance.

Returns the list of samples behind a cell of the confusion matrix of the training or testing samples.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
label_pair = feersum_nlu.ClassLabelPair() # ClassLabelPair | The true label, predicted label and matrix (train/test) to use.

try:
    # Endpoint to aid in the curation of a model instance.
    api_response = api_instance.faq_matcher_curate(instance_name, label_pair)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_curate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **label_pair** | [**ClassLabelPair**](ClassLabelPair.md)| The true label, predicted label and matrix (train/test) to use. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_del**
> FaqMatcherInstanceDetail faq_matcher_del(instance_name)

Delete named instance.

Delete and return the details of the named FAQ matcher instance. Deleted models can be reloaded from the trash with the create operation.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete named instance.
    api_response = api_instance.faq_matcher_del(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_del_testing_samples**
> list[LabelledTextSample] faq_matcher_del_testing_samples(instance_name, labelled_text_sample_list)

Delete testing samples.

Delete the listed testing samples of the named FAQ matcher. Returns the deleted samples.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.

try:
    # Delete testing samples.
    api_response = api_instance.faq_matcher_del_testing_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_del_testing_samples_all**
> list[LabelledTextSample] faq_matcher_del_testing_samples_all(instance_name)

Delete all testing samples.

Delete all testing samples of the named FAQ matcher. Returns the deleted samples.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete all testing samples.
    api_response = api_instance.faq_matcher_del_testing_samples_all(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del_testing_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_del_training_samples**
> list[LabelledTextSample] faq_matcher_del_training_samples(instance_name, labelled_text_sample_list)

Delete training samples.

Delete the listed training samples of the named FAQ matcher. Returns the deleted samples.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.

try:
    # Delete training samples.
    api_response = api_instance.faq_matcher_del_training_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_del_training_samples_all**
> list[LabelledTextSample] faq_matcher_del_training_samples_all(instance_name)

Delete all training samples.

Delete all training samples of the named FAQ matcher. Returns the deleted samples.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Delete all training samples.
    api_response = api_instance.faq_matcher_del_training_samples_all(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_del_training_samples_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_details**
> FaqMatcherInstanceDetail faq_matcher_get_details(instance_name)

Get details of named instance.

Get the details of the named FAQ matcher instance.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get details of named instance.
    api_response = api_instance.faq_matcher_get_details(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_details_all**
> list[FaqMatcherInstanceDetail] faq_matcher_get_details_all()

Get list of loaded FAQ matchers.

Returns the list of loaded faq matchers.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))

try:
    # Get list of loaded FAQ matchers.
    api_response = api_instance.faq_matcher_get_details_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_details_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FaqMatcherInstanceDetail]**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_labels**
> list[ClassLabel] faq_matcher_get_labels(instance_name)

Get list of possible labels.

Returns the classifier's list of possible class labels.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get list of possible labels.
    api_response = api_instance.faq_matcher_get_labels(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[ClassLabel]**](ClassLabel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_params**
> ModelParams faq_matcher_get_params(instance_name)

Get the editable model parameters of named FAQ matcher.

Get the editable model parameters of FAQ matcher.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get the editable model parameters of named FAQ matcher.
    api_response = api_instance.faq_matcher_get_params(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**ModelParams**](ModelParams.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_testing_samples**
> list[LabelledTextSample] faq_matcher_get_testing_samples(instance_name)

Get testing samples.

Returns the testing samples of the named faq matcher.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get testing samples.
    api_response = api_instance.faq_matcher_get_testing_samples(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_testing_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_get_training_samples**
> list[LabelledTextSample] faq_matcher_get_training_samples(instance_name)

Get training samples.

Returns the training samples of the named faq matcher.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Get training samples.
    api_response = api_instance.faq_matcher_get_training_samples(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_get_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**list[LabelledTextSample]**](LabelledTextSample.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_online_training_samples**
> TotalSamples faq_matcher_online_training_samples(instance_name, labelled_text_sample_list)

Train/update the classifier online with the samples provided.

Train/update the classifier online with the samples provided. This operation is more efficient than a full re-train. Returns the classifier's updated number of training samples.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
labelled_text_sample_list = [feersum_nlu.LabelledTextSample()] # list[LabelledTextSample] | List of labelled text samples.

try:
    # Train/update the classifier online with the samples provided.
    api_response = api_instance.faq_matcher_online_training_samples(instance_name, labelled_text_sample_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_online_training_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **labelled_text_sample_list** | [**list[LabelledTextSample]**](LabelledTextSample.md)| List of labelled text samples. | 

### Return type

[**TotalSamples**](TotalSamples.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_retrieve**
> list[ScoredLabel] faq_matcher_retrieve(instance_name, text_input)

Match retrieve and FAQ.

Matchers the FAQ and returns a probability sorted list of answer labels.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
text_input = feersum_nlu.TextInput() # TextInput | The input text.

try:
    # Match retrieve and FAQ.
    api_response = api_instance.faq_matcher_retrieve(instance_name, text_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **text_input** | [**TextInput**](TextInput.md)| The input text. | 

### Return type

[**list[ScoredLabel]**](ScoredLabel.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_set_params**
> FaqMatcherInstanceDetail faq_matcher_set_params(instance_name, model_params)

Set the model parameters of named FAQ matcher.

Set the model parameters of FAQ matcher.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
model_params = feersum_nlu.ModelParams() # ModelParams | The model parameters.

try:
    # Set the model parameters of named FAQ matcher.
    api_response = api_instance.faq_matcher_set_params(instance_name, model_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_set_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **model_params** | [**ModelParams**](ModelParams.md)| The model parameters. | 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_train**
> FaqMatcherInstanceDetail faq_matcher_train(instance_name, train_details)

Train the named FAQ matcher.

Train the named FAQ matcher with the training and testing data already provided. Returns the updated instance detail.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.
train_details = feersum_nlu.TrainDetails() # TrainDetails | The arguments provided to the train operation.

try:
    # Train the named FAQ matcher.
    api_response = api_instance.faq_matcher_train(instance_name, train_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_train: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 
 **train_details** | [**TrainDetails**](TrainDetails.md)| The arguments provided to the train operation. | 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **faq_matcher_vaporise**
> FaqMatcherInstanceDetail faq_matcher_vaporise(instance_name)

Vaporise the named model.

Permanently vaporises a model even if not trashed.

### Example
```python
from __future__ import print_function
import time
import feersum_nlu
from feersum_nlu.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = feersum_nlu.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'
# Configure API key authorization: APIKeyHeader_old
configuration = feersum_nlu.Configuration()
configuration.api_key['AUTH_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AUTH_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = feersum_nlu.FaqMatchersApi(feersum_nlu.ApiClient(configuration))
instance_name = 'instance_name_example' # str | The name of the model instance.

try:
    # Vaporise the named model.
    api_response = api_instance.faq_matcher_vaporise(instance_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FaqMatchersApi->faq_matcher_vaporise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_name** | **str**| The name of the model instance. | 

### Return type

[**FaqMatcherInstanceDetail**](FaqMatcherInstanceDetail.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyHeader_old](../README.md#APIKeyHeader_old)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

