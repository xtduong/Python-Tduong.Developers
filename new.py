import pandas as pd
import matplotlib.pyplot as plt

Tduong_Developers = {
    "Màu": "blue",
    "Dữ Liệu Học Sinh": [
        {"Tên": "Nguyễn Văn A", "Ngày Sinh": "01/05/2000", "Số Điểm": 85, "Thời Gian": 120, "Trạng Thái": "Thành Công"},
        {"Tên": "Trần Thị B", "Ngày Sinh": "15/08/2001", "Số Điểm": 78, "Thời Gian": 110, "Trạng Thái": "Thành Công"},
        {"Tên": "Lê Văn C", "Ngày Sinh": "20/03/2002", "Số Điểm": 92, "Thời Gian": 130, "Trạng Thái": "Thành Công"},
        {"Tên": "Phạm Thị D", "Ngày Sinh": "10/12/2003", "Số Điểm": 70, "Thời Gian": 105, "Trạng Thái": "Không Thành Công"},
    ]
}

df = pd.DataFrame(Tduong_Developers["Dữ Liệu Học Sinh"])

# TUNGDUONG
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('tight')
ax.axis('off')
ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', colColours=[Tduong_Developers["Màu"]]*len(df.columns))
plt.title('Bảng dữ liệu học sinh - Tduong.Developers', fontsize=16)
plt.show()
