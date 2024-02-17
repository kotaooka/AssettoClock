import ac
import acsys
import time

# デフォルトの設定値
DEFAULT_FONT = "Arial"
DEFAULT_FONT_SIZE = 30
DEFAULT_TIME_FORMAT = "%H:%M:%S"  # 24時間制

# グローバル変数
clock_label = None
font_dropdown = None
font_size_slider = None
time_format_dropdown = None

def acMain(ac_version):
    global clock_label, font_dropdown, font_size_slider, time_format_dropdown
    
    app_window = ac.newApp("Clock Settings")
    ac.setSize(app_window, 300, 200)
    
    # フォントのドロップダウンメニュー
    font_dropdown = ac.addDropdown(app_window, "Font:")
    ac.setPosition(font_dropdown, 10, 30)
    ac.setSize(font_dropdown, 200, 30)
    ac.addDropdownItem(font_dropdown, DEFAULT_FONT)
    # 利用可能なフォントを追加する必要がある場合は、ここに追加します
    
    # フォントサイズのスライダー
    font_size_slider = ac.addSlider(app_window, "Font Size:")
    ac.setPosition(font_size_slider, 10, 70)
    ac.setSize(font_size_slider, 200, 30)
    ac.setSliderRange(font_size_slider, 10, 50)
    ac.setSliderValue(font_size_slider, DEFAULT_FONT_SIZE)
    
    # 時計の表示形式のドロップダウンメニュー
    time_format_dropdown = ac.addDropdown(app_window, "Time Format:")
    ac.setPosition(time_format_dropdown, 10, 110)
    ac.setSize(time_format_dropdown, 200, 30)
    ac.addDropdownItem(time_format_dropdown, "24-hour (HH:MM:SS)")
    ac.addDropdownItem(time_format_dropdown, "12-hour (h:MM:SS AM/PM)")
    
    # 時計のラベル
    clock_label = ac.addLabel(app_window, "")
    ac.setPosition(clock_label, 10, 150)
    ac.setSize(clock_label, 200, 30)
    ac.setFontSize(clock_label, DEFAULT_FONT_SIZE)
    
    return "Clock Settings"

def update_clock(delta_time):
    current_time = time.strftime(get_time_format(), time.localtime())
    ac.setText(clock_label, current_time)

def get_time_format():
    selected_index = ac.getDropdownCurrentIndex(time_format_dropdown)
    if selected_index == 1:
        return "%I:%M:%S %p"  # 12-hour format
    else:
        return DEFAULT_TIME_FORMAT  # 24-hour format

def on_form_close(form_id):
    if form_id == 0:
        ac.log("Clock Settings form closed")
        ac.removeRenderCallback(update_clock)

ac.addRenderCallback(update_clock)
ac.addOnAppFormCloseListener(on_form_close)

# スクリプトの初期化
ac.log("Clock Settings initialized")
