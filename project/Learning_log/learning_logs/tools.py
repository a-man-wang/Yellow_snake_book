"""工具函数"""


def check_topic_owner(request, topic):
    """检查是否是请求用户的主题"""
    return topic.owner != request.user
