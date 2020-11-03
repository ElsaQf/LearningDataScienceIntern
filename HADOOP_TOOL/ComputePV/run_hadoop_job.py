#!/usr/bin python

import os


def func_run():
	dir_delete = "/home/work/hadoop-client-tianqi-ubs-feed/hadoop/bin/hadoop fs -rmr /user/ubs/ubs-feed/jiajinkang/qufang/output_compute22"
	job_cmd = '''/home/work/hadoop-client-tianqi-ubs-feed/hadoop/bin/hadoop streaming \
	-libjars /home/work/upi-2/lib/upi-mr.jar \
	-jobconf abaci.split.optimize.enable=false \
	-jobconf mapred.map.tasks=200 \
	-jobconf mapred.reduce.tasks=1 \
	-jobconf mapred.job.priority=VERY_HIGH \
    -jobconf mapred.job.name=jiajinkang_mapreduce_test_20201102 \
	-jobconf udw.upi.input="default.udwmart_ps_onelog_day#filter={event_day='20201028' AND event_hour='00' AND event_minute='00'}#inputcols=*" \
	-jobconf udw.mapred.select.file.num=10 \
	-input "anything" \
	-output "/user/ubs/ubs-feed/jiajinkang/qufang/output_compute22" \
	-inputformat  com.baidu.udw.mapred.MultiTableInputFormat \
	-outputformat org.apache.hadoop.mapred.TextOutputFormat \
	-mapper 'python mapper.py' \
	-reducer 'python reducer.py' \
	-file 'mapper.py' \
	-file 'reducer.py' \
	-cacheArchive /user/ubs/ubs-feed/jiajinkang/qufang/python2.7.tar.gz
	'''
	os.system(dir_delete)
	os.system(job_cmd)
	return 0

if __name__ == '__main__':
	func_run()