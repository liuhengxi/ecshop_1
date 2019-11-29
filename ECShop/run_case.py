import unittest
import HTMLTestRunnerPlugins
import time
# 确定测试用列存放路径
case_pasth="./script"
# 将测试文件夹的测试用例添加到测试套件中
discover=unittest.defaultTestLoader.discover(case_pasth,pattern="test*.py")
# 执行测试用例生成测试报告
# 确定测试报告存放路径
report_path="./report"
# 确定测试报告名称
now=time.strftime("%Y_%m_%d %H-%M-%S")
report_file=report_path+"/"+now+"report.html"
with open(report_file,"wb") as fp:# 打开文件并写入
    runner=HTMLTestRunnerPlugins.HTMLTestRunner(
        title="ECShop项目web自动化测试报告",
        description="ECShop购买流程",
        stream=fp
    )
    runner.run(discover)
