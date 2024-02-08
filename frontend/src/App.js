import "./App.css";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Splash from "./screens/Splash";
import SignInPage from "./screens/SignIn";
import Game from "./screens/GameScreen";
function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route
            path="playGame"
            element={
              <Game
                backgroundImageSRC="https://picsum.photos/1000/500"
                gameID="1"
              />
            }
          />
          <Route index element={<Splash />} />
          <Route path="signIn" element={<SignInPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
