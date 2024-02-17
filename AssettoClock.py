import ac
import acsys
import time

app_window = 0
time_label = 0

# ウィジェットの初期化
def acMain(ac_version):
    global app_window, time_label
    app_window = ac.newApp("AssettoClock")
    ac.setSize(app_window, 300, 100)
    ac.drawBorder(app_window, 0)
    ac.setBackgroundOpacity(app_window, 0)

    # 時刻を表示するラベルを作成
    time_label = ac.addLabel(app_window, "")
    ac.setPosition(time_label, 150, 55)  # 時計の位置をウィジェットの中央に設定
    ac.setFontSize(time_label, 25)
    ac.setFontAlignment(time_label, "center")
    ac.setFontColor(time_label, 1, 1, 1, 1)  # フォントの色を白に設定
    
    return "AssettoClock"

# 毎フレーム更新
def acUpdate(delta_t):
    current_time = time.strftime("%H:%M:%S", time.localtime())
    ac.setText(time_label, current_time)
    
# アプリが終了したときにウィジェットを破棄
def acShutdown():
    global app_window
    if app_window != 0:
        ac.log("Shutting down AssettoClock")
        ac.removeWidget(app_window)
        app_window = 0
        ac.log("Shutting down AssettoClock")
        ac.removeWidget(app_window)
        app_window = 0
