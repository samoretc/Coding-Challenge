# Coding-Challenge

task-2.json is a json file of task data pulled from a Business Process Management system.  

Here is an example of one element in the json:
 {
   "instanceName": "New Coverage Branch: 486",
   "dueDate": "2014-10-06T23:32:33Z",
   "priority": "High",
   "closeDate": "2014-10-08T23:32:33Z",
   "instanceStatus": "Active",
   "assigneeType": "Group",
   "createDate": "2014-10-06T23:32:33Z",
   "name": "Review Coverage Branch Request",
   "url": "/teamworks/process.lsw?zWorkflowState=1&zTaskId=1433",
   "assignee": "Impact 2014",
   "instanceId": 486,
   "status": "Closed",
   "variables": {"CoverageBranchAnnualRevenue": {"value": 143193}},
   "processName": "New Coverage Branch",
   "id": "1433"
 }

Each instance can have one or more task.  In the above json block we are looking at a task and the instance related to that task.

instanceName: The name of the instance. 

name: The name of the task 

instanceId: The unique identifier for the instance 

id: The unique identifier for the task 

status: The status of the task

Your job is to read in these tasks and provide methods that answer the following questions:

Given a specific date provide the current number of open and closed tasks. The date is inclusive so if we ask for midnight Oct 12, a task opened or closed on midnight would count
Given a specific start and end date, how many tasks were opened and how many were closed in that range. The start date is inclusive, the end date is exclusive.
Given a particular instanceId, provide the name of the most recent task.
Given a particular instanceId, provide the count of tasks.
Given a particular assignee, provide the count of open and closed tasks for that assignee.

