#--------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# 
# Code generated by Microsoft (R) AutoRest Code Generator 0.13.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
#--------------------------------------------------------------------------

class DatetimeWrapper(object):

    _required = []

    _attribute_map = {
        'field':{'key':'field', 'type':'iso-date'},
        'now':{'key':'now', 'type':'iso-date'},
    }

    def __init__(self, *args, **kwargs):

        self.field = None
        self.now = None

        for k in kwargs:
            if hasattr(self, k):
                setattr(self, k, kwargs[k])
