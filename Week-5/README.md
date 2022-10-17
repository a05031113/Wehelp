要求三：

使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

使用 SELECT 指令取得所有在 member 資料表中的會員資料。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req3_select_all.png?raw=true)

使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req3_select_all_orderby_time.png?raw=true)

使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req3_select_all_orderby_time_No.2~4.png?raw=true)

使用 SELECT 指令取得欄位 username 是 test 的會員資料。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req3_username=test.png?raw=true)

使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req3_username=teat&password=test.png?raw=true)

使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req3_update_name=test2_by_username=test.png?raw=true)

要求四：

取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req4_total_member_count.png?raw=true)

取得 member 資料表中，所有會員 follower_count 欄位的總和。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req4_total_follower_count.png?raw=true)

取得 member 資料表中，所有會員 follower_count 欄位的平均數。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req4_avg_of_follower_count.png?raw=true)

要求五：

使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req5_all_the_message&name.png?raw=true)

使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req5_all_message_by_username=test.png?raw=true)

使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。

![image](https://github.com/a05031113/Wehelp/blob/main/Week-5/image/req5_avg_of_like_count.png?raw=true)
