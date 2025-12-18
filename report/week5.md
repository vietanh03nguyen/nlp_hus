Lab5: RNN for Text and Token Classification

Part1: Tìm hiểu các mô hình RNN, LSTM, GRU và thực hành pytorch
- Thực hành torch được thực hiện trong labs/lab5_pytorch.ipynb


Part2: RNN cho phân loại văn bản
- Các mô hình w2v+Dense, Embedding+LSTM đem lại test_accuracy rất thấp so với mô hình TF-IDF + Logistic Regression
    - Nghi ngờ nguyên nhân có thể do lỗi xử lý dữ liệu hoặc mô hình

So sánh định lượng:
|Pipeline|F1-score|Test Loss|
|---|---|---|
|TF-IDF + Logistic Regression|0.8352983005857358||
|Word2Vec(Avg) + Dense|0.14141288639720895|3.1519622802734375|
|Embedding(Pre-trained) + LSTM|0.06178585513830433|3.381415843963623|
|Embedding(Scratch) + LSTM|0.0005422374429223744|4.124667167663574|

Phân tích định tính:
| True          | reminder_create | weather_query  | flight_search     |
|---------------|-----------------|----------------|-------------------|
| TF-IDF        | calendar_set    | weather_query  | general_negate    |
| Word2Vec      | general_explain | calendar_query | lists_createoradd |
| Pretrain-LSTM | qa_factoid      | qa_currency    | transport_taxi    |
| Scratch-LSTM  | play_game       | play_game      | play_game         |

- Mô hình TF-IDF là mo hình duy nhất có đưa ra được nhãn đúng với Weather Query
- Kết quả đi ngược với kì vọng rằng các mô hình mới hơn như LSTM sẽ cho kết quả tốt hơn các mô hình cổ điển như W2Vec hay TF-IDF
