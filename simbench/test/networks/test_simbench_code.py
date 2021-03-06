# -*- coding: utf-8 -*-

# Copyright (c) 2019 by University of Kassel, Tu Dortmund, RWTH Aachen University and Fraunhofer
# Institute for Energy Economics and Energy System Technology (IEE) Kassel and individual
# contributors (see AUTHORS file for details). All rights reserved.

import pytest

import simbench as sb

__author__ = "smeinecke"


def _occurance_test(code_list, code_to_test):
    assert code_to_test in code_list


def test_simbench_code_occurance():
    all_ = sb.collect_all_simbench_codes()

    _occurance_test(all_, "1-complete_data-mixed-all-1-sw")
    _occurance_test(all_, "1-EHVHVMVLV-mixed-all-2-sw")
    _occurance_test(all_, "1-HVMV-mixed-all-0-sw")
    _occurance_test(all_, "1-MVLV-urban-5.303-1-no_sw")
    _occurance_test(all_, "1-HV-mixed--0-sw")
    _occurance_test(all_, "1-MV-semiurb--0-sw")
    _occurance_test(all_, "1-LV-rural1--2-sw")
    _occurance_test(all_, "1-EHVHV-mixed-1-0-no_sw")
    _occurance_test(all_, "1-HV-urban--2-sw")


def test_simbench_code_conversion():
    all_ = sb.collect_all_simbench_codes()
    for input_code in all_:
        sb_code_parameters = sb.get_parameters_from_simbench_code(input_code)
        output_code = sb.get_simbench_code_from_parameters(sb_code_parameters)
        assert input_code == output_code


if __name__ == '__main__':
    if 0:
        pytest.main(["test_simbench_code.py", "-xs"])
    else:
#        test_simbench_code_occurance()
#        test_simbench_code_conversion()
        pass
