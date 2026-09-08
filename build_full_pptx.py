# -*- coding: utf-8 -*-
import zipfile
import io
import html

# 43 slides data
slides_data = [
    # 1
    {
        "type": "cover",
        "title": "加護病房常用藥物與高風險不良反應",
        "subtitle": "從給藥到床邊監測：護理人員需要辨識的藥物警訊",
        "meta": "李芸瑄 藥師 • 2026.09.09 • 43頁 / 60分鐘完整培訓",
        "tag": "ICU MEDICATION SAFETY",
        "core": "課程主軸：為什麼給？給完看什麼？什麼情況要立即回報？"
    },
    # 2
    {
        "type": "content",
        "title": "Slide 2｜學習目標",
        "tag": "第一部分｜開場",
        "body": [
            "課程結束後，學員能夠：",
            "1. 依治療目的辨認ICU常用藥物類別與主要用途。",
            "2. 說出各類高風險藥物給藥後的床邊監測重點。",
            "3. 辨識凝血異常、QT延長及嚴重皮膚／過敏反應。",
            "4. 發現異常時，完成暫停評估、確認用藥、立即回報與初步處置。"
        ],
        "core": "落實：給藥前評估、給藥後監測、異常即處置"
    },
    # 3
    {
        "type": "content",
        "title": "Slide 3｜ICU藥物安全：護理人員的重要角色",
        "tag": "第一部分｜開場",
        "body": [
            "【五階段閉環流程】精準給藥 → 主動監測 → 察覺變化 → 回推藥物 → 即時處置（ISBAR 通報・停藥急救）",
            "【床邊 8 大常見潛在藥物警訊】",
            "• 1. 血壓突然劇降    • 2. 心率過快或過慢    • 3. 尿量持續下降    • 4. 意識或呼吸抑制",
            "• 5. QTc 間期延長    • 6. 血小板急速驟降    • 7. 不明原因出血    • 8. 新發紅疹或黏膜潰爛",
            "【核心防線】護理人員往往是全醫療團隊中「最早發現藥物不良反應的人」！"
        ],
        "core": "核心訊息：護理人員往往是最早發現藥物不良反應的人"
    },
    # 4
    {
        "type": "transition",
        "title": "血流動力學藥物",
        "tag": "PART 1",
        "quote": "「血壓只是數字，真正的治療目標是恢復器官灌流。」",
        "core": "PART 1｜血流動力學藥物"
    },
    # 5
    {
        "type": "content",
        "title": "Slide 5｜Vasopressor與Inotrope有什麼不同？",
        "tag": "PART 1｜血流動力學藥物",
        "body": [
            "【升壓劑（Vasopressor）】",
            "• 主要目標：增加血管張力、提升平均動脈壓、維持器官灌流。",
            "• 代表藥物：Norepinephrine、Epinephrine、Vasopressin、Dopamine。",
            "【強心劑（Inotrope）】",
            "• 主要目標：增加心肌收縮力、提升心輸出量、改善低心輸出造成的低灌流。",
            "• 代表藥物：Dobutamine、Milrinone。",
            "【核心提醒】升壓劑與強心劑可能同時使用，但治療目的不同！"
        ],
        "core": "核心提醒：升壓劑與強心劑可能同時使用，但治療目的不同"
    },
    # 6
    {
        "type": "content",
        "title": "Slide 6｜常用升壓劑比較",
        "tag": "PART 1｜血流動力學藥物",
        "body": [
            "• Norepinephrine：以α1作用為主｜敗血性休克第一線｜周邊缺血、心律不整。",
            "• Epinephrine：α及β作用｜心跳停止、過敏性休克、難治性休克｜心搏過速、心律不整、乳酸上升。",
            "• Vasopressin：V1受體作用｜作為Norepinephrine輔助藥物｜手指、腸道或皮膚缺血。",
            "• Dopamine：劑量相關受體作用｜特定心搏過慢合併低血壓情境｜心搏過速、心律不整。",
            "【三大提醒】① NE 為敗血休克第一線；② 開始給藥前必須先矯正血容積不足；③ 原則由中央靜脈導管給藥避免外滲壞死。"
        ],
        "core": "NE 為第一線；先補足血容積；中央靜脈給藥防壞死"
    },
    # 7
    {
        "type": "content",
        "title": "Slide 7｜使用升壓劑，不是只看血壓",
        "tag": "PART 1｜血流動力學藥物",
        "body": [
            "【7 大監測項目】平均動脈壓(MAP)、心率與心律、意識狀態、尿量、四肢溫度與膚色、微血管回填時間(CRT)、乳酸變化趨勢。",
            "【6 大立即回報警訊】",
            "• 四肢冰冷、蒼白或發紺    • 尿量持續下降    • 意識惡化",
            "• 乳酸持續上升            • 新發心律不整    • 血壓過高或過低",
            "【核心訊息】血壓升高，不代表器官灌流一定改善！"
        ],
        "core": "核心訊息：血壓升高，不代表器官灌流一定改善"
    },
    # 8
    {
        "type": "content",
        "title": "Slide 8｜周邊靜脈使用升壓劑與外滲處理",
        "tag": "PART 1｜血流動力學藥物",
        "body": [
            "【使用原則】中心靜脈尚未建立時，可由清楚觀察、血流良好之周邊靜脈短期開始，不應等待 CVC 延誤治療。",
            "【輸注部位監測】疼痛或灼熱感、腫脹、皮膚蒼白、局部冰冷、滴注不順、回血異常、周邊灌流變差。",
            "【疑似外滲 5 步驟 SOP】",
            "1. 立即停止輸注。    2. 暫時保留原管路。    3. 評估抽吸殘留藥物。",
            "4. 抬高患肢，局部熱敷（不可冰敷）。         5. 通知醫師（評估 Phentolamine 解毒）。"
        ],
        "core": "外滲處理：停輸注 → 留管路 → 抽殘藥 → 抬高熱敷 → 通報醫師"
    },
    # 9
    {
        "type": "content",
        "title": "Slide 9｜Dobutamine與Milrinone比較",
        "tag": "PART 1｜血流動力學藥物",
        "body": [
            "• Dobutamine：β1受體為主｜增心肌收縮力與心輸出量｜心搏過速/心律不整/降血壓｜非主要腎排｜起效快易調，受β-blocker減弱。",
            "• Milrinone：PDE-3抑制劑｜增收縮力並擴血管(Inodilator)｜血壓下降/心律不整｜腎不全可能蓄積｜半衰期長調整消退慢。",
            "【使用前 4 項確認】",
            "① 血容量是否適當？    ② 血壓是否足以耐受？",
            "③ 是否有持續低心輸出或低灌流？    ④ 心率、心律及腎功能為何？"
        ],
        "core": "Dobutamine 易滴定；Milrinone 降肺壓但腎衰竭易蓄積"
    },
    # 10
    {
        "type": "content",
        "title": "Slide 10｜ICU常用降壓／血管擴張劑比較",
        "tag": "PART 1｜血流動力學藥物",
        "body": [
            "• Nicardipine：可滴定的靜脈降壓首選｜副作用：血壓過低、反射性心搏過速｜監測：血壓、心率、意識與尿量。",
            "• Labetalol：α1及β受體阻斷｜副作用：心搏過慢、房室傳導阻滯、支氣管痙攣｜監測：心率、心電傳導與呼吸音。",
            "• Nitroglycerin：急性冠心症、肺水腫等特定情境｜副作用：血壓過低、頭痛、反射性心搏過速｜監測：血壓、胸痛、呼吸與頭痛。"
        ],
        "core": "Nicardipine 監測反射心搏過速；Labetalol 監測心率過慢與氣喘；NTG 監測劇烈頭痛與低血壓"
    },
    # 11
    {
        "type": "content",
        "title": "Slide 11｜安全降壓：給藥前後看什麼？",
        "tag": "PART 1｜血流動力學藥物",
        "body": [
            "【降壓目標依疾病個別設定】主動脈剝離、腦出血/中風、ACS、肺水腫、高血壓急症。",
            "【Labetalol 給藥前確認】心率（HR < 60 禁忌）、PR延長/AV block、氣喘病史、血壓及灌流。",
            "【Nitroglycerin 給藥前確認】是否使用 PDE-5 抑制劑（威而鋼）、是否可能為右心室梗塞、前負荷依賴狀態。",
            "【立即回報警訊】血壓明顯下降、心跳過慢、新發傳導異常、喘鳴或呼吸困難、意識或尿量惡化。"
        ],
        "core": "NTG 禁忌 PDE-5 與 RV 梗塞；Labetalol 查心率與氣喘病史"
    },
    # 12
    {
        "type": "transition",
        "title": "ACLS 與心律不整用藥",
        "tag": "PART 2",
        "quote": "「心跳太快、太慢或停止，用藥選擇取決於心律與血流動力學狀態。」",
        "core": "PART 2｜ACLS 與心律不整用藥"
    },
    # 13
    {
        "type": "content",
        "title": "Slide 13｜先判斷穩定度，再依心律選擇處置",
        "tag": "PART 2｜ACLS與心律不整用藥",
        "body": [
            "• 心搏過慢：Atropine。無效時考慮經皮心律調節(TCP)、Dopamine或Epinephrine持續輸注。",
            "• 規則窄QRS心搏過速：迷走神經刺激法、Adenosine。",
            "• 不穩定心搏過速：優先同步電復律！不應為了嘗試藥物而延誤電復律！",
            "【改良式Valsalva操作 6 步驟（僅適用穩定規則窄QRS）】",
            "1. 半坐臥姿勢 → 2. 吹針筒15秒 → 3. 改平躺 → 4. 雙腿抬高45度15秒 → 5. 回半坐臥觀察45秒 → 6. 全程監測ECG/血壓。"
        ],
        "core": "不穩定心搏過速優先同步電復律；不應為藥物延誤電復律"
    },
    # 14
    {
        "type": "content",
        "title": "Slide 14｜Atropine、Adenosine與Isoproterenol定位",
        "tag": "PART 2｜ACLS與心律不整用藥",
        "body": [
            "• Atropine：有症狀心搏過慢第一線｜無效時不應延誤心律調節或升壓藥物。",
            "• Adenosine：規則窄QRS心搏過速主力｜快速推注，會出現短暫房室傳導阻滯。",
            "• Isoproterenol：特定情境暫時增加心率｜並非常規ACLS心搏過慢第二線用藥！",
            "【Isoproterenol 風險】心搏過速、心律不整、心肌耗氧增加、胸痛、心肌缺血或血壓下降。"
        ],
        "core": "Atropine 無效不拖延起搏；Adenosine 快推；Isoproterenol 非常規二線"
    },
    # 15
    {
        "type": "content",
        "title": "Slide 15｜Adenosine：給藥方法與常見反應",
        "tag": "PART 2｜ACLS與心律不整用藥",
        "body": [
            "• 適用：規則窄QRS心搏過速；單型寬QRS鑑別情境。不適用：不規則/多型性寬QRS心搏過速。",
            "• 給藥方法：由靠近中心循環大靜脈快速推注(1-2秒) → 立即快速沖入 20mL 生理食鹽水 → 全程 ECG 記錄。",
            "• 常見反應：臉部潮紅、胸悶/壓迫感、呼吸不適、頭暈、短暫心搏過慢、短暫房室傳導阻滯或心搏停止。",
            "【重要提醒】數秒短暫心搏停止（Asystole）為預期電氣重置作用，但仍須確認心律及時恢復！"
        ],
        "core": "不規則寬 QRS 禁用；近心端快推沖食鹽水；短暫心搏停止為預期現象"
    },
    # 16
    {
        "type": "content",
        "title": "Slide 16｜Amiodarone與Lidocaine比較",
        "tag": "PART 2｜ACLS與心律不整用藥",
        "body": [
            "• Amiodarone：VT/VF及心房心律不整｜副作用：低血壓、心搏過慢、傳導阻滯、QT延長、靜脈炎｜長期甲狀腺/肺/肝毒性｜合併低鉀低鎂易致 TdP。",
            "• Lidocaine：VT/VF心室心律不整｜副作用：低血壓、心搏過慢、傳導異常與神經毒性｜QTc不是主要監測指標。",
            "【Lidocaine 7 大神經毒性警訊】嘴唇或舌頭麻木、耳鳴、頭暈、嗜睡、意識混亂、顫抖、抽搐癲癇！",
            "【清除率警惕】肝功能不全或低心輸出狀態顯著降低 Lidocaine 清除率。"
        ],
        "core": "Amiodarone 監測低血壓與 QT；Lidocaine 嚴密監測舌唇麻木與抽搐神經毒性"
    },
    # 17
    {
        "type": "transition",
        "title": "鎮靜、止痛與肌肉鬆弛",
        "tag": "PART 3",
        "quote": "「病人安靜了，但呼吸、循環與疼痛真的安全嗎？」",
        "core": "PART 3｜鎮靜、止痛與肌肉鬆弛"
    },
    # 18
    {
        "type": "content",
        "title": "Slide 18｜ICU常用鎮靜劑比較",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "• Midazolam：起效快、順行性失憶｜呼吸抑制、低血壓、延遲甦醒、蓄積、增加譫妄。",
            "• Lorazepam：鎮靜、抗焦慮、抗癲癇｜呼吸抑制、低血壓｜特殊風險：丙二醇毒性。",
            "• Propofol：起效及恢復快速、易滴定｜低血壓、心搏過慢｜特殊風險：PRIS 輸注症候群。",
            "• Dexmedetomidine：容易喚醒、保留呼吸驅動｜心搏過慢、低血壓｜突然停藥戒斷反應。",
            "【鎮靜 5 大原則】先止痛再鎮靜、設定目標 RASS、優先輕鎮靜、最低有效劑量、每日評估自主中斷喚醒。"
        ],
        "core": "先止痛再鎮靜、設定目標 RASS、優先輕鎮靜、每日評估喚醒"
    },
    # 19
    {
        "type": "content",
        "title": "Slide 19｜Benzodiazepine合併Opioid",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "【核心警示】Benzodiazepine 與鴉片類止痛藥併用，會增加呼吸抑制、血壓過低與過度鎮靜風險！",
            "【7 大監測】呼吸速率與型態、SpO2、EtCO2、意識與喚醒能力、RASS、血壓心率、最近追加與累積劑量。",
            "【6 大立即回報】呼吸速率明顯下降(<8-10次/分)、呼吸變淺、無法喚醒、血氧下降、二氧化碳滯留、血壓下降。"
        ],
        "core": "核心警示：BZD 併用鴉片類增加呼吸抑制、血壓過低與過度鎮靜風險"
    },
    # 20
    {
        "type": "content",
        "title": "Slide 20｜Lorazepam持續輸注：注意丙二醇蓄積",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "【4 大高風險情境】高劑量、長時間靜脈輸注(>48-72h)、腎功能不全、同時使用其他含丙二醇製劑。",
            "【7 大警訊】滲透壓間隙增加(Osmolar gap↑)、陰離子間隙增加(AG↑)、代謝性酸中毒、乳酸上升、急性腎損傷(AKI)、尿量下降、意識惡化。",
            "【提醒】劑量與時間是風險因子，不是絕對診斷門檻；可疑即查 Osmolar gap。"
        ],
        "core": "Lorazepam 滴注注意滲透壓間隙增加、代謝酸中毒與急性腎損傷"
    },
    # 21
    {
        "type": "content",
        "title": "Slide 21｜Propofol Infusion Syndrome (PRIS)",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "【風險情境】高劑量(>4-5 mg/kg/h)或長時間(>48h)輸注、嚴重重症、合用兒茶酚胺或類固醇。",
            "【9 大警訊】無法解釋的代謝性/乳酸酸中毒、肌酸激酶(CK)上升、橫紋肌溶解、高血鉀、心搏過慢、新發心律不整(Brugada樣)、急性心衰竭、循環崩潰、三酸甘油脂上升。",
            "【監測】酸鹼狀態、乳酸、CK、血鉀、TG、心電圖與循環狀態；可疑即刻停藥！"
        ],
        "core": "高劑量長天數，注意酸中毒、CK飆高、高血鉀、心動過緩；疑似立停"
    },
    # 22
    {
        "type": "content",
        "title": "Slide 22｜Dexmedetomidine：病人容易喚醒，但仍要監測",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "• 特色：較容易維持輕鎮靜、病人通常可喚醒配合、較能保留呼吸驅動；【但仍不能免除呼吸道監測！】",
            "• 重要副作用：心搏過慢、血壓下降、快速給藥短暫血壓升高、長期突然停藥戒斷反應(躁動/頻脈/高血壓)。",
            "• 立即回報：心率明顯下降(HR<50)、新發傳導阻滯、血壓下降合併灌流不良、無法解釋的意識/呼吸變化。"
        ],
        "core": "容易喚醒仍需呼吸道監測；防心搏過慢、低血壓與停藥反彈"
    },
    # 23
    {
        "type": "content",
        "title": "Slide 23｜Fentanyl與Morphine比較",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "• Fentanyl：起效快(1-2分)、組織胺釋放少對血壓穩定、無活性腎代謝物(腎不良首選)；快推注意胸壁僵硬。",
            "• Morphine：組織胺釋放造成低血壓、活性代謝物(M6G)於腎功能不全蓄積；注意延遲性鎮靜與呼吸抑制。",
            "• 共同監測：疼痛評分、呼吸速率、意識與鎮靜程度、血壓、腸蠕動便秘、噁心與嘔吐。"
        ],
        "core": "Fentanyl 起效快無腎蓄積；Morphine 釋組織胺降血壓且腎衰竭大蓄積"
    },
    # 24
    {
        "type": "content",
        "title": "Slide 24｜腎功能不全患者使用Morphine",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "【臨床情境】腎功能惡化 ＋ 逐漸嗜睡 ＋ 呼吸速率下降。",
            "【應考慮】Morphine 活性代謝物(M6G)蓄積、延遲甦醒、持續性呼吸抑制。",
            "【護理觀察】意識變化(瞳孔縮小)、呼吸速率與深度、血氧與 PaCO2、腎功能及尿量、累積劑量。",
            "【核心提醒】病人「叫不醒」不一定只是神經學惡化，也可能與藥物蓄積有關！"
        ],
        "core": "提醒：病人「叫不醒」不一定只是神經學惡化，也可能與藥物蓄積有關"
    },
    # 25
    {
        "type": "content",
        "title": "Slide 25｜Ketamine與Parecoxib",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "• Ketamine：止痛、鎮靜及解離性麻醉作用，【不是神經肌肉阻斷劑！】｜副作用：血壓及心率升高、唾液分泌增加、幻覺/惡夢/甦醒期躁動、噁心嘔吐。",
            "• Parecoxib：IV COX-2抑制劑｜副作用：急性腎損傷(AKI)、液體滯留、水腫、血壓升高、腸胃道出血及心血管血栓風險（CABG術後禁忌）。"
        ],
        "core": "Ketamine 具止痛解離非肌鬆劑但增心率唾液；Parecoxib 警惕 AKI 與血栓"
    },
    # 26
    {
        "type": "content",
        "title": "Slide 26｜Tramadol與血清素症候群",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "【高風險合併用藥】SSRI／SNRI、MAOI、Linezolid(Zyvox)、其他增加血清素藥物。",
            "【11 項臨床表現】躁動/意識改變、大汗、心搏過速、血壓升高、體溫過高、腹瀉、顫抖、肌肉僵硬、抽搐；",
            "【★ 最重要特徵】反射亢進（Hyperreflexia） 與 肌肉陣攣（Myoclonus）！",
            "【核心提醒】肌肉陣攣與反射亢進，是辨識血清素症候群的重要線索！"
        ],
        "core": "核心提醒：肌肉陣攣與反射亢進，是辨識血清素症候群的重要線索"
    },
    # 27
    {
        "type": "content",
        "title": "Slide 27｜神經肌肉阻斷劑比較",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "• Succinylcholine：去極化型｜起效60-90秒/持續5-10分｜起效最快短效｜致命高血鉀、心搏過慢、惡性高熱、眼內壓↑｜快速插管RSI。",
            "• Rocuronium：非去極化型｜起效1-2分/持續30-60分｜高劑量起效快、循環平穩、具逆轉劑Sugammadex｜肝功能不全阻斷延長｜插管與肌鬆。",
            "• Atracurium：非去極化型｜起效2-3分/持續20-35分｜主要經Hofmann分解不依賴肝腎｜組織胺釋放/低血壓/支氣管痙攣/Laudanosine｜肝腎衰竭首選。"
        ],
        "core": "Succinylcholine 防高血鉀；Rocuronium 有逆轉劑；Atracurium 不經肝腎"
    },
    # 28
    {
        "type": "content",
        "title": "Slide 28｜病人不動，不代表沒有疼痛",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "【使用肌鬆劑時】病人可能仍有意識！病人可能仍會感到疼痛！無法以動作判斷疼痛或鎮靜不足！",
            "【必備原則】應先確保充分止痛與鎮靜！依院內流程監測神經肌肉阻斷程度(TOF)！持續眼睛保護、翻身與壓傷預防！",
            "【核心訊息】Paralysis ≠ Sedation ≠ Analgesia（癱瘓 ≠ 鎮靜 ≠ 止痛）！"
        ],
        "core": "核心訊息：Paralysis ≠ Sedation ≠ Analgesia；先止痛鎮靜再給肌鬆"
    },
    # 29
    {
        "type": "content",
        "title": "Slide 29｜Succinylcholine與致命性高血鉀",
        "tag": "PART 3｜鎮靜、止痛與肌肉鬆弛",
        "body": [
            "【7 大高風險族群（受體上調禁用）】大面積燒傷急性期後、壓砸傷/多發創傷、脊髓損傷、運動神經元損傷、神經肌肉疾病、嚴重去神經支配、長期臥床肌肉失用。",
            "【心電圖與臨床表現】血鉀快速驟升、心搏過慢、QRS波變寬(Sine-wave)、心室心律不整、心搏停止猝死！",
            "【提醒】受體上調隨時間增加，危險期可達數週至數月，此類病人插管改用 Rocuronium！"
        ],
        "core": "燒燙傷、壓砸傷、脊髓損傷、長期臥床禁用 Succinylcholine，防致命高血鉀"
    },
    # 30
    {
        "type": "transition",
        "title": "抗凝血與血栓溶解藥物",
        "tag": "PART 4",
        "quote": "「看到明顯出血之前，血小板、血紅素與神經狀態可能已經提供警訊。」",
        "core": "PART 4｜抗凝血與血栓溶解藥物"
    },
    # 31
    {
        "type": "content",
        "title": "Slide 31｜Heparin、Enoxaparin與Urokinase比較",
        "tag": "PART 4｜抗凝血與血栓溶解藥物",
        "body": [
            "• Heparin：非分段肝素｜主要監測 aPTT 或 anti-Xa、血紅素、血小板｜重要風險：出血、HIT。有解毒劑 Protamine。",
            "• Enoxaparin：低分子量肝素(LMWH)｜主要監測血紅素、血小板、腎功能｜重要風險：腎功能不全時蓄積及出血（Anti-Xa非常規監測）。",
            "• Urokinase：血栓溶解劑｜主要監測血紅素、出血部位、神經狀態(GCS/瞳孔)｜重要風險：重大出血、顱內出血(ICH)。"
        ],
        "core": "Heparin 監控 aPTT/血小板防 HIT；Enoxaparin 腎衰竭易蓄積；Urokinase 嚴防顱內出血"
    },
    # 32
    {
        "type": "content",
        "title": "Slide 32｜HIT：血小板還在正常範圍也不能排除",
        "tag": "PART 4｜抗凝血與血栓溶解藥物",
        "body": [
            "【6 大辨識要點】血小板較基準值下降>50%、常於第5-10天發生、新發血栓或血栓惡化、注射處皮膚壞死、bolus後急性全身反應、排除感染DIC等原因。",
            "【4Ts 評估英文字義（MDCalc）】① Thrombocytopenia（血小板降幅>50%） ② Timing（第5-10天） ③ Thrombosis（新血栓/壞死） ④ oTher causes（排除其他原因）。",
            "【核心提醒】HIT是促進血栓形成的免疫反應，不是單純出血性血小板低下！",
            "【中高機率處置】立即回報、停所有Heparin來源、嚴禁輸血小板、換非肝素抗凝劑(如Argatroban)並送檢。"
        ],
        "core": "核心提醒：HIT 是促進血栓形成的免疫反應，不是單純出血性血小板低下"
    },
    # 33
    {
        "type": "content",
        "title": "Slide 33｜血栓溶解治療：重大出血警訊",
        "tag": "PART 4｜抗凝血與血栓溶解藥物",
        "body": [
            "【6 項護理觀察】穿刺處持續出血、牙齦/鼻腔出血、血尿、黑便/吐血、血紅素無故下降、血壓降或心跳快。",
            "【6 大顱內出血(ICH)警訊】新發劇烈頭痛、意識改變、瞳孔變化(不等大)、單側肢體無力、新發語言障礙、抽搐癲癇！",
            "【提醒】溶栓期間避免不必要動脈穿刺、肌肉注射及侵入性處置；疑似腦出血立停送 CT！"
        ],
        "core": "溶栓避免侵入性處置；劇烈頭痛、瞳孔變化、意識改變立即停藥送 CT"
    },
    # 34
    {
        "type": "transition",
        "title": "看到異常，要想到可能是藥物",
        "tag": "PART 5",
        "quote": "「看到異常，要想到可能是藥物！前半段從藥物出發；接下來從病人的異常，反推可能相關藥物。」",
        "core": "PART 5｜看到異常，要想到可能是藥物"
    },
    # 35
    {
        "type": "content",
        "title": "Slide 35｜抗生素常見高風險不良反應",
        "tag": "PART 5｜看到異常，要想到可能是藥物",
        "body": [
            "• Linezolid：血小板下降、骨髓抑制、血清素症候群｜觀察出血、瘀青、陣攣、血球計數。",
            "• Vancomycin：急性腎損傷(AKI)、輸注反應(紅人症)｜觀察尿量、肌酸酐、潮紅搔癢。",
            "• Cefoperazone：PT／INR 延長、出血｜觀察注射處滲血、血尿、黑便。",
            "• Macrolide／Fluoroquinolone：QT延長、心室心律不整(TdP)｜觀察心悸、暈厥、ECG與電解質。",
            "• β-lactam (如 Cefepime)：中樞神經毒性(腎不全高危)｜觀察意識改變、抽動、顫抖、抽搐。",
            "【核心訊息】抗生素副作用不只紅疹腹瀉，凝血、心電圖、神經或腎功能異常都要警戒！"
        ],
        "core": "核心訊息：抗生素副作用不只紅疹腹瀉，也可能表現為凝血、心電圖、神經或腎功能異常"
    },
    # 36
    {
        "type": "content",
        "title": "Slide 36｜哪些藥物會造成凝血異常？",
        "tag": "PART 5｜看到異常，要想到可能是藥物",
        "body": [
            "• 血小板下降：Heparin(HIT)、Linezolid(骨髓抑制)、Vancomycin(免疫性低下)、部分β-lactam(如 Piperacillin、Ceftriaxone)。",
            "• PT／INR 延長：Cefoperazone、Warfarin、維生素K不足(NPO)、嚴重肝功能異常。",
            "• 直接增加出血：Heparin、Enoxaparin、Urokinase、多種抗血小板/抗凝血藥物併用。",
            "【Cefoperazone 高風險情境】營養不良、維生素K攝取不足、膽道或肝病、長時間抗生素、重症狀態、併用抗凝劑。",
            "【處置】Vitamin K 是否補充依檢驗、出血風險與院內流程決定。"
        ],
        "core": "PLT 降查 Heparin/Linezolid；PT 延長查 Cefoperazone/Vit K；多藥併用增出血"
    },
    # 37
    {
        "type": "content",
        "title": "Slide 37｜哪些藥物可能延長QT？（直接延長 vs 低鉀間接促發）",
        "tag": "PART 5｜看到異常，要想到可能是藥物",
        "body": [
            "【明確延長 QT／TdP 風險藥物】",
            "• 抗心律不整：Amiodarone。    • 止吐與腸胃：Ondansetron、Droperidol、Metoclopramide。",
            "• 抗感染：Macrolides(Azithro)、Fluoroquinolones(Levo/Moxi)、Azoles抗黴菌(Fluconazole)。",
            "• 精神科與鎮靜：Haloperidol、Ziprasidone、Quetiapine。",
            "【間接風險（低鉀/低鎂催化）】Loop利尿劑、Thiazide、Amphotericin B。",
            "【重要例外】Isavuconazole 會「縮短 QT」，短 QT 症候群禁用！",
            "【本頁總結】TdP 風險是「QT藥物＋心搏過慢＋低鉀鎂＋藥物蓄積」共同形成的完美風暴！"
        ],
        "core": "本頁總結：TdP 風險通常不是單一藥物造成，而是「QT藥物＋心搏過慢＋低鉀鎂＋蓄積」共同形成"
    },
    # 38
    {
        "type": "content",
        "title": "Slide 38｜什麼情況下QT特別危險？",
        "tag": "PART 5｜看到異常，要想到可能是藥物",
        "body": [
            "【高風險組合】多種QT藥物併用、低血鉀、低血鎂、低血鈣、心搏過慢、女性、高齡、心衰竭/缺血、肝腎不全、藥物蓄積。",
            "【提高警覺指標】QTc ≥ 500 ms、較基準值增加 ≥ 60 ms、新發 VPC、短暫多型性 VT、心悸/暈厥。",
            "【處置 5 步驟 SOP】",
            "1. 確認心電圖與 QTc。    2. 檢視所有延長 QT 藥物。    3. 檢查並矯正血鉀、血鎂與血鈣。",
            "4. 評估心搏過慢及藥物蓄積。    5. 明顯異常時立即回報醫師並備妥除顫器！"
        ],
        "core": "處置：確認 ECG/QTc → 檢視停藥 → 矯正鉀鎂鈣 → 評估緩脈蓄積 → 異常立報備除顫"
    },
    # 39
    {
        "type": "content",
        "title": "Slide 39｜輸注反應、過敏與嚴重皮膚反應",
        "tag": "PART 5｜看到異常，要想到可能是藥物",
        "body": [
            "• Vancomycin 輸注反應（紅人症）：與輸注速率相關｜臉、頸或上半身潮紅、搔癢、紅疹、胸背不適、血壓降｜處置：減慢輸注速率(≥60分鐘)。",
            "• 嚴重過敏反應（Anaphylaxis）：蕁麻疹、嘴唇/舌/喉部腫脹、喘鳴、呼吸困難、血壓下降休克、意識改變｜首選肌注 Epinephrine！",
            "【核心提醒】嚴重過敏反應可能沒有皮膚症狀，不能只靠有無紅疹判斷！"
        ],
        "core": "提醒：嚴重過敏反應可能沒有皮膚症狀，不能只靠有無紅疹判斷"
    },
    # 40
    {
        "type": "content",
        "title": "Slide 40｜看到紅疹，如何判斷嚴重度？",
        "tag": "PART 5｜看到異常，要想到可能是藥物",
        "body": [
            "• 較低風險表現：局部或輕微紅疹、輕微搔癢、生命徵象穩定、無黏膜或器官侵犯。",
            "• 嚴重紅疹 10 大警訊：皮膚疼痛、臉部水腫、黏膜糜爛(口眼生殖器)、水泡、表皮剝離、發燒、呼吸困難、血壓降、嗜酸球增加、肝腎肺功能異常。",
            "• 嚴重疾病：嚴重過敏反應、DRESS、Stevens-Johnson syndrome (SJS)、Toxic epidermal necrolysis (TEN)。",
            "【核心訊息】紅疹合併黏膜侵犯、臉部水腫或器官功能異常，不是單純皮膚過敏！"
        ],
        "core": "核心訊息：紅疹合併黏膜侵犯、臉部水腫或器官功能異常，不是單純皮膚過敏"
    },
    # 41
    {
        "type": "content",
        "title": "Slide 41｜看到這些異常，你會想到哪個藥？",
        "tag": "整合應用與總結",
        "body": [
            "• 情境一：Heparin使用第6天，血小板由22萬降至9萬／mm³ → 跌幅>50%，懷疑 HIT！評估4Ts立報停肝素。",
            "• 情境二：使用Amiodarone及Levofloxacin，QTc 525 ms，血鉀3.1 mmol/L → 多重QT藥＋低血鉀致TdP高危！檢視藥物立報補鉀。",
            "• 情境三：Propofol持續輸注後乳酸上升、代謝酸、CK飆高、心搏過慢 → 懷疑 PRIS！立報停藥評估替代鎮靜。",
            "• 情境四：抗生素後發燒、臉水腫、全身皮疹、嗜酸球增加、肝功能異常 → 懷疑 DRESS 症候群！立報評估停藥。"
        ],
        "core": "一：HIT；二：多重 QT 延長＋低血鉀 TdP 風險；三：PRIS；四：DRESS 症候群"
    },
    # 42
    {
        "type": "content",
        "title": "Slide 42｜總結：帶回臨床的藥物安全檢查",
        "tag": "整合應用與總結",
        "body": [
            "【五項病人變化】",
            "1. 血壓、心率與器官灌流。    2. 意識、鎮靜深度與呼吸。    3. 心電圖與 QTc。",
            "4. 血小板、血紅素、PT 與 INR。    5. 皮膚、黏膜與過敏表現。",
            "【四項用藥確認】",
            "• 適應症：為什麼使用？    • 管路：從哪條管路給藥？",
            "• 趨勢：數值及症狀如何變化？    • 救援處置：異常時如何暫停、處理與回報？",
            "【結尾】知道為什麼給、給完看什麼、異常時立即辨識與回報！"
        ],
        "core": "結尾：知道為什麼給、給完看什麼、異常時立即辨識與回報"
    },
    # 43
    {
        "type": "cover",
        "title": "感謝聆聽 • 守護加護病房用藥安全",
        "subtitle": "Q & A • 討論與學習總結",
        "meta": "主講人：李芸瑄 藥師 • 2026.09.09 • 敬請指教",
        "tag": "Q & A • THANK YOU",
        "core": "知道為什麼給、給完看什麼、異常時立即辨識與回報！"
    }
]

