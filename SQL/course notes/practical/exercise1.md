# Questions

1.Try and enter the following row:  `11111, Frank, Murphy, 4568777, Fmurphy@ucd.ie, REL20, Relational databases, 10, 300` What problem occurs and why? 
- **Answer:** Error occurs because studentid 11111 already exists, but primary key must be unique.



2.Try and enter the following row:  `33333, Frank, Murphy, 4568777, Fmurphy@ucd.ie, REL20, Relational databases, 10, 300 `What is the difference with respect to the previous example? 
- **Answer:** No error, it's because studentid 33333 is new and unique. 


3.Is it possible to have two different courses associated with the same student? 
- **Answer:** Yes,but each row should has a unique primary key`studentid`


4.What do you think is the purpose of the default value? 
- **Answer:** If no value is provided, the default value will automaticlly fill a column, so nulls can be avoided.

5.What information do you consider to be repeated unnecessarily in the table and why?For example how many times are we given the cost and duration of the 
“Relational Databases” course?  
- **Answer:** `Course cost` and `duration`. They are repeated for each students taking the same course.


6.How many pieces of information in the studentscourses table would you have to change if the “Relational Databases” course changed duration?   
- **Answer:** Change `duration` in every row that has a student who chose this course.

7.What would happen if you deleted the row for student 23000 (Aoife Byrne) from the database? What information might you want to save which would be deleted? 
- **Answer:** Aoife Byrne's personal informations and her enrollment data will be deleted. Any course information stored only in that row would be deleted too. To avoid that situation, course information should be stored separately in a courses table.



