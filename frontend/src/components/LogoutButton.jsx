import React from "react";
import { useNavigate } from "react-router-dom";

function LogoutButton() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("userToken"); // Remove the token from localStorage
    navigate("/signIn"); // Redirect to signIn page
  };

  return (
    <button
      onClick={handleLogout}
      style={{
        position: "absolute",
        top: "10px",
        right: "10px",
        fontSize: "16px", // Increase font size
        padding: "10px 20px", // Add more padding
        border: "none",
        backgroundColor: "#007bff", // Example blue background
        color: "white", // Text color
        cursor: "pointer", // Change cursor on hover
        borderRadius: "5px", // Rounded corners
      }}
    >
      Logout
    </button>
  );
}

export default LogoutButton;
