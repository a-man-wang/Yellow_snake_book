"""

练习8-10：发送消息 在你为完成练习8-9而编写的程序中，编写一个名为send_messages()的函数，将每条消息都打印出来并移到一个名为sent_messages的列
表中。调用函数send_messages()，再将两个列表都打印出来，确认正确地移动了消息。

"""

# def show_messages(lists):
#     for i in lists:
#         print(i)

def send_messages(lists):
    sent_messages = []
    while lists:
        i = lists.pop()
        sent_messages.append(i)
        print(i)
    print(lists)
    print(sent_messages)


listss = ["1","2","3"]
send_messages(listss)