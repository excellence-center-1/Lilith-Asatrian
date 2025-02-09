import { React, useState } from "react";
import "./styles/styles.css"  
import PostList from "./components/PostList"
import AddPost from "./components/AddPost"
import {BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from "./components/Login";
function App() {
  const [posts, setPosts] = useState([
    {id: 1, theme: "C++", desc: " pointers"},
    {id: 2, theme: "C++", desc: " references"}
  ])

  const createPost = (newPost) => {
    setPosts([...posts, newPost])
  }

  const removePost = (post) => {
    setPosts(posts.filter(p=>p.id!==post.id));
  }
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route path="/posts" element={
            <div>
              <AddPost create={createPost}/>
              <PostList remove = {removePost} post = {posts} title="Մի հրաշք էջ, Լիլիթի էջ"/>
            </div>
        }/>
      </Routes>
    </Router>
  );
}

export default App;
