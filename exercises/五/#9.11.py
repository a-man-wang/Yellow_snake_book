"""

练习9-11：导入Admin类 以为完成练习9-8而做的工作为基础。将User类、Privileges类和Admin类存储在一个模块中，再创建一个文件，
在其中创建一个Admin实例并对其调用方法show_privileges()，以确认一切都能正确运行。

"""

from modle_name import Admin

somone = Admin("lao","wang")
somone.privileges.show_privileges()