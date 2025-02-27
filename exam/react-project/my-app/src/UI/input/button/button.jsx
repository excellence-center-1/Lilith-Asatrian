import "./button.css"
import React from "react";
const MyButton = ({children, ...props}) => {
    return (
        <button className="button"{...props}>{children}</button>
    );
}

export default MyButton;