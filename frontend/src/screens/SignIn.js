import React, { useState } from "react";
import SERVER_URL from "../config";
import { useNavigate } from "react-router-dom";
import "../styles/login.css";

function SignInPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [messageFromBackend, setMessageFromBackend] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    console.log("On Handle Submit Function");
    e.preventDefault();
    try {
      const response = await fetch(`${SERVER_URL}/signin`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });
      const data = await response.json();
      console.log(data); // Process the response data

      if (data.message === "Successfully logged in") {
        localStorage.setItem("userToken", data.token);
        console.log("Token saved to local storage");
        navigate("/gameSelect"); // Use navigate to redirect
      } else {
        setMessageFromBackend(data.message);
      }

      setMessageFromBackend(data.message);
    } catch (error) {
      console.error("Error during the sign in:", error);
      setMessageFromBackend("Error during Sign In. Reload and try again");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="background">
        <h1 className="title">Sign In</h1>
        <label>
          <h1 className="info">Username:</h1>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <label>
          <h1 className="info"> Password: </h1>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <button type="submit">Sign In</button>
        <h1>{messageFromBackend}</h1>
      </div>
    </form>
  );
}

export default SignInPage;
