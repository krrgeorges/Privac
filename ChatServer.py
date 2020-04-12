from flask import Flask,request
from datetime import datetime
from flask_restful import Resource, Api
import psycopg2
import time
import json
import random
from collections import OrderedDict

app = Flask(__name__)
api = Api(app)

conn = psycopg2.connect("dbname='privac' user='postgres' host='localhost' password='root'")
cursor = conn.cursor()

class UserInit(Resource):
	def get(self,uid):
		try:
			cursor.execute("select user_name from users where uid=%s;",(uid,));
			uresults = cursor.fetchall()
			return {"status":1,"user_name":uresults[0][0]}, 200, {'Content-Type': 'application/json; charset=utf-8'}
		except Exception as e:
			return {"status":0,"exc":str(e)}, 200, {'Content-Type': 'application/json; charset=utf-8'}



class GetOtherUsers(Resource):
	def get(self,uid):
		try:
			data = {}
			cursor.execute("select uid,user_name from users;");
			uresults = cursor.fetchall()
			for result in uresults:
				if result[0] != uid:
					data[result[0]] = result[1]
			return {"status":1,"data":data}, 200, {'Content-Type': 'application/json; charset=utf-8'}
		except Exception as e:
			return {"status":0,"exc":str(e)}, 200, {'Content-Type': 'application/json; charset=utf-8'}



class SendMessage(Resource):
	def get(self,uid_from):
		try:
			uid_to = request.args.get("uid_to")
			msg = request.args.get("msg")
			mid = request.args.get("mid")
			mtime = request.args.get("mtime")
			ftype = request.args.get("ftype")
			fname = request.args.get("fname")
			fcontent = request.args.get("fcontent")
			furl = request.args.get("furl")
			#encrypted message, directly add to db?
			read = 0;
			cursor.execute("INSERT INTO msgs(mid,uid_to,uid_from,msg_text,read_status,mtime,ftype,fname,fcontent,furl) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(mid,uid_to,uid_from,msg,read,mtime,ftype,fname,fcontent,furl))
			conn.commit()
			return {"status":1,"mid":mid}, 200, {'Content-Type': 'application/json; charset=utf-8'}
		except Exception as e:
			conn.rollback();
			return {"status":0,"exc":str(e)}, 200, {'Content-Type': 'application/json; charset=utf-8'}


class GetSpecificMessages(Resource):
	def get(self,uid1):
		try:
			uid2 = request.args.get("uid2");
			cursor.execute("SELECT mid,uid_from,uid_to,msg_text,read_status,mtime,ftype,fname,fcontent,furl FROM msgs where (uid_from = %s and uid_to = %s) or (uid_from = %s and uid_to = %s) order by mtime asc;",(uid1,uid2,uid2,uid1));
			results = cursor.fetchall()
			data = []
			for result in results:
				data.append({"uid_from":result[1],"uid_to":result[2],"msg":result[3],"read":result[4],"mtime":result[5],"mid":result[0],"ftype":result[6],"fname":result[7],"fcontent":result[8],"furl":result[9]})
			return {"status":1,"data":data}, 200, {'Content-Type': 'application/json; charset=utf-8'}
		except Exception as e:
			return {"status":0,"exc":str(e)}, 200, {'Content-Type': 'application/json; charset=utf-8'}


class GetAllMessages(Resource):
	def get(self,uid1):
		try:
			cursor.execute("SELECT mid,uid_from,uid_to,(SELECT user_name FROM users where uid=a.uid_to),msg_text,read_status,mtime,(SELECT user_name FROM users where uid=a.uid_from),ftype,fname,fcontent,furl FROM msgs a where (uid_from=%s) or (uid_to=%s) order by mtime asc;",(uid1,uid1));
			results = cursor.fetchall()
			data = []
			for result in results:
				uname = "";
				if result[1] == uid1:
					uname = result[3]
				else:
					uname = result[7]
				data.append({"uid_from":result[1],"uid_to":result[2],"msg":result[4],"read":result[5],"mtime":result[6],"mid":result[0],"uname":uname,"ftype":result[8],"fname":result[9],"fcontent":result[10],"furl":result[11]})
			return {"status":1,"data":data}, 200, {'Content-Type': 'application/json; charset=utf-8'}
		except Exception as e:
			return {"status":0,"exc":str(e)}, 200, {'Content-Type': 'application/json; charset=utf-8'}


class ReadMessage(Resource):
	def get(self,mid):
		try:
			cursor.execute("UPDATE msgs SET read_status=1 where mid=%s;",(mid,))
			conn.commit()
			return {"status":1}, 200, {'Content-Type': 'application/json; charset=utf-8'}
		except Exception as e:
			return {"status":0,"exc":str(e)}, 200, {'Content-Type': 'application/json; charset=utf-8'}


class ReadAllMessages(Resource):
	def get(self,uid1):
		try:
			uid2 = request.args.get("uid2");
			cursor.execute("UPDATE msgs SET read_status = 1 where uid_from=%s and uid_to=%s;",(uid2,uid1));
			conn.commit()
			return {"status":1}, 200, {'Content-Type': 'application/json; charset=utf-8'}
		except Exception as e:
			return {"status":0,"exc":str(e)}, 200, {'Content-Type': 'application/json; charset=utf-8'}







api.add_resource(UserInit,"/UserInit/<int:uid>")
api.add_resource(SendMessage,"/SendMessage/<int:uid_from>")
api.add_resource(GetSpecificMessages,"/GetSpecificMessages/<int:uid1>")
api.add_resource(GetAllMessages,"/GetAllMessages/<int:uid1>")
api.add_resource(ReadMessage,"/ReadMessage/<string:mid>")
api.add_resource(ReadAllMessages,"/ReadAllMessage/<int:uid1>")
api.add_resource(GetOtherUsers,"/GetOtherUsers/<int:uid>")

app.run(debug=False,host="0.0.0.0")

