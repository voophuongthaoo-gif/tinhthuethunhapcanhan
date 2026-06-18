import streamlit as st

# Tiêu đề ứng dụng
st.image("IMG_3080.jpg")
st.title("💰 App tính Thuế Thu Nhập Cá Nhân đề tài 7 Võ Phương Thảo")

# Nhập dữ liệu
thu_nhap = st.number_input(
    "Nhập thu nhập trước thuế (VNĐ)",
    min_value=0.0,
    value=20000000.0
)

nguoi_phu_thuoc = st.number_input(
    "Nhập số người phụ thuộc",
    min_value=0,
    value=0
)

if st.button("Tính thuế"):

    # Các khoản giảm trừ
    giam_tru_ban_than = 15500000
    giam_tru_phu_thuoc = nguoi_phu_thuoc * 6200000
    bao_hiem = thu_nhap * 0.105

    tong_giam_tru = (
        giam_tru_ban_than
        + giam_tru_phu_thuoc
        + bao_hiem
    )

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = max(
        0,
        thu_nhap - tong_giam_tru
    )

    # Tính thuế lũy tiến từng phần
    tax = 0

    if thu_nhap_tinh_thue <= 5000000:
        tax = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 10000000:
        tax = 250000 + (thu_nhap_tinh_thue - 5000000) * 0.10

    elif thu_nhap_tinh_thue <= 18000000:
        tax = 750000 + (thu_nhap_tinh_thue - 10000000) * 0.15

    elif thu_nhap_tinh_thue <= 32000000:
        tax = 1950000 + (thu_nhap_tinh_thue - 18000000) * 0.20

    elif thu_nhap_tinh_thue <= 52000000:
        tax = 4750000 + (thu_nhap_tinh_thue - 32000000) * 0.25

    elif thu_nhap_tinh_thue <= 80000000:
        tax = 9750000 + (thu_nhap_tinh_thue - 52000000) * 0.30

    else:
        tax = 18150000 + (thu_nhap_tinh_thue - 80000000) * 0.35

    thu_nhap_sau_thue = thu_nhap - bao_hiem - tax

    st.success("Kết quả tính toán")

    st.write(f"📌 Thu nhập trước thuế: **{thu_nhap:,.0f} VNĐ**")
    st.write(f"📌 Giảm trừ bản thân: **{giam_tru_ban_than:,.0f} VNĐ**")
    st.write(f"📌 Giảm trừ người phụ thuộc: **{giam_tru_phu_thuoc:,.0f} VNĐ**")
    st.write(f"📌 Bảo hiểm bắt buộc (10.5%): **{bao_hiem:,.0f} VNĐ**")
    st.write(f"📌 Thu nhập tính thuế: **{thu_nhap_tinh_thue:,.0f} VNĐ**")
    st.write(f"📌 Thuế TNCN phải nộp: **{tax:,.0f} VNĐ**")
    st.write(f"📌 Thu nhập sau thuế: **{thu_nhap_sau_thue:,.0f} VNĐ**")
