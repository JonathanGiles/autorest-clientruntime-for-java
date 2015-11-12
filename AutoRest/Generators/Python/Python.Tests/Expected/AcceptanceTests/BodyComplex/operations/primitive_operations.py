#--------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# 
# Code generated by Microsoft (R) AutoRest Code Generator 0.13.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
#--------------------------------------------------------------------------

import sys


from msrest.service_client import ServiceClient
from msrest.serialization import Serializer, Deserializer
from msrest.exceptions import (
    SerializationError,
    DeserializationError,
    TokenExpiredError,
    ClientRequestError,
    HttpOperationError)

from ..models import *

class PrimitiveOperations(object):

    def __init__(self, client, config, serializer, derserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = derserializer

        self.config = config

    def _parse_url(self, name, value, datatype):

        try:
            value = self._serialize.serialize_data(value, str(datatype))

        except ValueError:
            raise ValueError("{} must not be None.".format(name))

        except DeserializationError:
            raise TypeError("{} must be type {}.".format(name, datatype))

        else:
            return value

    @ServiceClient.async_request
    def get_int(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with integer properties
        """

        # Construct URL
        url = '/complex/primitive/integer'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('IntWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_int(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with integer properties
        """

        # Construct URL
        url = '/complex/primitive/integer'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_long(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with long properties
        """

        # Construct URL
        url = '/complex/primitive/long'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('LongWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_long(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with long properties
        """

        # Construct URL
        url = '/complex/primitive/long'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_float(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with float properties
        """

        # Construct URL
        url = '/complex/primitive/float'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('FloatWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_float(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with float properties
        """

        # Construct URL
        url = '/complex/primitive/float'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_double(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with double properties
        """

        # Construct URL
        url = '/complex/primitive/double'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DoubleWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_double(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with double properties
        """

        # Construct URL
        url = '/complex/primitive/double'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_bool(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with bool properties
        """

        # Construct URL
        url = '/complex/primitive/bool'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('BooleanWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_bool(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with bool properties
        """

        # Construct URL
        url = '/complex/primitive/bool'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_string(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with string properties
        """

        # Construct URL
        url = '/complex/primitive/string'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('StringWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_string(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with string properties
        """

        # Construct URL
        url = '/complex/primitive/string'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_date(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with date properties
        """

        # Construct URL
        url = '/complex/primitive/date'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DateWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_date(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with date properties
        """

        # Construct URL
        url = '/complex/primitive/date'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_date_time(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with datetime properties
        """

        # Construct URL
        url = '/complex/primitive/datetime'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DatetimeWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_date_time(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with datetime properties
        """

        # Construct URL
        url = '/complex/primitive/datetime'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_date_time_rfc1123(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with datetimeRfc1123 properties
        """

        # Construct URL
        url = '/complex/primitive/datetimerfc1123'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Datetimerfc1123Wrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_date_time_rfc1123(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with datetimeRfc1123 properties
        """

        # Construct URL
        url = '/complex/primitive/datetimerfc1123'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_duration(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with duration properties
        """

        # Construct URL
        url = '/complex/primitive/duration'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DurationWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_duration(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with duration properties
        """

        # Construct URL
        url = '/complex/primitive/duration'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @ServiceClient.async_request
    def get_byte(self, custom_headers = {}, raw = False, callback = None):
        """

        Get complex types with byte properties
        """

        # Construct URL
        url = '/complex/primitive/byte'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ByteWrapper', response)

        if raw:
            return deserialized, response

        return deserialized

    @ServiceClient.async_request
    def put_byte(self, complex_body, custom_headers = {}, raw = False, callback = None):
        """

        Put complex types with byte properties
        """

        # Construct URL
        url = '/complex/primitive/byte'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(complex_body)

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response
