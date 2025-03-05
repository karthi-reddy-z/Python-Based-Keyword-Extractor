# **Keyword Extractor**  

### **🚀 Extract Keywords from Text, Files, and URLs using Python Flask**  
 
A simple **web-based keyword extractor** that identifies the most important words from **text input, uploaded files, or URLs**.  

---

## **📌 Features**  
✔️ Extract keywords from **manual text input**  
✔️ Process **uploaded `.txt` files**  
✔️ Scrape and extract keywords from **URLs**  
✔️ User-friendly **Flask-powered UI**  
✔️ Beautiful **CSS-styled interface**  

---

## **🖥️ Live Demo**  
Run the project locally and access it at **`http://127.0.0.1:5000`**  

---

## **🛠️ Tech Stack**  
- **Python** (Flask, Requests, BeautifulSoup)  
- **HTML & CSS** (Frontend UI)  

---

## **📂 Folder Structure**  
```
keyword-extractor/
│── static/
│   ├── styles.css
│── templates/
│   ├── index.html
│── app.py
│── requirements.txt
│── README.md
```

---

## **🛠️ Installation & Setup**  
### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/your-username/keyword-extractor.git
cd keyword-extractor
```

### **2️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Application**  
```sh
python app.py
```
Open **`http://127.0.0.1:5000`** in your browser.

---

## **📝 Usage Guide**  
1️⃣ **Paste Text** → Enter or paste text into the input box  
2️⃣ **Upload File** → Upload a `.txt` file for processing  
3️⃣ **Enter URL** → Provide a webpage URL to extract text  
4️⃣ **Click "Extract Keywords"** → View extracted keywords  

---

## **📜 Example Output**  
**Input Text:**  
*"Machine learning is a method of data analysis that automates analytical model building."*  

**Extracted Keywords:**  
`machine, learning, method, data, analysis, automates, model, building`

---

## **📌 Deployment (Optional)**  
To deploy the project on a server:  
```sh
pip install gunicorn
gunicorn -w 4 app:app
```

---

## **🌟 Contributing**  
Feel free to **fork** the repository, create a **feature branch**, and submit a **pull request**.

---

## **📜 License**  
This project is **open-source** under the **MIT License**.  
