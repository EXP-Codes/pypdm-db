#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# PDM: @{table_name}
# -------------------------------

class @{TableName} :
    table_name = "@{table_name}"
@{columns}


    def __init__(self) :
@{variables}


    def params(self) :
        return (
@{params}
        )


    def __repr__(self) :
        return "\n".join(
            (
                "%s: {" % self.table_name,
@{kvs}
                "}\n"
            )
        )
