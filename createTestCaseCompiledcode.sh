#!/bin/bash

problemList=`cat problems.txt`

for i in $problemList
do
	#echo $i
	pName=`echo "$i" | awk -F "/" '{ print $8}' `
	echo $pName
	mkdir $pName
	pUrl=`echo "$i" | awk -F "$pName" '{ print $1}' `
	echo $pUrl
	
	rReport=$pName"compiled_report.txt"
	#python3 DownlaodSubmissions.py $pUrl $pName
	echo =========================
	echo $pName
	echo "./${pName}/*.cpp"
	echo =========================
	
	 ./moss -l cc -c "$pname" ./${pName}/*.s #>> $rReport
	 
	
	

	
	
done

echo "Please Check Respective Problem Report folder for the reports.............."




