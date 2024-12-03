import React, { useState } from "react";

const TodoForm = ({ addTodo }) => {
  const [content, setContent] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    const newTodo = {
      id: Date.now().toString(),
      content,
      added_time: new Date().toISOString(),
      last_update_time: new Date().toISOString(),
    };
    addTodo(newTodo);
    setContent(""); // Clear the input field
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Add a new todo"
        required
      />
      <button type="submit">Add Todo</button>
    </form>
  );
};

export default TodoForm;
