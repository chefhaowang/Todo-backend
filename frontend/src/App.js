import React, { useState, useEffect } from "react";
import axios from "axios";
import TodoList from "./components/TodoList";
import TodoForm from "./components/TodoForm";
import "./App.css"; // Import the CSS file

const App = () => {
  const [todos, setTodos] = useState([]);

  const fetchTodos = async () => {
    try {
      const response = await axios.get("http://localhost:8000/gettodo");
      setTodos(response.data);
    } catch (error) {
      console.error("Error fetching todos:", error);
    }
  };

  const addTodo = async (todo) => {
    try {
      await axios.post("http://localhost:8000/createtodo", todo);
      fetchTodos();
    } catch (error) {
      console.error("Error creating todo:", error);
    }
  };

  const updateTodo = async (todo) => {
    try {
      await axios.put("http://localhost:8000/updatetodo", todo);
      fetchTodos();
    } catch (error) {
      console.error("Error updating todo:", error);
    }
  };

  const deleteTodo = async (id) => {
    try {
      await axios.delete("http://localhost:8000/deletetodo", {
        data: { id },
      });
      fetchTodos();
    } catch (error) {
      console.error("Error deleting todo:", error);
    }
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  return (
    <div className="App">
      <h1>Todo List</h1>
      <TodoForm addTodo={addTodo} />
      <TodoList todos={todos} updateTodo={updateTodo} deleteTodo={deleteTodo} />
    </div>
  );
};

export default App;
