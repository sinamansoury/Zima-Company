from django.shortcuts import render

# Create your views here.


def grouped_list(group_list, group_size=4):
    my_list = []
    for i in range(0, len(group_list), group_size):
        my_list.append(group_list[i:i+group_size])
    return my_list
