"""

练习9-12：多个模块 将User类存储在一个模块中，并将Privileges类和Admin类存储在另一个模块中。再创建一个文件，
在其中创建一个Admin实例并对其调用方法show_privileges()，以确认一切依然能够正确运行。

"""
from Privileges import Privileges,Admin
somone = Admin("lao","wang")
somone.privileges.show_privileges()
