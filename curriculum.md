# EE 深造課程總綱（26 週 / 約 180 天）

目標：半年後具備投遞並通過以下職缺面試的專業能力——
- Apple（龍潭）Camera Hardware EE Design and Test Engineer
- Apple（龍潭）Camera Hardware Design and Test Engineer（camera EE system integration / FA）
- Google（板橋）Senior Specialized Hardware Engineer, AR Glasses

學員背景：5 年 EE（NB 主機板 + 鏡頭模組），SI/PI 有量測經驗但理論與模擬較弱，無 Python 經驗（Python 依學員要求排在最後）。

## 每週節奏
- 週一～週四、週六：新觀念課（零基礎巨細靡遺教學）
- 週五：實作日（動手實驗 / 儀器操作 / 案例演練指引）——排平日是因為學員只有在公司才有儀器可操作
- 週日：週複習 + 自我測驗（20 題，附詳解）
（2026-07-26 起生效；Day 2〈2026-07-25 週六〉為舊制實作日，其實驗項目可於下週平日在公司補做）

## Phase 1（週 1–6）訊號完整性 SI 基礎
- 週 1：訊號的本質——上升時間與頻寬、傳播速度、何時要當傳輸線、集總 vs 分布、特性阻抗直覺
- 週 2：傳輸線理論——Z0 推導、微帶線/帶狀線、反射係數、端接策略（串聯/並聯/戴維寧）
- 週 3：反射實戰——TDR 原理與判讀、via stub、分支 (stub) 效應、connector 不連續
- 週 4：串擾——近端/遠端串擾機制、防護間距、guard trace、差動訊號原理與優勢
- 週 5：損耗與眼圖——導體損/介質損、skin effect、眼圖判讀、jitter 分類（RJ/DJ/ISI）
- 週 6：SI 量測週——高速探棒原理與負載效應、示波器頻寬選擇、S 參數入門、週總複習

## Phase 2（週 7–10）電源完整性 PI + EMI/EMC
- 週 7：PDN 概念——為什麼電源會塌、target impedance、電源樹分析（以 NB 多電源域為例）
- 週 8：去耦電容策略——電容的寄生 ESL/ESR、反諧振、擺放位置、平面電容
- 週 9：EMI 機制——共模 vs 差模、迴路面積、傳導/輻射耦合路徑、接地策略
- 週 10：ESD 與防護——ESD 模型（HBM/CDM/IEC 61000-4-2）、TVS 選型、layout 對策、週總複習

## Phase 3（週 11–16）Camera 領域深化（差異化武器）
- 週 11：影像感測器物理 I——光電效應、光電二極體、pinned photodiode、QE、full well capacity
- 週 12：影像感測器物理 II——雜訊全家福（dark current、read noise、shot noise、FPN、PLS）、conversion gain、photon transfer curve
- 週 13：MIPI D-PHY 電氣層——LP/HS 模式、阻抗與眼圖規範、C-PHY 比較、flex 走線挑戰
- 週 14：MIPI CSI-2 協定層——packet 結構、lane 分配、頻寬計算、常見 bring-up 失敗模式
- 週 15：鏡頭模組工程——VCM/OIS 驅動與 EMI、EEPROM 校正資料、模組 flex 設計、actuator 雜訊耦合
- 週 16：ISP pipeline 概觀——3A（AE/AWB/AF）、demosaic、降噪、tone mapping、camera 影像品質指標（SNR10、MTF）、週總複習

## Phase 4（週 17–19）FA 方法論 + 類比基本功
- 週 17：系統性 root-cause 流程——failure analysis 方法論、5-why/魚骨圖在硬體的用法、lock-in thermography / X-ray / CT 概念
- 週 18：類比基本功——運放非理想性（offset/bias/GBW/slew rate）、雜訊分析基礎、ADC/DAC 規格判讀
- 週 19：電源基本功——buck converter 工作原理與波形手繪（面試必考）、LDO vs DC-DC、power sequence 設計

