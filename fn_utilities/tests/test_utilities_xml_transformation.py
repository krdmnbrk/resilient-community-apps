# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import os
import pytest
from fn_utilities.util.utils_common import b_to_s
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_xml_transformation"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_utilities_xml_transformation_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_xml_transformation", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_xml_transformation_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesXmlTransformation:
    """ Tests for the utilities_xml_transformation function"""
    DATA_DIR = "data/xmltransformation"

    @pytest.mark.livetest
    @pytest.mark.parametrize("xml_source, xml_stylesheet, expected_results", [
        ("cdcatalog.xml", "cdcatalog.xslt", "cdcatalog.html")
    ])
    def test_success(self, circuits_app, xml_source, xml_stylesheet, expected_results):
        curr_dir = os.path.dirname(os.path.realpath(__file__))

        xml_data = open(os.path.join(curr_dir, TestUtilitiesXmlTransformation.DATA_DIR, xml_source), mode="rb").read()
        expected_results = open(os.path.join(curr_dir, TestUtilitiesXmlTransformation.DATA_DIR, expected_results), mode="r").read()

        """ Test calling with sample values for the parameters """
        function_params = {
            "xml_source": b_to_s(xml_data),
            "xml_stylesheet": xml_stylesheet
        }

        results = call_utilities_xml_transformation_function(circuits_app, function_params)

        assert expected_results == results['content']