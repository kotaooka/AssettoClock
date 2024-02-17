import ac
import acsys
import time

# ウィジェットの初期化
def acMain(ac_version):
    app_window = ac.newApp("Time Widget")
    ac.setSize(app_window, 200, 50)
    ac.drawBorder(app_window, 0)
    ac.setBackgroundOpacity(app_window, 0)
    
    # 時刻を表示するラベルを作成
    time_label = ac.addLabel(app_window, "Time: ")
    ac.setPosition(time_label, 10, 10)
    ac.setFontSize(time_label, 18)
    
    # 毎フレーム更新
    ac.addRenderCallback(app_window, update_time)
    
    return "Time Widget"

# 時刻を更新するコールバック関数
def update_time(delta_time):
    current_time = time.strftime("%H:%M:%S", time.localtime())
    ac.setText(time_label, "Time: {}".format(current_time))


