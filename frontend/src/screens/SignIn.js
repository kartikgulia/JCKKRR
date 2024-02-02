import React, { useState } from "react";
import SERVER_URL from "../config";

function SignInPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [messageFromBackend, setMessageFromBackend] = useState("");

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

      setMessageFromBackend(data.message);
    } catch (error) {
      console.error("Error during the sign in:", error);
      setMessageFromBackend("Error during Sign In. Reload and try again");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Sign In</h1>
      <div>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
      </div>
      <div>
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
      </div>
      <button type="submit">Sign In</button>

      <h1>{messageFromBackend}</h1>
    </form>
  );
}

export default SignInPage;
