// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
package com.microsoft.rest.v3.http.rest;

import com.microsoft.rest.v3.http.HttpHeaders;
import com.microsoft.rest.v3.http.HttpRequest;

import java.util.Map;

/**
 * REST response containing only a status code and raw headers.
 */
public final class RestVoidResponse extends SimpleRestResponse<Void> {
    /**
     * Creates RestVoidResponse.
     *
     * @param request the request which resulted in this response
     * @param statusCode the status code of the HTTP response
     * @param headers the headers of the HTTP response
     */
    public RestVoidResponse(HttpRequest request, int statusCode, HttpHeaders headers) {
        super(request, statusCode, headers, null);
    }

}
