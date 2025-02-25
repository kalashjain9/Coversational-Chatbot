# Coversational-Chatbot
🚀 AI-powered Streamlit Chatbot using Google Gemini API! Chat with AI, upload &amp; process multiple PDFs, and get brief &amp; detailed responses. Features aesthetic UI, secure API handling, and easy deployment. Built with Python &amp; Streamlit. ⭐ Star the repo &amp; contribute! 😊 #AI #Chatbot #Gemini #Streamlit
Here’s a **README.md** file for your **Streamlit Chatbot** project. It includes setup instructions, features, and deployment steps.  

---

## **📌 Aesthetic Multimodal Chatbot using Gemini API**
This is an AI-powered chatbot built with **Streamlit** and **Google Gemini API**. It supports **text-based Q&A** and **PDF file processing**, allowing users to chat with AI and extract insights from uploaded PDFs.

---

## **🚀 Features**
✅ **Chat with AI** – Uses Google Gemini API for smart responses  
✅ **PDF Upload & Processing** – Extracts text and answers queries from PDFs  
✅ **Aesthetic UI** – Designed with an elegant, user-friendly interface  
✅ **Multiple File Uploads** – Supports batch processing of multiple PDFs  
✅ **.env File for API Key** – Secure API key storage  

---

## **📂 Project Structure**
```
📁 Conversational Chatbot
│── 📂 new
│   ├── app.py            # Main Streamlit app
│   ├── utils.py          # Helper functions (PDF processing, Gemini API calls)
│   ├── .env              # Store API key securely
│   ├── requirements.txt  # Dependencies
│── 📄 README.md          # Documentation
```
Try a demo : https://conversationalchatbotprototype.streamlit.app/
---

## **🛠️ Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### **2️⃣ Set Up a Virtual Environment (Optional)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up the API Key**
Create a `.env` file in the root directory and add:
```
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## **🎯 Usage**
Run the chatbot locally with:
```sh
streamlit run app.py
```
This will launch the chatbot in your browser.

---

## **🚀 Deployment**
### **Option 1: Deploy on Streamlit Cloud**
1. **Push your code to GitHub**
2. **Go to** [Streamlit Cloud](https://share.streamlit.io/)
3. **Click "New App"** and select your repository
4. **Configure settings** (set `GEMINI_API_KEY` as an env variable)
5. **Click Deploy** 🚀

### **Option 2: Deploy on Render**
1. **Sign up on** [Render](https://render.com/)
2. **Create a new Web Service**
3. **Connect your GitHub repo**
4. **Set Start Command**:
   ```sh
   streamlit run app.py --server.port=10000
   ```
5. **Deploy!** 🚀

---

## **📝 Future Enhancements**
- 🎙️ **Add Voice Input** (speech-to-text)
- 🌍 **Multilingual Support**
- 🤖 **Fine-tune Gemini API for better contextual responses**

---

## **👨‍💻 Author**
**Kalash Jain** – Founder of NeuraMindsAI & ArogyaPath  
💻 AI & Tech Enthusiast | 🚀 Building Next-Gen AI Solutions  

🔗 **Website:** [NeuraMindsAI](https://neuramindsai.netlify.app)  
📧 **Email:** kalash.jain.211086@gmail.com 

---

## **⭐ Contribute**
If you like this project, feel free to **fork** and **contribute**! PRs are welcome. 😊

```sh
git clone https://github.com/your-username/your-repo-name.git
git checkout -b feature-branch
git commit -m "Added a new feature"
git push origin feature-branch
```

---

## **📜 License**
This project is licensed under the **MIT License**.  

