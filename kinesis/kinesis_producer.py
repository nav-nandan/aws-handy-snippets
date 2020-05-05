from boto import kinesis
import testdata
import datetime
import json
import time

class Users(testdata.DictFactory):
	custid = testdata.RandomInteger(1, 10)
	amount = testdata.RandomInteger(1, 100)
	gateway = testdata.RandomSelection(['visa', 'paypal', 'master', 'stripe', 'wallet'])

if __name__ == '__main__':
	kinesis = kinesis.connect_to_region("ap-southeast-1")
	print kinesis.describe_stream("payments")
	print kinesis.list_streams()

	for user in Users().generate(10):
		print(user)
		print kinesis.put_record("payments", json.dumps(user), "partitionkey")
		time.sleep(1)