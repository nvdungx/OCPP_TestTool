# OpenChargePointProtocol Test Environment

## Description
Automation test environment for validating OCPP protocol implementation
  of Charging Station or Charging Station Management System.

## System requirements
Target of system:
  - OCPP version 2.0.1 [SYS.001]
  - SUT could be either CS or CSMS (i.e. TestEnvironment act as CSMS or
    CS emulation). [SYS.002]
  - Web base user interface: [SYS.003]
    - Direct interact with SUT. [SYS.004]
    - Support both GUI or console when interact with SUT. [SYS.005]
    - Manual or auto execute test script with interactive graphical interface. [SYS.006]
  - User can create test script with Web base GUI or by text file defined syntax. [SYS.007]
  - User can config how validate operation carry out in test case. [SYS.008]
  - User can create abnormal operation condition. [SYS.009]
  - Local CLI extension for CI/CD integration. [SYS.010]
  - Tool come with list of test suites to test normal operation according to
    OCPP specification. [SYS.011]