# AWS-lamdba-Mutlithread-performance
Simple code to test performance and billing in AWS Lambda 

Test case: 
1) Create 6 threads and let them execute in parallel
2) Create single thread and let 6 task execute in sequence

Results:
1) When lambda function memory size is 128Mb, Both program takes approximately same CPU(little thread creation overhead) and billing time. Which indecates that at 128Mb lambda function has Single core assigned.
Acutal memory used by program:

44Mb in Single thread

64Mb in multithread

2) when lambda fucntion memory increased to 256 or more, execution time is reduced in multiple thread but billing remained same as billing depends on Execution_time X memory.  

Since acutal memory usage is less then allocated memory and max Number of core per Lambda in AWS is 2. Increasing memory beyond a point will increase the billing amount.
