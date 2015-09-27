import json
from pprint import pprint
import pdb
from datetime import datetime

class Task(object): 
	def __init__(self, arr):
		self.instanceName = arr['instanceName'] 
		self.dueDate = datetime.strptime( arr['dueDate'], "%Y-%m-%dT%H:%M:%SZ") if arr['dueDate'] != None else None
		self.priority = arr['priority']
		self.closeDate = datetime.strptime( arr['closeDate'], "%Y-%m-%dT%H:%M:%SZ") if arr['closeDate'] != None else None
		self.instanceStatus = arr['instanceStatus']
		self.assigneeType = arr['assigneeType']
		self.createDate =  datetime.strptime(arr['createDate'], "%Y-%m-%dT%H:%M:%SZ") if arr['createDate'] != None else None
		self.name = arr['name']
		self.url = arr['url']
		self.assignee = arr['assignee']
		self.instanceId = arr['instanceId']
		self.status = arr['status']
		self.variables = arr['variables']
		self.processName = arr['processName']
		self.id = arr['id']

class QueryTask(object): 

	def __init__(self, tasks): 
		self.tasks = tasks
	
	"""Given a specific date provide the current number of open and closed tasks. 
	The date is inclusive so if we ask for midnight Oct 12, a task opened or closed 
	on midnight would count"""
	def numOfOpenClosedTasksOnDate(self, date):
		# First if a task was created after date than it was neither open nor closed. 
		createdBefore = filter( lambda x: x.createDate < date , self.tasks)
		
		# I'm not sure which way is right. I wold have that they would retrunt he same results
		openTasks = filter(lambda x: x.status =='Received', createdBefore)
		closedTasks = filter(lambda x: x.status=='Closed',  createdBefore)

		openTasks = filter(lambda x: x.closeDate < date , createdBefore)
		closedTasks = filter(lambda x: date < x.closeDate, createdBefore)
		return openTasks, closedTasks

	"""Given a specific start and end date, how many tasks were opened and 
	how many were closed in that range. The start date is inclusive, the end 
	date is exclusive."""
	def openBetweenDates(self, openDate, closeDate): 
		return { 'tasksOpened' : filter( lambda x : openDate < x.createDate and (openDate < x.closeDate or x.closeDate == None),  self.tasks) }
	

	"""Given a particular instanceId, provide the name of the most recent task.
	
	What's weird aboutt his is that the tasks with the same instanceID have all had 
	the same task task names from my analysis """
	def mostRecentTaskNameforInstanceId(self, instanceId):
		tasksWithInstanceId = filter( lambda x : x.instanceId == instanceId , self.tasks )
		return max( tasksWithInstanceId , key=lambda x: x.createDate).name 

	"""Given a particular instanceId, provide the count of tasks."""
	def countforInstanceId(self, instanceId): 
		return len( filter(  lambda x : x.instanceId == instanceId   , self.tasks) )

	""" Given a particular assignee, provide the count of open and closed tasks for that assignee.

	I believe this query is for the current time """
	def openAndClosedTaskforAssignee(self, assignee):
		return {   'openTasks' : filter(  lambda x : x.assignee == assignee and x.status == 'Recieved', self.tasks),
				  'closedTasks': filter(  lambda x : x.assignee == assignee and x.status == 'Closed',   self.tasks) }



if __name__ == '__main__':
	json_data = open('task-2.json').read()
	data = json.loads(json_data)
	pprint
	tasks = []
	with open('task-2.json') as data_file:
		data = json.load(data_file)

	for  i in data:
		tasks.append(Task(i))

	QueryTask = QueryTask(tasks)
	print QueryTask.countforInstanceId(680)
	print QueryTask.mostRecentTaskNameforInstanceId(680)
