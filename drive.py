import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="App Dạy Lái Xe Online Pro",
    page_icon="🚗",
    layout="wide"
)

# Khởi tạo trạng thái đăng ký VIP trong phiên làm việc
if "is_vip" not in st.session_state:
    st.session_state.is_vip = False

# Sidebar chọn chức năng
st.sidebar.title("🚗 MENU ĐÀO TẠO LÁI XE")
menu = st.sidebar.radio(
    "Chọn danh mục:",
    ["Trang chủ & Giới thiệu", "Học lý thuyết & Mẹo", "Thi thử trắc nghiệm", "Nâng cấp tài khoản VIP (Thanh toán)"]
)

# ----------------- TRANG CHỦ -----------------
if menu == "Trang chủ & Giới thiệu":
    st.title("🌟 CHÀO MỪNG ĐẾN VỚI HỆ THỐNG HỌC LÁI XE ONLINE")
    st.write("Ứng dụng hỗ trợ học ôn thi lý thuyết và thực hành lái xe các hạng B1, B2, C chuẩn sát cấu trúc đề thi của Tổng cục Đường bộ Việt Nam.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Bộ đề chuẩn", value="600 Câu", delta="Mới nhất")
    with col2:
        st.metric(label="Mẹo ghi nhớ nhanh", value="100%", delta="Đậu cao")
    with col3:
        status_vip = "Đã kích hoạt" if st.session_state.is_vip else "Chưa kích hoạt"
        st.metric(label="Gói tài khoản", value=status_vip)
        
    st.info("💡 **Mẹo:** Nâng cấp tài khoản VIP để mở khóa toàn bộ câu hỏi điểm liệt, mẹo giải nhanh và video mô phỏng các tình huống giao thông nguy hiểm!")

# ----------------- HỌC LÝ THUYẾT -----------------
elif menu == "Học lý thuyết & Mẹo":
    st.title("📚 HỆ THỐNG LÝ THUYẾT & MẸO THI")
    
    tab1, tab2 = st.tabs(["📖 Cấu trúc 600 câu", "⚡ Mẹo giải nhanh"])
    
    with tab1:
        st.subheader("Phân bổ nội dung 600 câu hỏi ôn thi lý thuyết:")
        st.markdown("""
        * **Khái niệm và quy tắc giao thông đường bộ:** Từ câu 1 đến câu 166.
        * **Văn hóa giao thông và đạo đức người lái xe:** Từ câu 167 đến câu 182.
        * **Kỹ thuật lái xe:** Từ câu 183 đến câu 256.
        * **Cấu tạo và sửa chữa xe:** Từ câu 257 đến câu 317.
        * **Biển báo hiệu đường bộ:** Từ câu 318 đến câu 499.
        * **Giải thế sa hình và kỹ năng xử lý tình huống:** Từ câu 500 đến câu 600.
        """)
        
    with tab2:
        st.subheader("Bí kíp 'Học nhanh - Nhớ lâu - Không sợ trượt':")
        st.success("""
        1. **Từ khóa bắt buộc chọn ngay:** Các cụm từ như *'Bị nghiêm cấm', 'Không được phép', 'Phải có phép của cơ quan có thẩm quyền'* -> Chọn luôn ý có các từ này.
        2. **Giới hạn tốc độ:** 
           * Trong khu vực đông dân cư (không có dải phân cách): Tối đa **50 km/h**.
           * Trong khu vực đông dân cư (có dải phân cách): Tối đa **60 km/h**.
        3. **Câu hỏi về nồng độ cồn:** Đã uống rượu bia thì **TUYỆT ĐỐI KHÔNG** được lái xe (chọn mức phạt/nồng độ cồn bằng 0 hoặc nghiêm cấm tuyệt đối).
        """)

# ----------------- THI THỬ -----------------
elif menu == "Thi thử trắc nghiệm":
    st.title("📝 PHÒNG THI THỬ TRỰC TUYẾN")
    
    if not st.session_state.is_vip:
        st.warning("🔒 Bạn đang dùng tài khoản THƯỜNG. Bạn chỉ có thể làm thử 5 câu hỏi cơ bản. Vui lòng nâng cấp VIP để mở khóa toàn bộ đề thi chuẩn.")
        st.subheader("Câu hỏi mẫu số 1: Hành vi nào bị nghiêm cấm?")
        st.radio("Chọn đáp án đúng:", [
            "1. Điều khiển xe cơ giới chạy quá tốc độ quy định.",
            "2. Sử dụng ô, điện thoại di động khi đang điều khiển xe mô tô.",
            "3. Điều khiển xe ô tô mà trong máu hoặc hơi thở có nồng độ cồn.",
            "4. Cả ý 1, ý 2 và ý 3."
        ])
        if st.button("Nộp bài"):
            st.success("Chính xác! Đáp án đúng là số 4.")
    else:
        st.success("🎉 Bạn đang sở hữu tài khoản VIP! Toàn bộ 600 câu hỏi và video mô phỏng đã được mở khóa.")
        st.info("Hệ thống đề thi ngẫu nhiên 35 câu (đối với hạng B2) đang sẵn sàng cho bạn luyện tập.")

# ----------------- THANH TOÁN & NÂNG CẤP VIP -----------------
elif menu == "Nâng cấp tài khoản VIP (Thanh toán)":
    st.title("💎 NÂNG CẤP TÀI KHOẢN VIP ĐỂ MỞ KHÓA TOÀN BỘ")
    
    st.markdown("""
    * Mở khóa toàn bộ 600 câu hỏi sát hạch mới nhất.
    * Xem đầy đủ mẹo giải nhanh điểm liệt và sa hình.
    * Hỗ trợ giải đáp trực tuyến 24/7.
    * **Phí nâng cấp trọn đời:** **199.000 VNĐ**
    """)
    
    st.divider()
    
    st.subheader("💳 THÔNG TIN CHUYỂN KHOẢN THANH TOÁN")
    
    st.info("""
    Bạn vui lòng mở ứng dụng Ngân hàng (MB Bank, Vietcombank, Techcombank,...) và chuyển khoản theo thông tin sau:
    
    * **Ngân hàng:** MB Bank (Ngân hàng TMCP Quân Đội)
    * **Số tài khoản:** `0030132291981`
    * **Chủ tài khoản:** `HOANG HAI AN`
    * **Số tiền:** `199.000` VNĐ
    * **Nội dung chuyển khoản:** `VIP LAIXE [Số điện thoại của bạn]`
    """)
    
    st.divider()
    st.subheader("📝 XÁC NHẬN KÍCH HOẠT TÀI KHOẢN")
    st.write("Sau khi chuyển khoản thành công, hãy nhập thông tin chuyển khoản bên dưới để hệ thống duyệt và kích hoạt quyền VIP:")
    
    user_trans_code = st.text_input("Nhập Mã giao dịch / Số điện thoại chuyển khoản của bạn:")
    
    if st.button("Kích hoạt ngay"):
        if user_trans_code:
            st.session_state.is_vip = True
            st.balloons()
            st.success("🎉 Chúc mừng! Tài khoản của bạn đã được nâng cấp lên **VIP** thành công. Hãy quay lại mục Thi thử hoặc Học lý thuyết để trải nghiệm!")
        else:
            st.error("Vui lòng nhập thông tin mã giao dịch hoặc số điện thoại để hệ thống xác thực.")
