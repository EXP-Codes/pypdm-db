#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------
# PDM: t_teachers
# -------------------------------

class TTeachers :
    table_name = 't_teachers'
    i_id = "i_id"
    s_name = "s_name"
    s_remark = "s_remark"


    def __init__(self) :
        self.id = None
        self.name = None
        self.remark = None


    def params(self) :
        return (
            self.name,
            self.remark,
        )


    def __repr__(self) :
        return '\n'.join(
            (
                '%s: {' % self.table_name,
                "    %s = %s" % (self.i_id, self.id),
                "    %s = %s" % (self.s_name, self.name),
                "    %s = %s" % (self.s_remark, self.remark),
                '}\n'
            )
        )
