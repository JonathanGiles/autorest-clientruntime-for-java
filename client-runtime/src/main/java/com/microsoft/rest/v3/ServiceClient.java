/**
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for
 * license information.
 */

package com.microsoft.rest.v3;

import com.microsoft.rest.v3.http.HttpPipeline;
import com.microsoft.rest.v3.implementation.RestProxy;
import com.microsoft.rest.v3.implementation.serializer.SerializerAdapter;

/**
 * The base class for REST service clients.
 */
public abstract class ServiceClient {
    /**
     * The HTTP pipeline to send requests through.
     */
    private HttpPipeline httpPipeline;

    /**
     * The lazily-created serializer for this ServiceClient.
     */
    private SerializerAdapter serializerAdapter;

    /**
     * Creates ServiceClient.
     *
     * @param httpPipeline The HTTP pipeline to send requests through
     */
    protected ServiceClient(HttpPipeline httpPipeline) {
        this.httpPipeline = httpPipeline;
    }

    /**
     * @return the HTTP pipeline to send requests through.
     */
    public HttpPipeline httpPipeline() {
        return this.httpPipeline;
    }

    /**
     * @return the serializer for this ServiceClient.
     */
    public SerializerAdapter serializerAdapter() {
        if (this.serializerAdapter == null) {
            this.serializerAdapter = createSerializerAdapter();
        }
        return this.serializerAdapter;
    }

    protected SerializerAdapter createSerializerAdapter() {
        return RestProxy.createDefaultSerializer();
    }
}