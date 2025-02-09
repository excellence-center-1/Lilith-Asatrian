import { React, useState } from "react";
import MyInput from "../UI/input/input";
import MyButton from "../UI/input/button/button";

const AddPost = ({create}) => {
    const [post, setPost] = useState({theme: "", desc: ""});
    const AddNewPost = (e) => {
        e.preventDefault();
        create({...post, id: Date.now()})
        setPost({theme: "", desc: ""});
    }
    return (
        <form>
            <MyInput type="text" placeholder="Post theme" value={post.theme} onChange={Event => {setPost({...post, theme: Event.target.value })}} />
            <MyInput type="text" placeholder="Post description" value={post.desc} onChange={Event => {setPost({...post, desc: Event.target.value})}}/>
            <MyButton onClick={AddNewPost}>Add Post</MyButton>
        </form>
    );
}

export default AddPost;

