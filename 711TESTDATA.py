task_name_input = "Complete Final Project"
task_name_empty_input = ""  '''Empty Input to Check Validation'''

'''Test Validation by Adding A Task with a Valid Name'''
validate_entry(task_name_input) '''Should Show Success Message'''
validate_entry(task_name_empty_input)  '''Error Message for Empty Field'''
