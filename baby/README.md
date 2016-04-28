## 資料表
- baby_barcodes：寶寶掃條碼紀錄，目前無使用
- baby_breastfeedings：寶寶日誌之餵奶
- baby_chats：寶寶聊天記錄，目前無使用
- baby_defecations：寶寶日誌之排便
- baby_dessertfruits：寶寶日誌之點心水果
- baby_diapers：寶寶日誌之尿布
- baby_grocerys：寶寶日誌之副食品
- baby_pictures：寶寶日誌圖片
- baby_relativess：寶寶親戚，目前無使用
- babys：寶寶資料
- care_record：保母托育圖表資料

## API
- cu_baby：[HTTP POST][Insert][Update] 寶寶資料   

        POST VALUE:{"uid","Identify","name","birthday","sex","tips","img","height","weight","nickname","bid"}  
        RETURN:{"action","message"}

- u\_baby\_relevance\_remove：[HTTP POST][Update] 寶寶資料連結取消：從列表中移出該寶寶 

        POST VALUE:{"uid","bid"}
        RETURN:{"action","message"}
        
- get\_baby\_record\_simple：[HTTP POST][Select] 餵奶，副食品，點心、水果，排便，尿布的頁面資料(簡)

        POST VALUE:{"uid","Identify","bid"}
        POST VALUE:{"uid","Identify","bid","indextime"}
        RETURN:{"action","selecttime","BreastFeeding":{"todaycount","finaltime"},"Grocery":{"todaycount","finaltime"},"DessertFruit":{"todaycount","finaltime"},"Defecation":{"todaycount","finaltime"},"Diaper":{"todaycount","finaltime"}}
        
- get\_baby\_record\_detail：[HTTP POST][Select] 餵奶，副食品，點心、水果，排便，尿布的頁面資料(詳)

        POST VALUE:{"uid","Identify","bid","recordtype","indextime"}
        RETURN:{"action":1,"selecttime":"2015/12/12","datalist":[{"rid","text","time":"12:33"},{"rid","text","time":"17:33"}]}
        
> recordtype: [0:餵奶,1:副食品,2:點心、水果,3:排便,4:尿布]

- cu\_baby\_record：[HTTP POST][Insert][Update] 餵奶，副食品，點心、水果，排便，尿布的資料

        POST VALUE:{"uid","Identify","bid","recordtype","newtext"}
        POST VALUE:{"uid","Identify","bid","recordtype","newtext","rid"}
        RETURN:{"action","message"}
        
- get\_baby\_picture\_imglist：[HTTP POST][Select] 相機畫面的已上傳圖片網

		POST VALUE:{"uid","Identify":0,"bid"}
		RETURN:{"action","selecttime","imglist":[]}
		
- c\_baby\_picture：[HTTP POST][Insert] 相機畫面的 +photo 按鈕選擇的圖片
        
        POST VALUE:{"uid","bpid","uploaded_file"}
        RETURN:{"action","message"}
        
> bpid代表baby id，uploaded_file代表圖片檔案，這邊請使用一般post檔案的方式，勿使用json格式
 
- u\_baby\_relevance\_b2m：[HTTP POST][Update] 托育中心更新多個寶寶到某保姆名下

        POST VALUE:{"uid":"1","Identify":2,"mid":"1","bid_text":"1,2,3"}
        RETURN:{"action","message"}
        
> bid_text=baby id字串，每個bid透過','去區分
 
- updata\_baby\_pic：上傳寶寶頭像

		POST VALUE: uploaded_file, bid
		RETURN:{"action","message"}
		
- get\_baby\_data：取得單個寶寶資料

		POST VALUE: {bid}
		RETURN:{"action","name","nickname","height","weight","birthday","tips","sex"}
        

