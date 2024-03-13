import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Logout.css"

function LogoutButton() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("userToken"); // Remove the token from localStorage
    navigate("/signIn"); // Redirect to signIn page
  };

  return (
    <button
      className="logout-button"
      onClick={handleLogout}
    >
      Logout
    </button>
  );
}

export default LogoutButton;
