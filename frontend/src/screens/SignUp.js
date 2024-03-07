import React, { useState } from "react";
import SERVER_URL from "../config";
import { useNavigate } from "react-router-dom";
import "../styles/signup.css"; 

function SignUpPage(){
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();
  const [messageFromBackend, setMessageFromBackend] = useState("");

  const handleSubmit = async (e) => {
    console.log("On Handle Submit Function");
    e.preventDefault();
    try {
      const response = await fetch(`${SERVER_URL}/signup`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });
      const data = await response.json();
      console.log(data); // Process the response data

      if (data.message === "Successfully signed up") {
        navigate('/gameSelect'); // Use navigate to redirect
      } else {
        setMessageFromBackend(data.message);
      }

      setMessageFromBackend(data.message);
    } catch (error) {
      console.error("Error during the sign up:", error);
      setMessageFromBackend("Error during sign up. Reload and try again");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      
      <div className="background">
        <h1 className="title">Sign Up</h1>
        <label>
          <h1 className="info">Enter New Username:</h1>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <label>
          <h1 className="info"> Enter New Password: </h1>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <button type="submit">Sign Up</button>
        <h1>{messageFromBackend}</h1>
      </div>
      
    </form>
  );
}

export default SignUpPage;
