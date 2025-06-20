
import React, { useState } from 'react';
import './App.css';

function App() {
  const [chats, setChats] = useState([{ id: 1, name: "Chat 1", messages: [] }]);
  const [currentChatId, setCurrentChatId] = useState(1);
  const [input, setInput] = useState('');
  const [csvUploaded, setCsvUploaded] = useState(false);

  const currentChat = chats.find(chat => chat.id === currentChatId);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg = { type: 'user', text: input };

    const updatedChatsUser = chats.map(chat => {
      if (chat.id === currentChatId) {
        return { ...chat, messages: [...chat.messages, userMsg] };
      }
      return chat;
    });

    setChats(updatedChatsUser);
    setInput('');

    const botText = await generateBotResponse(input);
    const botMsg = { type: 'bot', text: botText };

    const updatedChatsWithBot = updatedChatsUser.map(chat => {
      if (chat.id === currentChatId) {
        return { ...chat, messages: [...chat.messages, botMsg] };
      }
      return chat;
    });

    setChats(updatedChatsWithBot);
  };

  const generateBotResponse = async (msg) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: msg }),
      });

      const data = await response.json();
      return data.answer || data.error || "No response received.";
    } catch (error) {
      console.error("Error fetching bot response:", error);
      return "Sorry, something went wrong while fetching the answer.";
    }
  };

  const handleNewChat = () => {
    const newId = chats.length + 1;
    const newChat = { id: newId, name: `Chat ${newId}`, messages: [] };
    setChats([...chats, newChat]);
    setCurrentChatId(newId);
  };

  const handleChatClick = (id) => {
    setCurrentChatId(id);
  };

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload-csv", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      if (data.message) {
        setCsvUploaded(true);
        alert("CSV uploaded successfully. You can now ask audit questions.");
      } else {
        alert("Upload failed.");
      }
    } catch (error) {
      alert("Upload failed. Please try again.");
      console.error(error);
    }
  };

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>Assistant</h2>
        <button onClick={handleNewChat} className="new-chat-btn">+ New Chat</button>
        <ul className="chat-list">
          {chats.map(chat => (
            <li
              key={chat.id}
              onClick={() => handleChatClick(chat.id)}
              className={chat.id === currentChatId ? 'active-chat' : ''}
            >
              {chat.name}
            </li>
          ))}
        </ul>
      </aside>

      <main className="chat-window">
        <div className="chat-history">
          {currentChat.messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${msg.type === 'user' ? 'user-message' : 'bot-message'}`}
            >
              <strong>{msg.type === 'user' ? 'You:' : 'Bot:'}</strong> {msg.text}
            </div>
          ))}
        </div>

        {/* CSV Upload section */}
        <div className="csv-upload">
          <label>
            Upload CSV for audit: &nbsp;
            <input type="file" onChange={handleFileUpload} />
          </label>
          {csvUploaded && <small style={{ color: 'lightgreen' }}>CSV uploaded </small>}
        </div>

        <div className="chat-input">
          <input
            type="text"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && handleSend()}
            placeholder="Ask anything..."
          />
          <button onClick={handleSend}>➤</button>
        </div>
      </main>
    </div>
  );
}

export default App;

