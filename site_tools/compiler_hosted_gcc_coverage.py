#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014-2016, German Aerospace Center (DLR)
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Authors:
# - 2014-2016, Fabian Greif (DLR RY-AVS)

from SCons.Script import *


def generate(env, **kw):
    env.Tool('compiler_hosted_gcc')

    env.Append(CCFLAGS='--coverage')
    env.Append(LINKFLAGS='--coverage')

    env['CCFLAGS_optimize'] = [
        '-O1',
        '-fno-default-inline',
        '-fno-inline-functions',
        '-fno-inline',
    ]

    # Suppress warnings generated by gmock
    env.AppendUnique(CCFLAGS_warning='-Wno-unused-local-typedefs')

    # The C++ standard allows an implementation to omit creating a temporary
    # which is only used to initialize another object of the same type.
    # Specifying this option disables that optimization, and forces G++ to
    # call the copy constructor in all cases.
    env.AppendUnique(CXXFLAGS='-fno-elide-constructors')


def exists(env):
    return env.Detect('gcc')

