"""
import pandas as pd #top level code
from datetime import timezone
import datetime

print("this is my module") #top level code


df=pd.DataFrame(
    [1, 2]
) #not top level code

print(__name__) #top level code
print(pd.__name__) #import ettiğimiz modulun name'i


print(timezone.__name__)
print(datetime.__name__)

"""

def my_function():
    print("Hello!")
    
def call_api(request):
    pass
    
if __name__=="__main__":
    my_function()
    request=""
    call_api(request)