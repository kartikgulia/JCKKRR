import "./styles/App.css";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Splash from "./screens/Splash";
import SignInPage from "./screens/SignIn";
import SignUpPage from "./screens/SignUp";
import Game from "./screens/GameScreen";
import LeaderboardScreen from "./screens/LeaderboardScreen";
import GameSelectScreen from "./screens/GameSelectScreen";
function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="playGame/:difficulty" element={<Game />} />
          <Route index element={<Splash />} />
          <Route path="signIn" element={<SignInPage />} />
          <Route path="signUp" element={<SignUpPage />} />
          <Route path="leaderboard" element={<LeaderboardScreen />} />
          <Route path="gameSelect" element={<GameSelectScreen />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
