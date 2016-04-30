## 資料表
- notification_apns
- notification_gcm


## API
- cu\_notification\_id：[HTTP POST][Update] 推播裝置資料新增修改

		POST VALUE:{"provider":1,"useragent","deviceid","user_id"}
		{"provider":0,""token"","user_id", "token"}
		RETURN: {"action"}
		
- get_notification_datalist：[HTTP POST][Select] 推播裝置資料查看

		POST VALUE:{"provider":0}
		
