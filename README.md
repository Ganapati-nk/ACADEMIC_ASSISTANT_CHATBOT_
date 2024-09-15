<h1>Student Management System Chatbot</h1>

<p>This project is a <strong>conversational chatbot</strong> built using <strong>Streamlit</strong> and <strong>LangChain's Groq API</strong> integration. It helps users (students) ask questions about books, papers, and articles, while maintaining conversation flow and providing contextually relevant answers.</p>

<p>Check the live demo <a href="https://student-management-system-2-xl93.onrender.com/">here</a>.</p>


<h2>Features</h2>
<ul>
  <li><strong>Conversational Assistant</strong>: Provides responses related to books, papers, or articles based on user queries.</li>
  <li><strong>Contextual Responses</strong>: Tracks the history of the conversation, ensuring responses are coherent with previous interactions.</li>
  <li><strong>Streamlit Integration</strong>: The chatbot is deployed as a web app for easy user interaction.</li>
  <li><strong>LangChain & Groq API</strong>: Utilizes <code>LangChain</code> and <code>ChatGroq</code> for leveraging the <code>Gemma-7b-It</code> language model.</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.7+</li>
  <li>Streamlit</li>
  <li>LangChain</li>
  <li>LangChain Groq API</li>
  <li>Python Dotenv</li>
</ul>

<p>You can install all required dependencies via:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>Setup Instructions</h2>
<ol>
  <li><strong>Clone the repository</strong>:
    <pre><code>git clone https://github.com/your-repo/student-management-chatbot.git
cd student-management-chatbot</code></pre>
  </li>
  <li><strong>Set up environment variables</strong>:
    <p>Create a <code>.env</code> file in the root directory with your Groq API key:</p>
    <pre><code>GROQ_API_KEY=your_groq_api_key_here</code></pre>
  </li>
  <li><strong>Run the app</strong>:
    <pre><code>streamlit run app.py</code></pre>
  </li>
  <li><strong>Access the app</strong>:
    <p>Open your browser and go to <code>http://localhost:8501</code>.</p>
  </li>
</ol
