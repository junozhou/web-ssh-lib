"""This is to test the Version 1 """
def list_scan (the_list,level=0,indent=False):
    for each_item in the_list:
        if isinstance(each_item,list):
            list_scan(each_item,level+1,indent)
        else:
            if indent:
                for count in range(level):
                    print("New")
            print(each_item)
            
                
                
            
