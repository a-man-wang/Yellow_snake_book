"""

练习8-11：消息归档 修改你为完成练习8-10而编写的程序，在调用函数send_messages()时，向它传递消息列表的副本。调用函数send_messages()后，
将两个列表都打印出来，确认保留了原始列表中的消息。

"""
def send_messages(lists):
    sent_messages = []
    while lists:
        i = lists.pop()
        sent_messages.append(i)
        print(i)
    print(listss)
    print(sent_messages)


listss = ["1","2","3"]
send_messages(listss[:])