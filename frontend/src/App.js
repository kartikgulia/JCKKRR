import "./App.css";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Splash from "./screens/Splash";
import SignInPage from "./screens/SignIn";
function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route index element={<Splash />} />
          <Route path="signIn" element={<SignInPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
