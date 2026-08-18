import { useState } from "react";
import "./App.css";

const API = "http://127.0.0.1:8000";

function App() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadDocument = async () => {
    if (!file) {
      setMessage("Please select a document first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setMessage("");

    try {
      const response = await fetch(`${API}/upload`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Upload failed");
      }

      setMessage("✅ Document uploaded successfully!");
    } catch (error) {
      setMessage(`❌ ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  const askQuestion = async () => {
    if (!question.trim()) {
      setAnswer("Please enter a question.");
      return;
    }

    setLoading(true);
    setAnswer("");

    try {
      const response = await fetch(`${API}/ask`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Could not get answer");
      }

      setAnswer(data.answer || data.response || JSON.stringify(data));
    } catch (error) {
      setAnswer(`❌ ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <nav className="navbar">
        <div className="logo">🧠 DocMind AI</div>

        <div className="nav-links">
          <span>Home</span>
          <span>Documents</span>
          <span>AI Assistant</span>
        </div>
      </nav>

      <main>
        <section className="hero">
          <div className="badge">🤖 AI DOCUMENT ASSISTANT</div>

          <h1>
            Understand Your
            <span> Documents with AI</span>
          </h1>

          <p>
            Upload documents, ask questions, summarize content,
            and get intelligent answers instantly.
          </p>

          <div className="upload-card">
            <h2>📄 Upload Document</h2>

            <input
              type="file"
              accept=".pdf,.docx,.txt"
              onChange={(e) => setFile(e.target.files[0])}
            />

            {file && (
              <p className="filename">
                Selected: {file.name}
              </p>
            )}

            <button
              onClick={uploadDocument}
              disabled={loading}
            >
              {loading ? "Uploading..." : "Upload Document"}
            </button>

            {message && <div className="message">{message}</div>}
          </div>
        </section>

        <section className="assistant">
          <div className="assistant-card">
            <h2>✨ DocMind Assistant</h2>

            <p className="subtitle">
              What is this document about?
            </p>

            <textarea
              placeholder="Ask anything about your document..."
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
            />

            <button
              className="ask-button"
              onClick={askQuestion}
              disabled={loading}
            >
              {loading ? "Thinking..." : "Ask AI 🤖"}
            </button>

            {answer && (
              <div className="answer">
                <h3>🤖 Answer</h3>
                <p>{answer}</p>
              </div>
            )}
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;