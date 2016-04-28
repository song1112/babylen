## 資料表
- header_pic：主畫面的輪播
- user：使用者帳號資訊
- user_normal：使用者個人資料
- user_daycarecenter：中心資料
- user_bonne：保母資料

> models.py中有個PathAndRename()可設定上傳圖片的路徑

## API
- login：[HTTP POST][Select] 使用者登入

        POST VALUE:[account, password, Identify]
        RETURN:[action,message]
    
- register：[HTTP POST][Insert] 使用者註冊
		
		POST VALUE:[account,password,Identify_parents,Identify_bonne,Identify_daycarecenter,email]
		RETURN:[action,message]

- get\_user\_datalist：[HTTP POST][Select] 使用者個人資料

		POST VALUE:{"uid","Identify"}
		RETURN:{"action","normal":{"email","name","birthday","sex","tips","img","phone":,"address"},
        "bonne":{"seniority","baby_count_record","specialty","experience"},
        "daycare_center":{"setuptime","business_philosophy","diet_plan","environment_plan_imglist","learn_plan","about_us"}}}

- u\_user\_datalist：[HTTP POST][Update] 使用者更新個人資料

		POST VALUE:{"uid","Identify","email","name","birthday","sex","tips","img","phone","address"}
		RETURN:{"action"}
  
- u\_barcode\_relevance\_m2c：[HTTP POST][Update] 條碼掃瞄 托育中心掃保母：托育中心新增保母到該名下

 		POST VALUE:{"uid","Identify","mid"}
 		
- u\_barcode\_relevance\_b2m：[HTTP POST][Update] 條碼掃瞄 保母掃寶寶：保母新增寶寶到該名下

		POST VALUE:{"uid","Identify","bid"}    

- u\_barcode\_relevance\_b2p：[HTTP POST][Update] 條碼掃瞄 父母掃寶寶：父母新增寶寶到該名下

		POST VALUE:{"uid","Identify","bid"} 

- u\_barcode\_relevance\_b2c：[HTTP POST][Update] 條碼掃瞄 托育中心掃寶寶：托育中心新增寶寶到該名下

		POST VALUE:{"uid","Identify","bid"}
		
- get\_baby\_datalist：[HTTP POST][Select] 所有寶寶清單的資料列表

		POST VALUE:{"uid","Identify"}
		POST VALUE:{"uid","Identify","mid"}
		RETURN:{"action","typelist":[{"bonne","img","mid","datalist":{"datalist":[{"bid","name","img"}]}
		
- updata\_user\_pic：更新使用者大頭貼

		POST VALUE: uploaded_file, uid
		
> 需使用一般的post方法，不可post json

- get\_center\_bonne：取得中心旗下的所有保母

		POST VALUE: {uid}
		RETURN: {datalist:[boid,uid,name,seniority,specialty,experience,baby_count_record]}

- add\_baby\_auth：增加托育權限

		POST VALUE: {uid, Identify, count}
		RETURN: {action}

- bonne\_care\_chart：保母資料圖表

        POST VALUE:{uid}
        REATURN:{action,boy_count_1st,girl_count_1st,boy_count_2nd,girl_count_2nd,boy_count_3rd,girl_count_3rd,boy_count_4th,girl_count_4th}

> 越後面的計數代表越近的日期，假設今年是2016/01/01，4th代表的區間是2016/01/01-2016/06/30，3th代表2015/07/01-2015/12/31，依此類推
