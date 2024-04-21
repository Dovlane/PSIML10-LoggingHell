# PSIML10-LoggingHell
Below is a text for one of the three tasks that were part of application for universary 10th PSIML.

# Description
You are a software engineer thrown to work on a legacy application trying to figure out the state of the codebase, but you have one small problem - you have no access to the code. Luckiliy a good minded colleague provided you with some production logs and it's up to you to figure out how the app performs. After a quick glance at the logs you realize that there are multiple different services all using different log formats, this is going to get messy.
You are given a directory that contains arbitrarily deep subdirectory tree. Inside of the subdirectories scattered around you can find the log files (which end wiht ".logtxt" extension).
	- Log files can be formatted in up to 5 different ways, you need to go through the files in the public dataset and figure out the exact formats.

 Example of a directory tree containing .logtxt files.
	- {main_directory}/{dirX}/{dirY}/file1.logtxt <br />
	- {main_directory}/{dirX}/{dirY}/file2.logtxt <br />
	- {main_directory}/{dirX}/{dirY}/file3.logtxt <br />
	- {main_directory}/{dirZ}/file2.logtxt <br />
	- {main_directory}/file0018.logtxt <br />

These are the following tasks that you must do:
	A) Calculate the total number of ".logtxt" files
	B) Calculate the total number of log entries insede ".logtxt" files. (Each nonempty line inside a log is a log entry)
	C) Calculate the number of ".logtxt" files that have at least 1 error entry. (You need to deduce how exactly an error entry is described based on the given files)
	D) Calculate the 4 most common words that appear in the message body of each log entry at least once. (You need to deduce what exactly is the message body in different log formats based on the given files). Notes:
		- If multiple words occur with the same frequency, prioritize the one that appears first lexicographically
		- If the total number of words is fewer than five, include all available words.
		- Consider all words case-sensitive.
	E) Find the logest period of time (in seconds) with at most 5 warning log entries from the earliest log entry date to the latest log entry date. (You will need to how the dates and warning log entries are described in different log formats based on the given files.) Note: Consider warning entries from all files!

## Input format:
Input is the path to the directory where all log files are stored. All inputs are given in the given dataset.

## Output format:
Output answeres to subtastks in 5 seperate lines for each of the subtasks in order. If you don't have the answer to some answer leave a blank line. <br />
	A) integer, total number of ".logtxt" files <br />
	B) integer, total number of log entries <br />
	C) integer, total number of ".logtxt" files that have at least 1 error entry <br />
	D) string, comma seperated list of 5 most common lexicographically sorted words (as explained in subtask D) <br />
	E) integer, longest period of time (in seconds) with at most 5 warnings (as explained in subtask <br />
