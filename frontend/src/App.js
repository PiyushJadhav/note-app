import "./App.css";
import { useState } from "react";
import axios from "axios";

function App() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/notes/", {
        title: title,
        content: content,
      });

      console.log("Note created:", response.data);

      setTitle("");
      setContent("");
      alert("You created your Note");
    } catch (error) {
      console.error("Error creating note", error);
    }
  };

  return (
    <div className="container">
      <h1>Create a Note!</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Title:
          <input
            id="title"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter a title"
          />
        </label>

        <label>
          Note:
          <input
            id="content"
            type="text"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            placeholder="Enter your notes"
          />
        </label>
        <button type="submit">Create Note</button>
      </form>
    </div>
  );
}

export default App;
