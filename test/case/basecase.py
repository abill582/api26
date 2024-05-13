import unittest,requests,json,sys,ast
from lib.case_log import *
from lib.read_excel import *
from config.config import *


class BaseCase(unittest.TestCase):
    readexcel=readexcel()
    @classmethod
    def setUpClass(cls):
        print(cls.__name__)
        if cls.__name__!='BaseCase':
            cls.data_list=readexcel.excel_to_list(data_file,cls.__name__)
            print(cls.__name__)
    def get_case_data(self,case_name):
        return readexcel.get_test_data(self.data_list,case_name)

    def send_request(self,case_name):
        case_data=self.get_case_data(case_name)
        url=case_data.get('url')
        method=case_data.get('method')
        headers=case_data.get('headers')
        args = case_data.get('args')
        data_type = case_data.get('data')
        expect_res = case_data.get('expect_res')
        print(case_name,url,method,headers,args,data_type,expect_res)
        if method.upper()=='GET':
            logging.info("post json data")
            response=requests.get(url,headers=headers,params=args)
            print(response.text)

        elif data_type.upper()=='JSON':
            logging.info("post json data")
            res=requests.post(url=url,json=json.loads(args))
            log_case_info(case_name,url,args,expect_res,requests.json())
            self.assertIn(expect_res,res.text)
        elif data_type=='FORM':
            logging.info("post form data")
            response=requests.post(url,headers=headers,data=args)
            log_case_info(case_name, url, args, expect_res, requests.json())
            self.assertIn(expect_res, response.text)
        else:
            print("""暂不支持该数据类型""")


if __name__ == '__main__':
    unittest.main()
