# The sort function requires quite a bit of effort to work in a list within a list
# see when a list of strings like this is to be sorted:
# list_of_strings = ["a", "b", "c", "d"]
# list_of_strings.sort() will sort the list on its own

# HOWEVER, if you have a list of lists, like this:
# list_of_lists = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
# list_of_lists.sort() will not work,
# you need to specify which part of the list you want to sort by

#The lazy way to do this is to use a lambda function
"""
# list_of_lists.sort(key=lambda item: item[1]) 
"""
# lambda allows you to quickly write a function that will be used to sort the list
# the item: item[1] part is similar to (for item in items:)
# where item = one row of list_of_lists.
# The second part item[1] indicates what value is to be ordered, in this case the numbers  

#The normal way to do this is to write a function that will be used to sort the list
"""
list_of_dict = [{"name":"Steve", "num":2},{"name":"Bob", "num":7},{"name":"Alice", "num":5}]

 def sort_on(item):
    return item["num"]  

 list_of_dict.sort(reverse=True, key=sort_on)
"""
# In this case, the item in sort-on is the equivalent of a single row for list_of_lists (the dict inside the list)
# the return is the value of the "num" key in that row's dictionary
# So the sort on will give back the item[N]["num"] where N is the current row

# It takes more room and is generally inferior to lambda since the def is temporary
# but it is more readable and easier to understand for beginners



#BONUS example
"""
Using an External Dictionary for Priority

# External priority mapping
priority_order = {"urgent": 1, "normal": 2, "low": 3}

tasks = ["normal", "urgent", "low", "normal"]
tasks.sort(key=lambda task: priority_order[task])
# Result: ["urgent", "normal", "normal", "low"]
"""