def make_slide_xml_white(s, slide_idx):
    stype = s.get("type", "content")
    title = html.escape(s.get("title", ""))
    tag = html.escape(s.get("tag", ""))
    core = html.escape(s.get("core", ""))
    
    if stype == "cover":
        subtitle = html.escape(s.get("subtitle", ""))
        meta = html.escape(s.get("meta", ""))
        xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      
      <!-- Tag Box -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="Tag"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="800000" y="900000"/><a:ext cx="10592000" cy="500000"/></a:xfrm></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="zh-TW" sz="1600" b="1"><a:solidFill><a:srgbClr val="0284C7"/></a:solidFill></a:rPr><a:t>● {tag}</a:t></a:r></a:p></p:txBody>
      </p:sp>

      <!-- Title Box -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Title"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="800000" y="1500000"/><a:ext cx="10592000" cy="2400000"/></a:xfrm></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/>
          <a:p><a:r><a:rPr lang="zh-TW" sz="4400" b="1"><a:solidFill><a:srgbClr val="0F172A"/></a:solidFill></a:rPr><a:t>{title}</a:t></a:r></a:p>
          <a:p><a:r><a:rPr lang="zh-TW" sz="2400" b="1"><a:solidFill><a:srgbClr val="334155"/></a:solidFill></a:rPr><a:t>{subtitle}</a:t></a:r></a:p>
        </p:txBody>
      </p:sp>

      <!-- Meta Box -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="4" name="Meta"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="800000" y="4300000"/><a:ext cx="10592000" cy="800000"/></a:xfrm></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="zh-TW" sz="2000" b="1"><a:solidFill><a:srgbClr val="0369A1"/></a:solidFill></a:rPr><a:t>{meta}</a:t></a:r></a:p></p:txBody>
      </p:sp>

      <!-- Core Message Banner -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="5" name="Core"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="800000" y="5300000"/><a:ext cx="10592000" cy="800000"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val 20000"/></a:avLst></a:prstGeom>
          <a:solidFill><a:srgbClr val="F0F9FF"/></a:solidFill>
          <a:ln w="25400"><a:solidFill><a:srgbClr val="0284C7"/></a:solidFill></a:ln>
        </p:spPr>
        <p:txBody><a:bodyPr anchor="ctr"/><a:lstStyle/><a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="zh-TW" sz="2000" b="1"><a:solidFill><a:srgbClr val="0369A1"/></a:solidFill></a:rPr><a:t>{core}</a:t></a:r></a:p></p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMap/></p:clrMapOvr>
