# my-project
 題目：政治立場預測
 
 簡介：
     先利用爬蟲程式將PTT政黑版的文章爬下，匯入Elastic Search加以整理，從中挑選發文量大於20以上的發文者，人工判斷其立場並將之作為訓練資料，兩不同立場的訓練集各約有1000筆資料，測試集則各約200筆，訓練後得到模型，將之用以預測政治立場，模型種類依演算法種類分為三種，分別為Naïve Bayes、K Nearest Neighbor及Support Vector Machine。
     
功能介紹：
     輸入一段文字或文章並選擇欲使用之演算法，程式將依照不同演算法給出預測之結果。
     
使用工具及演算法：
     Python、Elastic Search、Beautiful soup、Naïve Bayes、K Nearest Neighbor、Support Vector Machine、Tkinter


     

