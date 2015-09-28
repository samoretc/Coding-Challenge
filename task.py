import json
from pprint import pprint
import pdb
from datetime import datetime, timedelta

class Task(object): 
	def __init__(self, dic):
		self.instanceName = dic['instanceName'] 
		self.closeDate = datetime.strptime( dic['closeDate'], "%Y-%m-%dT%H:%M:%SZ") if dic['closeDate'] != None else None
		self.createDate =  datetime.strptime(dic['createDate'], "%Y-%m-%dT%H:%M:%SZ")
		self.name = dic['name']
		self.assignee = dic['assignee']
		self.instanceId = int(dic['instanceId'])
		self.status = dic['status']
		self.id = int(dic['id'])

class QueryTask(object): 

	def __init__(self, tasks): 
		self.tasks = tasks
	
	"""Given a specific date provide the current number of open and closed tasks. 
	The date is inclusive so if we ask for midnight Oct 12, a task opened or closed 
	on midnight would count"""
	def numOfOpenClosedTasksAtTime(self, time): 
		time =  datetime.strptime( time, "%Y-%m-%dT%H:%M:%SZ") 
		createdBeforeAndWithEndDate = filter( lambda x: x.createDate <= time and x.closeDate != None , self.tasks)
		closedTasks = len ( filter(lambda x: x.closeDate <= time , createdBeforeAndWithEndDate) )
		openTasksWithEndDate = 	len ( filter(lambda x: time < x.closeDate, createdBeforeAndWithEndDate) ) 
		openTasksWithoutEndDate=len ( filter(lambda x: x.createDate <= time and x.closeDate == None, self.tasks) )
		openTasks = openTasksWithEndDate + openTasksWithoutEndDate
		return openTasks, closedTasks
        
	"""Given a specific start and end date, how many tasks were opened and 
	how many were closed in that range. The start date is inclusive, the end 
	date is exclusive."""
	def numBetweenDates(self, startDate, closeDate):
		startDate =  datetime.strptime( startDate, "%Y-%m-%dT%H:%M:%SZ") 
		closeDate =  datetime.strptime( closeDate, "%Y-%m-%dT%H:%M:%SZ") 
		numOpened = len ( filter( lambda x : startDate <= x.createDate and x.createDate < closeDate,  self.tasks) )
		notClosedYet = filter( lambda x: x.closeDate != None, self.tasks)
		numClosed = len ( filter( lambda x : startDate <= x.closeDate  and x.closeDate < closeDate, notClosedYet  ) ) 
		return numOpened, numClosed	

	"""Given a particular instanceId, provide the name of the most recent task.
	What's weird aboutt his is that the tasks with the same instanceID have all had 
	the same task task names from my analysis """
	def mostRecentTaskNameforInstanceId(self, instanceId):
		tasksWithInstanceId = filter( lambda x : x.instanceId == instanceId , self.tasks )
		return max( tasksWithInstanceId , key=lambda x: x.createDate).name 

	"""Given a particular instanceId, provide the count of tasks."""
	def countforInstanceId(self, instanceId): 
		return len( filter(  lambda x : x.instanceId == instanceId   , self.tasks) )

	""" Given a particular assignee, provide the count of open and closed tasks for that assignee."""
	def openAndClosedTaskforAssignee(self, assignee):
		openTasks  = len( filter(  lambda x : x.assignee == assignee and x.status == 'Recieved', self.tasks) ) 
		closedTasks= len( filter(  lambda x : x.assignee == assignee and x.status == 'Closed',   self.tasks) )
		return openTasks, closedTasks



if __name__ == '__main__':
	tasks = []
	with open('task-2.json') as data_file:
		data = json.load(data_file)

	for  i in data:
		tasks.append(Task(i))

	QueryTask = QueryTask(tasks)
	### Write your queries here
