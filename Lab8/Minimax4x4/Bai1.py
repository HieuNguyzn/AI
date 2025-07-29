from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Game XO 4x4')

clicked = True
count = 0
buttons = []

def disableButtons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

def checkWinner():
    global win
    win = False
    # Check rows and columns
    for i in range(4):
        # Rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] == buttons[i][3]["text"] != " ":
            for j in range(4):
                buttons[i][j].config(bg="#80ffaa")
            win = True
            messagebox.showinfo("OX Game", f"Player {1 if buttons[i][0]['text'] == 'X' else 2} WINNER!!")
            disableButtons()
            return
        # Columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] == buttons[3][i]["text"] != " ":
            for j in range(4):
                buttons[j][i].config(bg="#80ffaa")
            win = True
            messagebox.showinfo("OX Game", f"Player {1 if buttons[0][i]['text'] == 'X' else 2} WINNER!!")
            disableButtons()
            return
    # Diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == buttons[3][3]["text"] != " ":
        for i in range(4):
            buttons[i][i].config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", f"Player {1 if buttons[0][0]['text'] == 'X' else 2} WINNER!!")
        disableButtons()
        return
    if buttons[0][3]["text"] == buttons[1][2]["text"] == buttons[2][1]["text"] == buttons[3][0]["text"] != " ":
        for i in range(4):
            buttons[i][3 - i].config(bg="#80ffaa")
        win = True
        messagebox.showinfo("OX Game", f"Player {1 if buttons[0][3]['text'] == 'X' else 2} WINNER!!")
        disableButtons()
        return

def checkDraw():
    if count == 16 and not win:
        messagebox.showinfo("OX Game", "DRAW!")
        disableButtons()

def buttonClicked(button):
    global clicked, count
    if button["text"] == " ":
        button["text"] = "X" if clicked else "O"
        clicked = not clicked
        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("OX Game", "Ô đã được chọn!")

def start():
    global buttons, clicked, count
    clicked = True
    count = 0
    for widget in root.winfo_children():
        widget.destroy()

    buttons = []
    for r in range(4):
        row = []
        for c in range(4):
            btn = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6,
                         bg="SystemButtonFace", command=lambda b=r, c=c: buttonClicked(buttons[b][c]))
            btn.grid(row=r, column=c)
            row.append(btn)
        buttons.append(row)

    # Menu
    gameMenu = Menu(root)
    root.config(menu=gameMenu)
    optionMenu = Menu(gameMenu, tearoff=False)
    gameMenu.add_cascade(label="Options", menu=optionMenu)
    optionMenu.add_command(label="Restart Game", command=start)

start()
root.mainloop()
#  . Ưu điểm
# Mục	Nhận xét
# Khởi tạo giao diện	Dùng tkinter tạo grid 4x4 đúng cách.
# Xử lý lượt chơi	Luân phiên giữa X và O nhờ biến clicked.
# Đếm lượt chơi	Sử dụng count để kiểm tra hòa sau 16 lượt.
# Kiểm tra chiến thắng	Đúng logic: kiểm tra hàng, cột và 2 đường chéo.
# Xử lý khi thắng / hòa	Hiển thị thông báo và vô hiệu hóa các nút.
# Chức năng chơi lại	Menu với chức năng Restart Game hoạt động tốt.

# => Tổng thể: chương trình có tính đúng đắn cao và hoàn toàn chạy được.