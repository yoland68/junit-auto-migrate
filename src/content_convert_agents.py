#!/usr/bin/env python

import model
import parser
import test_convert_agent

import re
import os
import collections
import codecs
import logging

class ConnectivityCheckerTestAgent(test_convert_agent.TestConvertAgent):
  """Agent for ConnectivityCheckerTestAgent direct childrens"""
  @staticmethod
  def class_runner():
    return ('BaseJUnit4ClassRunner',
            'org.chromium.base.test.BaseJUnit4ClassRunner')

  @classmethod
  def ignore_files(cls):
    return []

  @staticmethod
  def raw_api_mapping():
    result_mapping = collections.OrderedDict()
    result_mapping["ConnectivityCheckerTestBase"] = {
        "package": "org.chromium.chrome.browser.feedback",
        "location": "chrome/android/javatests/src/org/chromium/chrome/browser"
            +"/feedback/ConnectivityCheckerTestRule.java",
        "rule_var": "ConnectivityCheckerTestRule",
        "rule": "ConnectivityCheckerTestRule",
        "var": "mConnectivityCheckerTestRule",
        "instan": "ConnectivityCheckerTestRule()",
        "parent_key": None,
        "special_method_change": {}
    }
    return result_mapping

  def skip(self):
    if self.super_class_name != "ConnectivityCheckerTestBase":
      self.logger.debug('Skip: %s is not ConnectivityCheckerTestBase children'
                       % self._filepath)
      return True
    return False

  def actions(self):
    self.changeSetUpTearDown()
    self.changeAssertions()
    self.replaceInstrumentationApis()
    self.addClassRunner()
    self.addTestAnnotation()
    self.changeRunTestOnUiThread()
    self.importTypes()
    self.changeSendKeys()
    self.removeExtends()
    self.insertActivityTestRuleTest()
    self.changeApis()
    #Save file
    self.Save()

class SelectorObserverTest(test_convert_agent.TestConvertAgent):
  """Agent for SelectorObserverTestAgent direct childrens"""
  @staticmethod
  def class_runner():
    return ('BaseJUnit4ClassRunner',
            'org.chromium.base.test.BaseJUnit4ClassRunner')

  @classmethod
  def ignore_files(cls):
    return []

  @staticmethod
  def raw_api_mapping():
    result_mapping = collections.OrderedDict()
    result_mapping["TabModelSelectorObserverTestBase"] = {
        "package": "org.chromium.chrome.browser.tabmodel",
        "location": "chrome/android/javatests/src/org/chromium/chrome/browser"
            +"/tabmodel/TabModelSelectorObserverTestRule.java",
        "rule_var": "SelectorObserverTestRule",
        "rule": "SelectorObserverTestRule",
        "var": "mSelectorObserverTestRule",
        "instan": "SelectorObserverTestRule()",
        "parent_key": None,
        "special_method_change": {}
    }
    return result_mapping

  def skip(self):
    if self.super_class_name != "TabModelSelectorObserverTestBase":
      self.logger.debug('Skip: %s is not TabModelSelectorObserverTestBase children'
                       % self._filepath)
      return True
    return False

  def actions(self):
    self.changeSetUpTearDown()
    self.changeAssertions()
    self.replaceInstrumentationApis()
    self.addClassRunner()
    self.addTestAnnotation()
    self.changeRunTestOnUiThread()
    self.importTypes()
    self.changeSendKeys()
    self.removeExtends()
    self.insertActivityTestRuleTest()
    self.changeApis()
    #Save file
    self.Save()


