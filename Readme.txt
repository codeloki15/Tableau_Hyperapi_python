*************************************************

This is an implementation note on .hyper file. 


***
When a csv file is created it work as a virtual for the Hyper API, 
It can be any file, may be xls or may be hyper API is directly connected with the DB. 
Now when we import any data to Tableau, the data can be ingested with live / extract service. 

HyperAPI brings the power of creating the extract(.hyper) file from csv directly. In Hyper API 
we are supposed to create the schema then a table with the contents and data type in the same order as will be passed 
by the CSV. Once that is done we will execute the command and this command will either , copy update, insert or delete the needed from 
the .hyper file, and after this the file is created in the given location. 
***
Implementation Steps

Step1. Creating a file checker.python to check the presence of data ingestion(.csv file).
Step2. Creating a python file for the data import and execution command.(Hyper API call).
Step3. Creating a batch file for python execution.
Step4. Linking all the files to capture data and implemet it as .hyper files.

The hyperd log file creates on its own with the log data for the python execution scripts and the hyper file updation details. We can also see the assigned PID






