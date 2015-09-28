import unittest
import json
from task import *
import pdb
class ProblemTests(unittest.TestCase):
	def setUp(self): 
		with open('test.json') as data_file:
			self.data = json.load(data_file)
		

	"""Given a specific date provide the current number of open and closed tasks. 
	The date is inclusive so if we ask for midnight Oct 12, a task opened or closed 
	on midnight would count"""
	def test_numOfOpenClosedTasksAtTime(self):
		Query = QueryTask([Task(self.data)])

		time = "2015-03-22T22:24:55Z" # The second before the task is created
		assert Query.numOfOpenClosedTasksAtTime(time) == (0 , 0)

		time = "2015-03-22T22:24:56Z" # The second the task is created	
		assert Query.numOfOpenClosedTasksAtTime(time) == (1 , 0)	

		time = "2015-03-22T22:24:57Z" # The second after the task is created 
		assert Query.numOfOpenClosedTasksAtTime(time) == (1, 0)	

		time =   "2015-04-22T22:24:55Z" # The second before the task is closed	
		assert Query.numOfOpenClosedTasksAtTime(time) == (1, 0)

		time =   "2015-04-22T22:24:56Z" # The second  the task is closed
		assert Query.numOfOpenClosedTasksAtTime(time) == (0, 1)

		time =   "2015-04-22T22:24:57Z" # The second after the task is closed
		assert Query.numOfOpenClosedTasksAtTime(time) == (0 , 1)	

		# Test if the the JSON Data has no close date
		noCloseDate = dict(self.data)
		noCloseDate['closeDate'] = None
		Query = QueryTask([Task(noCloseDate)])
		time = "2015-03-22T22:24:57Z" # The second after the task is created 		
		assert Query.numOfOpenClosedTasksAtTime(time)  ==  (1, 0)
		
		

	"""Given a specific start and end date, how many tasks were opened and 
	how many were closed in that range. The start date is inclusive, the end 
	date is exclusive."""
	def test_numBetweenDates(self): 
		Query = QueryTask([Task(self.data)])

		# Test just outside the start and end time of the tsk
		startTime = "2015-03-22T22:24:55Z" # The second before the task is created	
		endTime =   "2015-04-22T22:24:57Z" # The second after the task is closed 
		assert Query.numBetweenDates(startTime, endTime) == (1, 1)

		# Test just within the start and end time of the task 
		startTime = "2015-03-22T22:24:57Z" # The second after the task is created 
		endTime =   "2015-04-22T22:24:55Z" # The second before the task is closed
		assert Query.numBetweenDates(startTime, endTime) == (0, 0)

		# Test the start and end time of the task 
		startTime = "2015-03-22T22:24:56Z" # The second the task is created
		endTime =   "2015-04-22T22:24:56Z" # The second the task is closed
		assert Query.numBetweenDates(startTime, endTime) == (1, 0)

		# Test if the the JSON Data has no close date
		noCloseDate = dict(self.data)
		noCloseDate['closeDate'] = None
		Query = QueryTask([Task(noCloseDate)])
		assert Query.numBetweenDates(startTime, endTime) == (1, 0)

	"""Given a particular instanceId, provide the name of the most recent task."""
	def test_mostRecentTaskNameforInstanceId(self):
		moreRecent = dict(self.data)
		moreRecent['createDate'] = "2015-03-22T22:24:57Z"
		moreRecent['name'] = "More Recent Task"
		Query = QueryTask([Task(self.data), Task(moreRecent)])
		assert Query.mostRecentTaskNameforInstanceId(680) == moreRecent['name']

	"""Given a particular instanceId, provide the count of tasks."""
	def test_countforInstanceId(self):
		Query = QueryTask([Task(self.data), Task(self.data)])
		assert Query.countforInstanceId(0)   == 0
		assert Query.countforInstanceId(680) == 2

	""" Given a particular assignee, provide the count of open and closed tasks for that assignee."""
	def test_openAndClosedTaskforAssignee(self):
		Query = QueryTask([Task(self.data), Task(self.data)])
		assert Query.openAndClosedTaskforAssignee("Ted") == (0, 0)
		assert Query.openAndClosedTaskforAssignee("BP3") == (0, 2)		
		


if __name__ == '__main__':
	tasks = []
	with open('test.json') as data_file:
		data = json.load(data_file)

	unittest.main()