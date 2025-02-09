import Post from "./PostItem";
import React from "react";

const PostList = ({remove, post, title}) => {
    
    return (
        <>
            <h1 style={{textAlign: "center"}}>{title}</h1>
            {
              post.map(post=>
                <Post remove={remove} post={post} key={post.id}/>
              )
            }
        </>
        
    );
}

export default PostList;
