import os
from pathlib import Path
import re
from datetime import datetime
import filecmp



def parse_date_time(input_string):
    date_formats = [
        r'(\d{2})[.: ](\d{2})[.: ](\d{4})[.: ](\d{2})h:(\d{2})m:(\d{2})s(.*)',
        r'(\d{2})[.: ](\d{2})[.: ](\d{4})[.: ](\d{2}):(\d{2}):(\d{2})(.*)',
        r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})\](.*)',
        r'(\d{4})[.: ](\d{2})[.: ](\d{2})[.: ](\d{2}):(\d{2}):(\d{2})(.*)',
        r'dt=(\d{4})-(\d{2})-(\d{2})_(\d{2}):(\d{2}):(\d{2})(.*)',
    ]
    for i, date_format in enumerate(date_formats):
        match = re.search(date_format, input_string)
        if match:
            groups = list(match.groups())
            if int(groups[0]) >= 30:
                tmp = groups[0]
                groups[0] = groups[2]
                groups[2] = tmp
            date_time_str = ':'.join(groups[:3]) + ' ' + ':'.join(groups[3:6])
            other_content_index = match.start(7) if groups[6] else None
            return datetime.strptime(date_time_str, '%d:%m:%Y %H:%M:%S'), other_content_index, i

    return None, None, None

errorSigns = ['error', 'Error', 'ERROR', 'ERR', 'err', 'Err']
warningSigns = ['warning', 'Warning', 'WARNING', 'WARN', 'warn', 'Warn']

msgEqualStr = "msg="

directory_path = input()
"""
D:/Desktop/trenutniProgrami/testingPSIML/loggingHell/public-log/set/1
3
98
3
for, a, to, data, updated
31594
"""


error_logtxt_counter = 0
logtxt_counter = 0
entries_counter = 0
fileCnt = 0
most_rep_words = ""
dictWords = dict()
warning_times = []
for root, dirs, files in os.walk(directory_path):
    for filename in files:
        if filename.endswith(".logtxt"):
            logtxt_counter += 1
            filepath = os.path.join(root, filename)
            with open(filepath) as file_logtxt:
                hasError = False
                logCnt = 0
                for line in file_logtxt:
                    line = line.strip()
                    if line:
                        time, startIndex, typeFormat =  parse_date_time(line)
                        lineSplited = line[startIndex:].replace(';', '').replace('.', '').replace(',', '').split()
                        for err in errorSigns:
                            if (not hasError) and (err in lineSplited[0] or (typeFormat == 3 and 'err' in lineSplited[1])):
                                hasError = True
                                break
                        isWarning = False
                        for wrn in warningSigns:
                            if wrn in lineSplited[0]:
                                isWarning = True
                                break
                        if typeFormat == 3 and 'warn' in lineSplited[1]:
                            isWarning = True
                        if isWarning:
                            warning_times.append(time)
                        
                        comment = []
                        if typeFormat == 0:
                            comment = lineSplited[3:]
                        elif typeFormat == 1:
                            comment = lineSplited[1:]
                            comment[0] = comment[0][4:]
                        elif typeFormat == 2:
                            comment = lineSplited[3:]
                        elif typeFormat == 3:
                            comment = lineSplited[2:]
                        elif typeFormat == 4:
                            comment = lineSplited[2:]
                            comment[0] = comment[0][4:]

                        for word in comment:
                            if not word in dictWords.keys():
                                dictWords[word] = (0, fileCnt, logCnt)
                            tupleVal = dictWords[word]
                            reps = tupleVal[0]
                            lastFileCnt = tupleVal[1]
                            lastLogCnt = tupleVal[2]
                            
                            if fileCnt != lastFileCnt or logCnt != lastLogCnt:
                                reps += 1
                            
                            dictWords[word] = (reps, fileCnt, logCnt)
                        
                        entries_counter += 1
                        logCnt += 1
                    
                
                if hasError:
                    error_logtxt_counter += 1
                

            fileCnt += 1
dictWords = sorted(dictWords.items(), key = lambda x: (-x[1][0], x[0]))

num_words_to_print = min(len(dictWords), 5)

if num_words_to_print > 1:
    for i in range(num_words_to_print - 1):
        most_rep_words += dictWords[i][0] + ", "
    most_rep_words += dictWords[num_words_to_print - 1][0]

warning_times.sort()
max_delta_time = 0
if len(warning_times) <= 5:
    max_datetime = warning_times[-1]
    min_datetime = warning_times[0]
    max_delta_time = (max_datetime - min_datetime).total_seconds()
else:
    n = len(warning_times)
    for i in range(n - 5):
        delta_time = (warning_times[i + 4] - warning_times[i]).total_seconds()
        max_delta_time = max(delta_time, max_delta_time)

max_delta_time = int(max_delta_time)

print(logtxt_counter)
print(entries_counter)
print(error_logtxt_counter)
print(most_rep_words)
print(max_delta_time)