</p:sld>'''
    elif stype == "transition":
        quote = html.escape(s.get("quote", ""))
        xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="F8FAFC"/></a:solidFill></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      
      <!-- Tag Badge -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="PartBadge"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="3896000" y="1400000"/><a:ext cx="4400000" cy="650000"/></a:xfrm></p:spPr>
          <a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val 25000"/></a:avLst></a:prstGeom>
          <a:solidFill><a:srgbClr val="E0F2FE"/></a:solidFill>
          <a:ln w="19050"><a:solidFill><a:srgbClr val="0284C7"/></a:solidFill></a:ln>
        </p:spPr>
        <p:txBody><a:bodyPr anchor="ctr"/><a:lstStyle/><a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="zh-TW" sz="1800" b="1"><a:solidFill><a:srgbClr val="0369A1"/></a:solidFill></a:rPr><a:t>{tag}</a:t></a:r></a:p></p:txBody>
      </p:sp>

      <!-- Main Title -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Title"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="800000" y="2300000"/><a:ext cx="10592000" cy="1500000"/></a:xfrm></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="zh-TW" sz="4200" b="1"><a:solidFill><a:srgbClr val="0F172A"/></a:solidFill></a:rPr><a:t>{title}</a:t></a:r></a:p></p:txBody>
      </p:sp>

      <!-- Quote Box -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="4" name="Quote"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="1400000" y="4100000"/><a:ext cx="9392000" cy="1400000"/></a:xfrm></p:spPr>
          <a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val 15000"/></a:avLst></a:prstGeom>
          <a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>
          <a:ln w="25400"><a:solidFill><a:srgbClr val="0284C7"/></a:solidFill></a:ln>
        </p:spPr>
        <p:txBody><a:bodyPr anchor="ctr"/><a:lstStyle/><a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="zh-TW" sz="2400" b="1"><a:solidFill><a:srgbClr val="0369A1"/></a:solidFill></a:rPr><a:t>{quote}</a:t></a:r></a:p></p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMap/></p:clrMapOvr>
</p:sld>'''
    else:
        # Standard content slide (Fill space generously, larger text)
        body_lines = s.get("body", [])
        paragraphs_xml = ""
        for line in body_lines:
            line_esc = html.escape(line)
            is_bold = line_esc.startswith("【") or line_esc.startswith("•") or line_esc.startswith("1.") or line_esc.startswith("2.")
            color = "1E293B"
            sz = "2000"  # 20pt for crystal clear reading
            if line_esc.startswith("【"):
                color = "0284C7"
                sz = "2200"  # 22pt section labels
            elif "核心" in line_esc or "立即回報" in line_esc or "警訊" in line_esc or "致命" in line_esc:
                color = "B91C1C"
            
            paragraphs_xml += f'''
          <a:p>
            <a:pPr marL="288000" indent="-288000" spaceBefore="60000" spaceAfter="60000"/>
            <a:r>
              <a:rPr lang="zh-TW" sz="{sz}" b="{ '1' if is_bold else '0' }">
                <a:solidFill><a:srgbClr val="{color}"/></a:solidFill>
              </a:rPr>
              <a:t>{line_esc}</a:t>
            </a:r>
          </a:p>'''

        xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:bg><p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill></p:bgPr></p:bg>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
      
      <!-- Tag / Header -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="2" name="Tag"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="650000" y="380000"/><a:ext cx="10892000" cy="380000"/></a:xfrm></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="zh-TW" sz="1500" b="1"><a:solidFill><a:srgbClr val="0284C7"/></a:solidFill></a:rPr><a:t>{tag}</a:t></a:r></a:p></p:txBody>
      </p:sp>

      <!-- Slide Title -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="3" name="Title"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="650000" y="760000"/><a:ext cx="10892000" cy="650000"/></a:xfrm></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr lang="zh-TW" sz="3000" b="1"><a:solidFill><a:srgbClr val="0F172A"/></a:solidFill></a:rPr><a:t>{title}</a:t></a:r></a:p></p:txBody>
      </p:sp>

      <!-- Content Card Surface -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="4" name="CardBg"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>
        <p:spPr>
          <a:xfrm><a:off x="650000" y="1480000"/><a:ext cx="10892000" cy="4750000"/></a:xfrm>
          <a:prstGeom prst="roundRect"><a:avLst><a:gd name="adj" fmla="val 12000"/></a:avLst></a:prstGeom>
          <a:solidFill><a:srgbClr val="F8FAFC"/></a:solidFill>
          <a:ln w="22225"><a:solidFill><a:srgbClr val="CBD5E1"/></a:solidFill></a:ln>
        </p:spPr>
        <p:txBody>
          <a:bodyPr bIns="220000" lIns="300000" rIns="300000" tIns="240000" anchor="ctr"/>
          <a:lstStyle/>
          {paragraphs_xml}
        </p:txBody>
      </p:sp>

      <!-- Slide number bottom right -->
      <p:sp>
        <p:nvSpPr><p:cNvPr id="5" name="SlideNum"/><p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>
        <p:spPr><a:xfrm><a:off x="10600000" y="6300000"/><a:ext cx="942000" cy="400000"/></a:xfrm></p:spPr>
        <p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:pPr algn="r"/><a:r><a:rPr lang="zh-TW" sz="1400" b="1"><a:solidFill><a:srgbClr val="94A3B8"/></a:solidFill></a:rPr><a:t>{slide_idx} / 43</a:t></a:r></a:p></p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMap/></p:clrMapOvr>
