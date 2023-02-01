# !/usr/bin/env python3
"""
    xpan userinfo
    include:
        user_info
        user_quota
"""
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import openapi_client
from openapi_client.api import userinfo_api
from openapi_client.model.quotaresponse import Quotaresponse
from openapi_client.model.uinforesponse import Uinforesponse
from pprint import pprint

def user_quota(access_token):
    """
    user_quota demo
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = userinfo_api.UserinfoApi(api_client)

        #access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ" # str | 
        checkexpire = 1 # int |  (optional)
        checkfree = 1 # int |  (optional)

        # example passing only required values which don't have defaults set
        # and optional values
        try:
            api_response = api_instance.apiquota(access_token, checkexpire=checkexpire, checkfree=checkfree)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling UserinfoApi->apiquota: %s\n" % e) 


def user_info(access_token):
    """
    user_info demo
    """
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient() as api_client:
        # Create an instance of the API class
        api_instance = userinfo_api.UserinfoApi(api_client)
        #access_token = "123.56c5d1f8eedf1f9404c547282c5dbcf4.YmmjpAlsjUFbPly3mJizVYqdfGDLsBaY5pyg3qL.a9IIIQ" # str | 

        # example passing only required values which don't have defaults set
        try:
            api_response = api_instance.xpannasuinfo(access_token)
            pprint(api_response)
        except openapi_client.ApiException as e:
            print("Exception when calling UserinfoApi->xpannasuinfo: %s\n" % e)


if __name__ == '__main__':
    """
    main
    """
    user_quota()
    user_info()
