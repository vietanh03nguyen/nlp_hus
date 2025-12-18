Khó khăn:
- Gặp vấn đề về chạy Script trong VScode từ subfolder có import relative
    - Giải quyết tạm thời bằng cách đặt file script ra thư mục gốc root
- Gặp vấn đề khi import pyspark trên Windows VSCode
    - Giải quyết bằng chuyển sang Colab

Task 1: Chuẩn bị data và triển khai mô hình TextClassifier
- Sử dụng Count Vectorizer từ Lab 2
- Triển khai thành công mô hình TextClassifier theo hướng dẫn có ứng dụng mô hình Logistic Regression.
    - Xây dựng hàm dựng của class TextClassifier chứa tính chất _model
    - Xây dựng hàm fit có pipeline sử dụng RegexTokenizer + CountVectorizer + LogisticRegression
    - Xây dựng hàm predict dự đoán label trên text mới
    - Xây dựng hàm evaluate trả về dictionary chứa tên metric sử dụng và giá trị đánh giá.

Task 2: Đánh giá
- Tạo dataset nhỏ và chia 80/20 bằng train_test_split của sklearn
- Khởi tạo các mô hình RegexTokenizer và CountVectorizer
- Khởi tạo mô hình TextClassfier
- Train classifier và test trên dataset đã chia
- Đánh giá mô hình bằng hàm evaluate

Task 3: Sentiment Analysis với Spark
- Máy local gặp vấn đề với sử dụng spark => Sử dụng Colab -> Xuất ra file lab4_spark.ipynb trong folder labs
- Hướng dẫn chạy: 
    1. Upload lab4_spark.ipynb lên Colab 
    2. Upload data sentiments.csv lên folder contents của instance Colab
    3. Run all
- Thử nghiệm thành công pipeline bao gồm Tokenizer, StopwordsRemover, hashingTF và IDF

Task 4: Cải thiện kết quả mô hình:
- Sử dụng Word2Vec thay HashingTF + IDF trong pipeline.
- Kết quả đạt dược kém hơn khi dữ liệu nhỏ
    - Rút ra kinh nghiệm nên sử dụng W2Vec với bộ dữ liệu lớn
- Chưa thực hiện với bộ dữ liệu lớn hơn.