</p:sld>'''
    return xml

def generate_white_pptx(output_file):
    num_slides = len(slides_data)
    print(f"Generating white theme PPTX ({num_slides} slides) into {output_file}...")
    
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        overrides = ""
        for i in range(1, num_slides + 1):
            overrides += f'  <Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>\n'
        
        zf.writestr('[Content_Types].xml', f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
{overrides}</Types>''')

        zf.writestr('_rels/.rels', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>''')

        pres_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/>\n'''
        for i in range(1, num_slides + 1):
            pres_rels += f'  <Relationship Id="rId{i+2}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>\n'
        pres_rels += '</Relationships>'
        zf.writestr('ppt/_rels/presentation.xml.rels', pres_rels)

        sld_ids = ""
        for i in range(1, num_slides + 1):
            sld_ids += f'    <p:sldId id="{255 + i}" r:id="rId{i+2}"/>\n'
            
        zf.writestr('ppt/presentation.xml', f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:sldMasterIdLst>
    <p:sldMasterId id="2147483648" r:id="rId1"/>
  </p:sldMasterIdLst>
  <p:sldIdLst>
{sld_ids}  </p:sldIdLst>
  <p:sldSz cx="12192000" cy="6858000" type="screen16x9"/>
  <p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>''')

        zf.writestr('ppt/theme/theme1.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Medical White Theme">
  <a:themeElements>
    <a:clrScheme name="Medical Clinical">
      <a:dk1><a:srgbClr val="0F172A"/></a:dk1>
      <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="334155"/></a:dk2>
      <a:lt2><a:srgbClr val="F8FAFC"/></a:lt2>
      <a:accent1><a:srgbClr val="0284C7"/></a:accent1>
      <a:accent2><a:srgbClr val="0D9488"/></a:accent2>
      <a:accent3><a:srgbClr val="DC2626"/></a:accent3>
      <a:accent4><a:srgbClr val="D97706"/></a:accent4>
      <a:accent5><a:srgbClr val="16A34A"/></a:accent5>
      <a:accent6><a:srgbClr val="7C3AED"/></a:accent6>
      <a:hlink><a:srgbClr val="0284C7"/></a:hlink>
      <a:folHlink><a:srgbClr val="64748B"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="Modern Sans">
      <a:majorFont><a:latin typeface="Arial"/><a:ea typeface="Noto Sans TC"/></a:majorFont>
      <a:minorFont><a:latin typeface="Arial"/><a:ea typeface="Noto Sans TC"/></a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="Office">
      <a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst>
      <a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst>
      <a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle><a:effectStyle><a:effectLst/></a:effectStyle><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>
      <a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst>
    </a:fmtScheme>
  </a:themeElements>
</a:theme>''')

        zf.writestr('ppt/slideMasters/_rels/slideMaster1.xml.rels', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>''')

        zf.writestr('ppt/slideMasters/slideMaster1.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst>
    <p:sldLayoutId id="2147483649" r:id="rId1"/>
  </p:sldLayoutIdLst>
</p:sldMaster>''')

        zf.writestr('ppt/slideLayouts/_rels/slideLayout1.xml.rels', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>''')

        zf.writestr('ppt/slideLayouts/slideLayout1.xml', '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank">
  <p:cSld name="Blank">
    <p:spTree>
      <p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>
      <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr><a:masterClrMap/></p:clrMapOvr>
</p:sldLayout>''')

        slide_layout_rel = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>'''

        for idx, slide_item in enumerate(slides_data, start=1):
            zf.writestr(f'ppt/slides/_rels/slide{idx}.xml.rels', slide_layout_rel)
            slide_xml = make_slide_xml_white(slide_item, idx)
            zf.writestr(f'ppt/slides/slide{idx}.xml', slide_xml)

    with open(output_file, 'wb') as f:
        f.write(buf.getvalue())
    print(f"Generated {output_file} ({len(buf.getvalue())} bytes) in clean White Theme with enlarged fonts!")

if __name__ == '__main__':
    out_path = '/Users/liyunsyuan/.gemini/antigravity/scratch/icu-medication-safety-presentation/icu_medication_safety_presentation.pptx'
    generate_white_pptx(out_path)
