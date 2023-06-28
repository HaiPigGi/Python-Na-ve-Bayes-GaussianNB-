import pandas as pd
from tkinter import Tk, Label, Button, Frame
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def train_and_evaluate_model():
    #Langkah 1: Muat kumpulan data
    data = pd.read_csv('bank.csv', delimiter=';', quoting=3)

    # Step 2: Praproses data/memproses data
    categorical_columns = ['"job"', '"marital"', '"education"', '"default"', '"housing"', '"loan"', '"contact"', '"month"', '"poutcome"', '"y"']
    for column in categorical_columns:
        data[column].fillna('unknown', inplace=True)
        label_encoder = LabelEncoder()
        data[column] = label_encoder.fit_transform(data[column])

    # Step 3: Pisahkan kumpulan data
    X = data.drop('"duration"', axis=1)
    y = data['"duration"']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 4: mencoba pengklasifikasi Naïve Bayes / membuat sebuah model klasifikasi Naive Bayes dengan distribusi Gaussian (Gaussian Naive Bayes).
    clf = GaussianNB()
    clf.fit(X_train, y_train)

    # Step 5: Membuat prediksi / melakukan prediksi pada data uji (X_test).
    y_pred = clf.predict(X_test)

    # Step 6: Evaluasi modelnya / menghitung beberapa metrik evaluasi kinerja model klasifikasi.
    accuracy = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred, average='macro', zero_division=1)
    recall = metrics.recall_score(y_test, y_pred, average='macro', zero_division=1)

    # membuat gui windows
    window = Tk()
    window.title("Naïve Bayes Classifier")

    print("Akurasi : ",accuracy)
    print("Precision : ",precision)
    print("Recall : ",recall)

    # Buat label untuk menampilkan output
    accuracy_label = Label(window, text="Accuracy: {:.2f}".format(accuracy))
    precision_label = Label(window, text="Precision: {:.2f}".format(precision))
    recall_label = Label(window, text="Recall: {:.2f}".format(recall))

    #mengatur label di jendela
    accuracy_label.pack()
    precision_label.pack()
    recall_label.pack()

    # Create a frame for the plot
    plot_frame = Frame(window)
    plot_frame.pack()

    # menampilkan plot scor nya
    scores = [accuracy, precision, recall]
    score_labels = ['Accuracy', 'Precision', 'Recall']
    fig, ax = plt.subplots()
    ax.bar(score_labels, scores)
    ax.set_ylabel('Score')
    ax.set_ylim([0, 1])
    ax.set_title('Evaluation Metrics')
    plt.tight_layout()

    # Buat kanvas untuk menampilkan plot
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # membuat button close
    close_button = Button(window, text="Close", command=window.destroy)

  
    close_button.pack()

   
    window.mainloop()


# Call the function to train and evaluate the model
train_and_evaluate_model()
