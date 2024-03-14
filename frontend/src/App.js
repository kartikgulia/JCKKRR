import React, { useEffect } from "react";
import "./styles/App.css";
import { BrowserRouter, Routes, Route, useNavigate } from "react-router-dom";

import Splash from "./screens/Splash";
import SignInPage from "./screens/SignIn";
import SignUpPage from "./screens/SignUp";
import Game from "./screens/GameScreen";
import LeaderboardScreen from "./screens/LeaderboardScreen";
import GameSelectScreen from "./screens/GameSelectScreen";
import ProfileScreen from "./screens/Profile";
import ConditionalLogoutButton from "./components/ConditionalLogoutButton";
import SERVER_URL from "./config";

function App() {
  return (
    <div>
      <BrowserRouter>
        <ConditionalLogoutButton />

        <Routes>
          <Route path="playGame/:difficulty" element={<Game />} />
          <Route index element={<SplashWithRedirect />} />
          <Route path="signIn" element={<SignInPage />} />
          <Route path="signUp" element={<SignUpPage />} />
          <Route path="leaderboard" element={<LeaderboardScreen />} />
          <Route path="gameSelect" element={<GameSelectScreen />} />
          <Route path="profile" element={<ProfileScreen />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

function SplashWithRedirect() {
  const navigate = useNavigate();

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
        navigate("/gameSelect");
      } else {
      }
    };

    fetchProfileInfo();
  }, [navigate]);

  return <Splash />;
}

export default App;