## Phase 5（週 20–22）Python 量測自動化（依學員要求置後）
- 週 20：Python 零基礎入門——語法、資料結構、檔案處理（以量測資料為例）
- 週 21：PyVISA 儀器控制——SCPI 指令、控制示波器/電源供應器、自動掃參數
- 週 22：資料分析與報告——pandas 整理量測資料、matplotlib 畫圖、自動產報告

## Phase 6（週 23–26）面試衝刺
- 週 23：STAR 故事工作坊——把 5 年經歷整理成 6–8 個英文故事
- 週 24：白板手繪演練——buck 波形、MIPI 眼圖、PDN 阻抗曲線、運放電路
- 週 25：英文 mock interview 題庫演練（技術深挖題 + behavioral）
- 週 26：總複習 + 弱點補強 + 談薪準備

## 貫穿全程
- 英文：每日通勤 30 分（The Amp Hour / Moore's Lobby 跟讀），每課附「面試怎麼考」英文題
- Anki：每課附當日卡片，睡前 10 分複習
- 履歷投遞：第 12 週左右履歷就緒即投（面試流程 2–3 個月，邊面邊補強）
- 參考書《Perfect Timing II》（Cypress Semiconductor, 2002—Design Guide for Clock Generation and Distribution）：全文已拆章存於 reference/chapters/ch01~ch16（不入 git）。出課時若當日主題與下表章節相關，agent 必須先讀對應章節檔，將書中的實例、數據、圖表觀念帶入課程（引用時標註「Perfect Timing II Ch.X」）：
  - 週1（訊號本質/傳輸線判斷）→ Ch2 Clock Buffer Basics、Ch3 Timing Budget
  - 週2（Z0/端接策略）→ Ch7 Clock Termination（串聯/並聯/戴維寧實測波形）、Ch6 PCB Layout
  - 週3（反射實戰/TDR）→ Ch6 PCB Layout（via、return path）、Ch7
  - 週4（串擾/差動）→ Ch6（crosstalk、guard trace）、Ch14 Skew Control（trace matching）
  - 週5（損耗/眼圖/jitter）→ Ch4 Clock Jitter（RJ/DJ、cycle-to-cycle/period/long-term、高斯統計）、Ch13 Cascading PLLs（jitter 累積、phase noise）
  - 週6（SI 量測）→ Ch11 Probing High-Speed Clocks、Ch16 Motherboard Clock Validation（NB 主機板直接對口）、Ch10 IBIS/SPICE
  - 週7–8（PDN/去耦）→ Ch5 Power Supply Filtering、Ch8 Bypass Capacitors（ESL/ESR、擺放）
  - 週9（EMI）→ Ch9 EMI（spread spectrum、down/center spread、諧波）
  - 週19（電源/sequence）→ Ch5、Ch12 Clock Generators
  - 面試衝刺期 → Ch3 Timing Budget（TTB）、Ch16 當 case study 素材

## 課程產出規則（給每日出課 agent）
1. 全程繁體中文，絕不可出現簡體字；技術名詞可保留英文
2. 零基礎巨細靡遺：每個觀念先講直覺/比喻，再講原理，再數學，再實務
3. 固定章節：今日目標 → 前情提要 → 觀念講解（含 SVG 圖解）→ 數學推導 → 實務案例（連結 NB 主機板/鏡頭模組場景）→ 動手練習與詳解（details 收合）→ 面試怎麼考（英文題+參考答案）→ 今日 Anki 卡片 → 明日預告
4. 絕不捏造規格數據；不確定的數字標註「約」或「量級」
5. 週五實作日與週日複習日格式可調整（實驗指引 / 20 題測驗）；實作日必排平日，因學員僅平日在公司有儀器可用
6. 出課前查「貫穿全程」的《Perfect Timing II》章節對照表：當日主題有對應章節時，先讀 reference/chapters/ 下的章節檔再寫課，把書中實例/數據/量測波形觀念織入（標註「Perfect Timing II Ch.X」）；引用忠於原文，不可捏造書中沒有的數據；書是 2002 年出版，數據過時處（如頻率量級、製程）要註明「以現代標準需上修」
