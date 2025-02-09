import MyButton from "../UI/input/button/button";
import React from "react";
const Post = (props) => {
    return (
        <div className="post">
            <div className="post__content">
                <h1>{props.post.theme}</h1>
                <div>
                    {props.post.desc}   
                </div>
            </div>
            <div className="post__button">
                <MyButton onClick = {() => {props.remove(props.post)}}>Delete post</MyButton>
            </div>
        </div>
    )
}

export default Post;