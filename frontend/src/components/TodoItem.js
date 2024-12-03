import React, { useState } from "react";

const TodoItem = ({ todo, updateTodo, deleteTodo }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [content, setContent] = useState(todo.content);

  const handleUpdate = () => {
    const updatedTodo = {
      ...todo,
      content,
      last_update_time: new Date().toISOString(),
    };
    updateTodo(updatedTodo);
    setIsEditing(false);
  };

  return (
    <div>
      {isEditing ? (
        <>
          <input
            type="text"
            value={content}
            onChange={(e) => setContent(e.target.value)}
          />
          <button onClick={handleUpdate}>Save</button>
        </>
      ) : (
        <span>{todo.content}</span>
      )}
      <button onClick={() => setIsEditing(!isEditing)}>
        {isEditing ? "Cancel" : "Edit"}
      </button>
      <button onClick={() => deleteTodo(todo.id)}>Delete</button>
    </div>
  );
};

export default TodoItem;
