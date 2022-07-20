import re
from flask import Flask, Response, request
from module import file_module
from db import db_connection
from flask_restx import Resource, Api, Namespace
from werkzeug.datastructures import FileStorage
from celery_worker import celery

####################################AI에 전달 - AI 함수로 전달하는 부분 수정필요#######################################

AI = Namespace(
    name="AI",
    description="AI CRUD를 작성하기 위해 사용하는 API.",
)

@AI.route('')
@AI.doc(responses={200: 'Success'})
@AI.doc(responses={404: 'Failed'})
class AIClass(Resource):

    def post(self):
       result = celeryTest.delay("abc")
       return result

@celery.task()
def celeryTest(a):
    print(a)
    return True

