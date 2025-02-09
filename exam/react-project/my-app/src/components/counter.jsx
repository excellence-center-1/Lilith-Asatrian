import { useState } from "react";
const Counter = () => {
    const [likes, setLikes] = useState(0);
    const increment = () => {
        setLikes(likes+1);
    }
    const decrement = () => {
        setLikes(likes-1);
    }
    return (
        <>
            <h1>{likes}</h1>
            <button onClick={increment}>Like</button>
            <button onClick={decrement}>Dislike</button>    
        </>
    )
}

export default Counter