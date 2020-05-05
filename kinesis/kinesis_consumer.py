from boto import kinesis
import time

if __name__ == '__main__':
	kinesis = kinesis.connect_to_region("ap-southeast-1")
	print kinesis.describe_stream("payments")
	print kinesis.list_streams()

	shard_id = 'shardId-000000000000'
	shard_it = kinesis.get_shard_iterator("payments", shard_id, "LATEST")["ShardIterator"]
	while 1==1:
		out = kinesis.get_records(shard_it, limit=2)
		shard_it = out["NextShardIterator"]
		print out
		time.sleep(0.2)