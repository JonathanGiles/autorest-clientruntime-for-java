#--------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# 
# Code generated by Microsoft (R) AutoRest Code Generator 0.13.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
#--------------------------------------------------------------------------

class BooleanWrapper(object):

    _required = []

    _attribute_map = {
        'field_true':{'key':'field_true', 'type':'bool'},
        'field_false':{'key':'field_false', 'type':'bool'},
    }

    def __init__(self, *args, **kwargs):

        self.field_true = None
        self.field_false = None

        for k in kwargs:
            if hasattr(self, k):
                setattr(self, k, kwargs[k])
