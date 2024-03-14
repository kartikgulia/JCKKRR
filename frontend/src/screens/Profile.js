import React, { useEffect, useState } from "react";
import "../styles/ProfileScreen.css";
import SERVER_URL from "../config";
import { Link } from "react-router-dom";

const ProfileScreen = () => {
  const [errorMessage, setErrorMessage] = useState(null);

  const [name, setName] = useState(null);
  const [email, setEmail] = useState(null);
  const [easyScore, setEasyScore] = useState(null);
  const [mediumScore, setMediumScore] = useState(null);
  const [hardScore, setHardScore] = useState(null);
  useEffect(() => {
    const fetchProfileInfo = async () => {
      const userID = localStorage.getItem("userToken");
      const response = await fetch(
        `${SERVER_URL}/getProfileInfo?userID=${userID}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const data = await response.json();

      if (data.message === "Success") {
        // Navigate with useNavigate and pass state
        console.log(data.name);
        console.log(data.email);
        setName(data.name);
        setEmail(data.email);
        setEasyScore(data.easyScore);
        setMediumScore(data.mediumScore);
        setHardScore(data.hardScore);
      } else {
        setErrorMessage(data.message);
        console.log(errorMessage);
      }
    };

    fetchProfileInfo();
  });

  return (
    <div className="profile-container">
      <Link to="/gameSelect" className="back-button">
        Back
      </Link>
      <h2 className="profile-name">Hi, {name}</h2>
      <div className="scores">
        <p>
          <strong>Easy Score:</strong> {easyScore}
        </p>
        <p>
          <strong>Medium Score:</strong> {mediumScore}
        </p>
        <p>
          <strong>Hard Score:</strong> {hardScore}
        </p>
      </div>
      <p>
        <strong>Email:</strong> {email}
      </p>
    </div>
  );
};

export default ProfileScreen;
