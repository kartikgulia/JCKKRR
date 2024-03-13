import React, { useEffect } from "react";
import "./styles/App.css";
import {
  BrowserRouter,
  Routes,
  Route,
  useNavigate,
  useLocation,
} from "react-router-dom";

import Splash from "./screens/Splash";
import SignInPage from "./screens/SignIn";
import SignUpPage from "./screens/SignUp";
import Game from "./screens/GameScreen";
import LeaderboardScreen from "./screens/LeaderboardScreen";
import GameSelectScreen from "./screens/GameSelectScreen";
import ConditionalLogoutButton from "./components/ConditionalLogoutButton";
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
        </Routes>
      </BrowserRouter>
    </div>
  );
}

function SplashWithRedirect() {
  const navigate = useNavigate();

  useEffect(() => {
    const userToken = localStorage.getItem("userToken");
    if (userToken) {
      navigate("/");
    }
  }, [navigate]); // useEffect will only run once after the initial render
  // Render Splash component normally if there's no userToken
  return <Splash />;
}

export default App;
