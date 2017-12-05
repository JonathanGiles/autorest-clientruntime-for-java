/**
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for
 * license information.
 */

package com.microsoft.rest.v2.policy;

import com.microsoft.rest.v2.http.HttpPipeline;

/**
 * An abstract RequestPolicy base-class.
 */
public abstract class AbstractRequestPolicy implements RequestPolicy {
    private final RequestPolicy nextPolicy;
    private final Options options;
    private final HttpPipeline.Logger logger;

    /**
     * Initialize the fields for this AbstractRequestPolicy.
     * @param nextPolicy The next RequestPolicy in the policy chain.
     * @param options The options for this RequestPolicy.
     */
    protected AbstractRequestPolicy(RequestPolicy nextPolicy, Options options) {
        this.nextPolicy = nextPolicy;
        this.options = options;
        this.logger = options == null ? null : options.logger();
    }

    /**
     * Get the next RequestPolicy in the policy chain.
     * @return The next RequestPolicy in the policy chain.
     */
    protected RequestPolicy nextPolicy() {
        return nextPolicy;
    }

    /**
     * Get the options that were provided to this AbstractRequestPolicy.
     * @return The options that were provided to this AbstractRequestPolicy.
     */
    protected Options options() {
        return options;
    }

    /**
     * Get the logger that was provided to this AbstractRequestPolicy.
     * @return The logger that was provided to this AbstractRequestPolicy.
     */
    protected HttpPipeline.Logger logger() {
        return logger;
    }

    /**
     * Attempt to log the provided message to the provided logger. If no logger was provided or if
     * the log level does not meat the logger's threshold, then nothing will be logged.
     * @param logLevel The log level of this log.
     * @param message The message of this log.
     * @param formattedMessageArguments The formatted arguments to apply to the message.
     */
    protected void log(HttpPipeline.LogLevel logLevel, String message, Object... formattedMessageArguments) {
        if (logger != null && logLevel.ordinal() < logger.minimumLogLevel().ordinal()) {
            logger.log(logLevel, message, formattedMessageArguments);
        }
    }
}