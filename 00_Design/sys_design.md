# OpenChargePointProtocol Test Environment

## **System component**

| Component | Description |
|--------|--------|
| Web UI | Front end application, user interaction with test environment |
| TestFrame| server operation for Web UI, execute test operation to SUT, can directly interact in local host |

----------
### **I. Web UI**
- no framework, http web page
- test environment config page
- test case creation page
- test case execution page
- test report page
- manual interaction page
- interaction could be done by GUI or console
- http with TestFrame server
----------
### **II. TestFrame**
- django module (web UI interaction handling api)
- sqlite (data storage: test case, test report)
- bridge (communication between test framework and django module)
- test framework (python, websocket, ocpp, exposed direct access for CI/CD)

#### [TestTool come with predefine test suites]