import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import UserProfile
from .serializers import UserProfileModelSerializer, MyTokenObtainPairSerializer
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, AllowAny
import json
import re
import datetime
import random
from note.settings import APIKEY
from .models import Code
# 引入对接云片网模块
from utils.yunpian import YunPian
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


# class IsAuthenticated(BasePermission):
#     message = '查无此人'
#
#     def has_permission(self, request, view):
#         User_id = request.query_params.get("user_id")
#         user = UserProfile.objects.filter(id=int(User_id)).all()
#         if user:
#             return True
#         else:
#             print(self.message)
#             return False


class UserProfileModelViewSet(viewsets.ModelViewSet):

    # authentication_classes = []
    # permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileModelSerializer

    def get_queryset(self):
        User_id = self.request.query_params.get("user_id")
        userInfo = UserProfile.objects.filter(id=int(User_id))
        queryset = userInfo
        return queryset


class SendCodeView(APIView):
    """
    获取验证码
    """
    # 取消token认证限制
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        mobile = request.GET.get('mobile')
        if mobile:
            # 验证手机号
            mobile_pat = re.compile('^((13|14|15|16|17|18|19)\d{9})$')
            res = re.search(mobile_pat, mobile)
            if res:
                # 查看是否已注册
                had_register = UserProfile.objects.filter(mobile=mobile)
                # 已注册
                if had_register:
                    # 判断是否发送验证码
                    had_send = Code.objects.filter(mobile=mobile).last()
                    if had_send:
                        # 限制一分钟发一条验证码
                        if had_send.add_time.replace(tzinfo=None) > (
                                datetime.datetime.now() - datetime.timedelta(minutes=1)):
                            msg = '距离上次发送不足1分钟'
                            result = {"status": "403", "data": {'msg': msg}}
                            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                                content_type="application/json,charset=utf-8")
                        else:
                            # 发送验证码
                            code = Code()
                            code.mobile = mobile
                            # 生成6位随机验证码
                            c = random.randint(100000, 999999)
                            code.code = str(c)
                            # print(type(code.code), type(c), type(str(c)))
                            # 设定验证码20分钟有效期
                            code.end_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
                            code.save()
                            user = UserProfile.objects.get(mobile=mobile)
                            user.set_password(code.code)
                            user.save()
                            # 调用发送模块
                            # code = Code.objects.filter(mobile=mobile).last().code
                            # yunpian = YunPian(APIKEY)
                            # sms_status = yunpian.send_sms(code=code, mobile=mobile)
                            # msg = sms_status
                            # return HttpResponse(msg)
                            return HttpResponse()
                    else:
                        # 发送验证码
                        code = Code()
                        code.mobile = mobile
                        c = random.randint(100000, 999999)
                        code.code = str(c)
                        print(type(code.code), type(c), type(str(c)))
                        code.end_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
                        code.save()
                        user = UserProfile.objects.get(mobile=mobile)
                        user.set_password(code.code)
                        user.save()
                        # 调用发送模块
                        # code = Code.objects.filter(mobile=mobile).last().code
                        # yunpian = YunPian(APIKEY)
                        # sms_status = yunpian.send_sms(code=code, mobile=mobile)
                        # msg = sms_status
                        # # print(msg)
                        # return HttpResponse(msg)
                        return HttpResponse()
                else:
                    #发验证码
                    code = Code()
                    code.mobile = mobile
                    c = random.randint(100000, 999999)
                    code.code = str(c)
                    code.end_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
                    code.save()
                    # 调用发送模块
                    # code = Code.objects.filter(mobile=mobile).last().code
                    # yunpian = YunPian(APIKEY)
                    # sms_status = yunpian.send_sms(code=code, mobile=mobile)
                    # msg = sms_status
                    # # print(msg)
                    # return HttpResponse(msg)
                    # 注册用户
                    num = random.randint(10000, 9999999)
                    username = 'user' + str(num)
                    user = UserProfile.objects.create_user(password=code.code, mobile=mobile, username=username)
                    user.save
                    return HttpResponse()
            else:
                msg = '手机号错误'
                result = {"status": "403", "data": {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
        else:
            msg = '手机号为空'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")


# class RegisterView(APIView):
#     """
#     注册
#     """
#     # 取消token认证限制
#     authentication_classes = []
#     permission_classes = []
#     def get(self, request):
#         mobile = request.GET.get('mobile')
#         code = request.GET.get('code')
#         username = request.GET.get('username')
#         pwd1 = request.GET.get('pwd1')
#         pwd2 = request.GET.get('pwd2')
#         # 查看是否已注册
#         had_register = UserProfile.objects.filter(mobile=mobile)
#         if had_register:
#             msg = '该手机号已注册'
#             result = {"status": "402", "data": {'msg': msg}}
#             return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                 content_type="application/json,charset=utf-8")
#         else:
#             pass
#
#         if mobile:
#             pass
#         else:
#             msg = '手机号不能为空'
#             result = {"static": "404", "data": {'msg': msg}}
#             return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                 content_type="application/json, charset=utf-8")
#
#         if code:
#             pass
#         else:
#             msg = '验证码不能为空'
#             result = {"static": "404", "data": {'msg': msg}}
#             return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                 content_type="application/json, charset=utf-8")
#
#         if username:
#             pass
#         else:
#             msg = '用户名不能为空'
#             result = {"static": "404", "data": {'msg': msg}}
#             return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                 content_type="application/json, charset=utf-8")
#
#         if pwd1 == pwd2 and pwd1 or pwd2:
#             pass
#         else:
#             msg = '两个密码不一致'
#             result = {"static": "404", "data": {'msg': msg}}
#             return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                 content_type="application/json, charset=utf-8")
#
#         # 查找验证码表该号码最新的记录并对比验证码
#         codeCheck = Code.objects.filter(mobile=mobile).last()
#         if code == codeCheck.code:
#             end_time = codeCheck.end_time
#             end_time = end_time.replace(tzinfo=None)
#             if end_time > datetime.datetime.now():
#                 user = UserProfile.objects.create_user(username=username, password=pwd1, mobile=mobile)
#                 # user.username = username
#                 # user.password = pwd1
#                 # user.mobile = mobile
#                 user.save
#                 msg = '注册成功'
#                 Code.objects.filter(mobile=mobile, code=code).delete()
#                 result = {"static": "200", "data": {'msg': msg}}
#                 return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                     content_type="application/json, charset=utf-8")
#             else:
#                 msg = '验证码已过期'
#                 result = {"static": "404", "data": {'msg': msg}}
#                 return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                     content_type="application/json, charset=utf-8")
#         else:
#             msg = '验证码错误'
#             result = {"static": "404", "data": {'msg': msg}}
#             return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                 content_type="application/json, charset=utf-8")
#
#
# class LoginView(APIView):
#     """
#     登录
#     """
#     # 取消token认证限制
#     authentication_classes = []
#     permission_classes = []
#     def get(self, request):
#         mobile = request.GET.get('mobile')
#         code = request.GET.get('code')
#         had_register = UserProfile.objects.filter(mobile=mobile)
#         if mobile:
#             pass
#         else:
#             msg = '手机号不能为空'
#             result = {"static": "404", "data": {'msg': msg}}
#             return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                 content_type="application/json, charset=utf-8")
#         if code:
#             pass
#         else:
#             msg = '验证码不能为空'
#             result = {"static": "404", "data": {'msg': msg}}
#             return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                 content_type="application/json, charset=utf-8")
#
#         # 查找验证码表该号码最新的记录并对比验证码
#         codeCheck = Code.objects.filter(mobile=mobile).last()
#         if code == codeCheck.code:
#             end_time = codeCheck.end_time
#             end_time = end_time.replace(tzinfo=None)
#             if end_time > datetime.datetime.now():
#                 # 判断是否存在该用户
#                 if had_register:
#                     pass
#                 else:
#                     # 不存在，注册
#                     num = random.randint(10000, 99999)
#                     username = 'user' + str(num)
#                     print(username, type(mobile))
#                     user = UserProfile.objects.create_user(mobile=mobile, username=username)
#                     user.save
#
#                 msg = '登录成功'
#                 Code.objects.filter(mobile=mobile, code=code).delete()
#                 result = {"static": "200", "data": {'msg': msg}}
#                 return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                     content_type="application/json, charset=utf-8")
#             else:
#                 msg = '验证码已过期'
#                 result = {"static": "404", "data": {'msg': msg}}
#                 return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                     content_type="application/json, charset=utf-8")
#         else:
#             msg = '验证码错误'
#             result = {"static": "404", "data": {'msg': msg}}
#             return HttpResponse(json.dumps(result, ensure_ascii=False),
#                                 content_type="application/json, charset=utf-8")


User = get_user_model()


class MyCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                # Code.objects.filter(mobile=username, code=password).delete()
                # 提交登录后，修改密码，设置user 与 user1，避免return user错误
                user1 = UserProfile.objects.get(mobile=username)
                user1.set_password(str(uuid.uuid4())[0:16])
                user1.save()
                # print(user)
                return user
        except Exception as e:
            return None


