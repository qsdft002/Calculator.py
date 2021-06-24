import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('儲蓄貸款利率計算機')
window.geometry('700x450')

# 儲存計算label
output_list = []
# 儲存選項label
nameChange_list = []
# 儲存選項entry
textClear_list = []
# 儲蓄貸款名稱list
savingText=['存放金額：','儲蓄時間（年）：']
loanText=['貸款金額：','貸款時間（年）：']


def main():
    # 建立表頭
    header_label = tk.Label(window, text='請選擇要計算的項目', font=("微軟正黑體", 20))
    header_label.pack()
    # 建立儲蓄貸款選像框架
    choose_frame = tk.Frame(window)
    choose_frame.pack(side=tk.TOP)
    saving_btn = tk.Button(choose_frame, text='儲蓄', font=("微軟正黑體", 20)
                           , command=lambda: show(savingText))
    saving_btn.pack(side=tk.LEFT)
    loan_btn = tk.Button(choose_frame, text='貸款', font=("微軟正黑體", 20)
                         , command=lambda: show(loanText))
    loan_btn.pack(side=tk.LEFT)

def show(textList):
    # 判斷是否第一次建立框架
    if len(textClear_list) == 0:
        # >0、數字
        # 建立本金框架
        principal_frame = tk.Frame(window)
        principal_frame.pack(side=tk.TOP)
        principal_label = tk.Label(principal_frame, text='', font=("微軟正黑體", 20))
        principal_label.pack(side=tk.LEFT)
        principal_entry = tk.Entry(principal_frame, text='', font=("Consolas", 20))
        principal_entry.pack(side=tk.LEFT)
        nameChange_list.append(principal_label)
        textClear_list.append(principal_entry)
        # 建立利率框架
        rate_frame = tk.Frame(window)
        rate_frame.pack(side=tk.TOP)
        rate_label = tk.Label(rate_frame, text='複利年利率（%）：', font=("微軟正黑體", 20))
        rate_label.pack(side=tk.LEFT)
        rate_entry = tk.Entry(rate_frame, text='', font=("Consolas", 20))
        rate_entry.pack(side=tk.LEFT)
        textClear_list.append(rate_entry)
        # 建立次數框架>=1
        frequent_frame = tk.Frame(window)
        frequent_frame.pack(side=tk.TOP)
        frequent_label = tk.Label(frequent_frame, text='利息頻率（年）：', font=("微軟正黑體", 20))
        frequent_label.pack(side=tk.LEFT)
        frequent_entry = tk.Entry(frequent_frame, text='', font=("Consolas", 20))
        frequent_entry.pack(side=tk.LEFT)
        textClear_list.append(frequent_entry)
        # 建立時間框架
        time_frame = tk.Frame(window)
        time_frame.pack(side=tk.TOP)
        time_label = tk.Label(time_frame, text='', font=("微軟正黑體", 20))
        time_label.pack(side=tk.LEFT)
        time_entry = tk.Entry(time_frame, text='', font=("Consolas", 20))
        time_entry.pack(side=tk.LEFT)
        nameChange_list.append(time_label)
        textClear_list.append(time_entry)
        # 建立選項框架
        option_frame = tk.Frame(window)
        option_frame.pack(side=tk.TOP)

        # 建立清除按鈕
        clear_btn = tk.Button(option_frame, text='清除', font=("微軟正黑體", 20)
                              , command=lambda:clear())
        clear_btn.pack(side=tk.LEFT)
        # 建立計算按鈕
        count_btn = tk.Button(option_frame, text='計算', font=("微軟正黑體", 20),
                              command=lambda: check(principal_entry.get(),
                                                    rate_entry.get(),
                                                    frequent_entry.get(),
                                                    time_entry.get()))
        count_btn.pack(side=tk.LEFT)
    # 清空entry裡的值
    clear()
    # 更新選項label名稱，對照傳入的textList
    nameChange_list[0]['text'] = textList[0]
    nameChange_list[1]['text'] = textList[1]


def clear():
    # 針對所有entry做清空值的動作，並聚焦在第一個輸入空格
    for widget in textClear_list:
        widget.delete(0, 'end')
    textClear_list[0].focus()
    # 判斷是否有計算過，才隱藏計算的label
    if len(output_list) > 0:
        output_list[0].pack_forget()
        output_list[1].pack_forget()

def check(p, r, f, t):
    # 判斷輸入的值是否合宜
    msg = ''
    if len(p) == 0 or len(p) == 0 or len(p) == 0 or len(p) == 0:
        messagebox.showinfo('請修正', '請勿空白')
    else:
        p = eval(p)
        r = eval(r)
        f = eval(f)
        t = eval(t)

        if not isinstance(p, int):
            msg += '金額請為整數\n'
        elif p < 0:
            msg += '金額請大於0\n'
        if not isinstance(r, float) and not isinstance(r, int):
            msg += '年利率請為數值\n'
        elif r < 0:
            msg += '年利率請大於0\n'
        if not isinstance(f, float) and not isinstance(f, int):
            msg += '利息頻率請為數值\n'
        elif f < 0:
            msg += '利息頻率請大於0\n'
        if not isinstance(t, float) and not isinstance(t, int):
            msg += '時間請為數值\n'
        elif t < 0:
            msg += '時間請大於0\n'

        if len(msg) != 0:
            messagebox.showinfo('請修正', msg)
        else:
            count_saving(p, r, f, t)


def count_saving(p, r, f, t):
    # 課本範例
    i = r / f
    n = f * t
    amount = p * ((1 + i) ** n)

    result_msg = '經過' + str(t) + '年後：'
    amount_msg = '總金額為' + '${0:,.2f}'.format(amount)

    # 建立計算框架
    if len(output_list) == 0:
        result_frame = tk.Frame(window)
        result_frame.pack(side=tk.TOP)
        result_label = tk.Label(result_frame, text=result_msg, font=("微軟正黑體", 20))
        result_label.pack(side=tk.LEFT)
        amount_label = tk.Label(result_frame, text=amount_msg, font=("微軟正黑體", 20))
        amount_label.pack(side=tk.LEFT)
        output_list.append(result_label)
        output_list.append(amount_label)

    else:
        output_list[0].pack(side=tk.LEFT)
        output_list[1].pack(side=tk.LEFT)
        output_list[0]['text'] = result_msg
        output_list[1]['text'] = amount_msg


main()
window.mainloop()